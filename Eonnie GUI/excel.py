import pandas as pd
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Alignment


def export_timetable_to_excel(schedules):
    # Create a new Excel workbook
    workbook = Workbook()

    # Generate the timetable for each week
    for week_num, week_schedules in enumerate(
        group_schedules_by_week(schedules), start=1
    ):
        # Create a new worksheet for each week
        worksheet = workbook.create_sheet(title=f"Week {week_num}")

        # Create the timetable header row
        header_row = ["Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        worksheet.append(header_row)

        # Generate the timetable rows for each hour
        for hour in range(24):
            timetable_row = [f"{hour}:00 - {hour + 1}:00"] + [""] * 5
            for schedule in week_schedules:
                if schedule_in_hour_range(schedule, hour):
                    day_index = get_day_index(schedule.scheduled_days)
                    timetable_row[
                        day_index
                    ] = f"{schedule.description}\n({schedule.allocated_location_name})"

            worksheet.append(timetable_row)

        # Set the column widths and alignment
        for col_num in range(1, len(header_row) + 1):
            col_letter = chr(
                64 + col_num
            )  # Convert column number to Excel column letter
            worksheet.column_dimensions[col_letter].width = 15  # Set column width
            for cell in worksheet[col_letter]:
                cell.alignment = Alignment(wrapText=True)  # Wrap text for each cell

    # Remove the default sheet created by openpyxl
    default_sheet = workbook["Sheet"]
    workbook.remove(default_sheet)

    return workbook


def group_schedules_by_week(schedules):
    week_schedule_groups = {}  # Dictionary to store schedules grouped by week
    for schedule in schedules:
        activity_dates = schedule.activity_dates
        start_date = datetime.strptime(activity_dates, "%d/%m/%Y")

        # Calculate the week number (ISO week, starting from Monday)
        week_num = start_date.strftime("%U")

        if week_num not in week_schedule_groups:
            week_schedule_groups[week_num] = []

        week_schedule_groups[week_num].append(schedule)

    return week_schedule_groups.values()


def schedule_in_hour_range(schedule, hour):
    start_hour = int(schedule.scheduled_start_time.split(":")[0])
    end_hour = int(schedule.scheduled_end_time.split(":")[0])
    return start_hour <= hour < end_hour


def get_day_index(day):
    day_mapping = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
    }
    return day_mapping.get(day, -1)
