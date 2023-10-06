import os
import csv
import argparse
from datetime import datetime, time
from operator import itemgetter


class Schedule:
    def __init__(
        self,
        name,
        description,
        activity_dates,
        scheduled_days,
        scheduled_start_time,
        scheduled_end_time,
        duration,
        allocated_location_name,
        allocated_staff_name,
        zone_name,
    ):
        self.name = name
        self.description = description
        self.activity_dates = activity_dates
        self.scheduled_days = scheduled_days
        self.scheduled_start_time = scheduled_start_time
        self.scheduled_end_time = scheduled_end_time
        self.duration = duration
        self.allocated_location_name = allocated_location_name
        self.allocated_staff_name = allocated_staff_name
        self.zone_name = zone_name


def load_data(folder_path):
    schedules = []
    folder_path ='d:\Yona\BCS\Algorithms and Data Structures\dataset'
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            with open(os.path.join(folder_path, filename), "r") as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    schedule = Schedule(
                        row["Name"],
                        row["Description"],
                        row["Activity Dates (Individual)"],
                        row["Scheduled Days"],
                        row["Scheduled Start Time"],
                        row["Scheduled End Time"],
                        row["Duration"],
                        row["Allocated Location Name"],
                        row["Allocated Staff Name"],
                        row["Zone Name"],
                    )
                    schedules.append(schedule)
    return schedules


def day_of_week_to_number(day):
    day_mapping = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7,
    }
    return day_mapping.get(day, 0)


def merge(left, right, sort_field, sort_order):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        left_value = getattr(left[i], sort_field)
        right_value = getattr(right[j], sort_field)

        # Convert values to datetime for comparison if they are in a date-like format
        if sort_field == "scheduled_days":
            left_value = day_of_week_to_number(left_value)
            right_value = day_of_week_to_number(right_value)
        elif isinstance(left_value, str) and "/" in left_value:
            left_value = datetime.strptime(left_value, "%d/%m/%Y")
        if isinstance(right_value, str) and "/" in right_value:
            right_value = datetime.strptime(right_value, "%d/%m/%Y")
        if isinstance(left_value, str) and ":" in left_value:
            left_value = datetime.strptime(left_value, "%H:%M:%S").time()
        if isinstance(right_value, str) and ":" in right_value:
            right_value = datetime.strptime(right_value, "%H:%M:%S").time()

        if sort_order == "asc":
            if left_value <= right_value:
                merged.append(left[i])
                i += 1
            elif left_value > right_value:
                merged.append(right[j])
                j += 1
        else:
            if left_value <= right_value:
                merged.append(right[j])
                j += 1
            elif left_value > right_value:
                merged.append(left[i])
                i += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def merge_sort(arr, sort_field, sort_order):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left, sort_field, sort_order)
    right = merge_sort(right, sort_field, sort_order)

    return merge(left, right, sort_field, sort_order)


def print_schedule_info(filtered_schedules):
    print(
        "\n{:<55} {:<15} {:<10} {:<15} {:<15} {:<20} {:<10} {:<20}".format(
            "Module Name",
            "Date",
            "Day",
            "Start Time",
            "End Time",
            "Location",
            "Duration",
            "Staff Name",
        )
    )
    print("-" * 170)  # Horizontal line for separation

    for schedule in filtered_schedules:
        print(
            "{:<55} {:<15} {:<10} {:<15} {:<15} {:<20} {:<10} {:<20}".format(
                schedule.description,
                schedule.activity_dates,
                schedule.scheduled_days,
                schedule.scheduled_start_time,
                schedule.scheduled_end_time,
                schedule.allocated_location_name,
                schedule.duration,
                schedule.allocated_staff_name,
            )
        )


def list_schedules(schedules, key, sort_field, sort_fields, **kwargs):
    filtered_schedules = []

    try:
        if key == "module":
            module_name = sort_field
            for schedule in schedules:
                if schedule.description == module_name:
                    filtered_schedules.append(schedule)
        elif key == "lecturer":
            lecturer_name = sort_field
            for schedule in schedules:
                if schedule.allocated_staff_name == lecturer_name:
                    filtered_schedules.append(schedule)
        elif key == "location":
            location = sort_field
            for schedule in schedules:
                if schedule.allocated_location_name == location:
                    filtered_schedules.append(schedule)
        elif key == "date":
            for schedule in schedules:
                schedule_date = datetime.strptime(schedule.activity_dates, "%d/%m/%Y")
                if kwargs["date"] == schedule_date:
                    filtered_schedules.append(schedule)
        elif key == "date_range":
            for schedule in schedules:
                schedule_date = datetime.strptime(schedule.activity_dates, "%d/%m/%Y")
                if kwargs["start_date"] <= schedule_date <= kwargs["end_date"]:
                    filtered_schedules.append(schedule)
        elif key == "specific_time":
            for schedule in schedules:
                schedule_start_time = datetime.strptime(
                    schedule.scheduled_start_time, "%H:%M:%S"
                ).time()
                schedule_end_time = datetime.strptime(
                    schedule.scheduled_end_time, "%H:%M:%S"
                ).time()
                if schedule_start_time <= kwargs["specific_time"] <= schedule_end_time:
                    filtered_schedules.append(schedule)
        elif key == "time_range":
            for schedule in schedules:
                schedule_start_time = datetime.strptime(
                    schedule.scheduled_start_time, "%H:%M:%S"
                ).time()
                schedule_end_time = datetime.strptime(
                    schedule.scheduled_end_time, "%H:%M:%S"
                ).time()
                if (
                    kwargs["start_time"] <= schedule_start_time <= kwargs["end_time"]
                    or kwargs["start_time"] <= schedule_end_time <= kwargs["end_time"]
                ):
                    filtered_schedules.append(schedule)
        elif key == "day":
            day_to_search = sort_field.capitalize()
            for schedule in schedules:
                if day_to_search == schedule.scheduled_days:
                    filtered_schedules.append(schedule)
        else:
            raise ValueError("Invalid key.")
    except ValueError as e:
        print(f"Error: {e}")

    # Apply sorting based on the specified sort fields and orders
    for sort_field, sort_order in sort_fields[::-1]:
        filtered_schedules = merge_sort(filtered_schedules, sort_field, sort_order)

    return filtered_schedules


def sort_schedules(schedules, field, order):
    if order == "asc":
        return sorted(schedules, key=lambda x: getattr(x, field))
    elif order == "desc":
        return sorted(schedules, key=lambda x: getattr(x, field), reverse=True)
    else:
        raise ValueError("Invalid sort order.")


def choose_sort_columns():
    sort_fields = []

    print("Available columns to sort:")
    print("1. Module Name")
    print("2. Date")
    print("3. Day")
    print("4. Start Time")
    print("5. End Time")
    print("6. Location")
    print("7. Duration")
    print("8. Staff Name")

    while True:
        column_choice = input(
            "Enter the number of the column to sort (or 'q' to quit sorting): "
        )

        if column_choice.lower() == "q":
            break

        column_mapping = {
            "1": "description",
            "2": "activity_dates",
            "3": "scheduled_days",
            "4": "scheduled_start_time",
            "5": "scheduled_end_time",
            "6": "allocated_location_name",
            "7": "duration",
            "8": "allocated_staff_name",
        }

        sort_field = column_mapping.get(column_choice, None)
        if sort_field:
            sort_order = input("Enter the sort order ('asc' or 'desc'): ").lower()
            if sort_order not in ["asc", "desc"]:
                print("Invalid sort order. Defaulting to 'asc'.")
                sort_order = "asc"
            sort_fields.append((sort_field, sort_order))
            break
        else:
            print("Invalid choice. Please try again.")

    return sort_fields


def main():
    parser = argparse.ArgumentParser(description="View, list, and sort timetables.")
    parser.add_argument(
        "-f",
        "--folder",
        type=str,
        required=False,
        help="Path to the folder containing the CSV files.",
    )
    args = parser.parse_args()

    folder_path = args.folder
    schedules = load_data(folder_path)

    while True:
        print("\nSelect an option:")
        print("1. List all sessions by module name")
        print("2. List all sessions by lecturer name")
        print("3. List all sessions by location/room")
        print("4. List all sessions by date")
        print("5. List all sessions by date range")
        print("6. List all sessions by specific time")
        print("7. List all sessions by time range")
        print("8. List all sessions by day")
        print("9. Quit")

        table = None
        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "8"]:
            key = {
                "1": "module",
                "2": "lecturer",
                "3": "location",
                "8": "day",
            }[choice]
            filter_input = input(f"Enter the {key.replace('_', ' ')}: ")
            sort_key = choose_sort_columns()
            table = list_schedules(schedules, key, filter_input, sort_key)
        elif choice == "4":
            sort_key = choose_sort_columns()
            date = datetime.strptime(
                input("Enter the date (format: dd/mm/yyyy): "), "%d/%m/%Y"
            )
            table = list_schedules(schedules, "date", None, sort_key, date=date)
        elif choice == "5":
            sort_key = choose_sort_columns()
            start_date = datetime.strptime(
                input("Enter the start date (format: dd/mm/yyyy): "), "%d/%m/%Y"
            )
            end_date = datetime.strptime(
                input("Enter the end date (format: dd/mm/yyyy): "), "%d/%m/%Y"
            )
            table = list_schedules(
                schedules,
                "date_range",
                None,
                sort_key,
                start_date=start_date,
                end_date=end_date,
            )
        elif choice == "6":
            sort_key = choose_sort_columns()
            specific_time = datetime.strptime(
                input("Enter the specific time (format: HH:MM:SS): "), "%H:%M:%S"
            ).time()
            table = list_schedules(
                schedules, "specific_time", None, sort_key, specific_time=specific_time
            )
        elif choice == "7":
            sort_key = choose_sort_columns()
            start_time = datetime.strptime(
                input("Enter the start time (format: HH:MM:SS): "), "%H:%M:%S"
            ).time()
            end_time = datetime.strptime(
                input("Enter the end time (format: HH:MM:SS): "), "%H:%M:%S"
            ).time()
            table = list_schedules(
                schedules,
                "time_range",
                None,
                sort_key,
                start_time=start_time,
                end_time=end_time,
            )
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")

        if table:
            print_schedule_info(table)


if __name__ == "__main__":
    main()
