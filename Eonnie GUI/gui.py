import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from generator import load_data, list_schedules
from excel import export_timetable_to_excel
from datetime import datetime


class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Schedule Viewer")
        self.folder_path = ""
        self.schedules = []
        self.list_method = tk.StringVar()
        self.sort_column = tk.StringVar()
        self.sort_order = tk.StringVar()
        self.filter_input = tk.StringVar()
        self.initialize_gui()

    def initialize_gui(self):
        ttk.Label(self.root, text="Load Folder Section:").pack(pady=(10, 5))

        load_folder_frame = ttk.Frame(self.root)
        load_folder_frame.pack(pady=5)
        self.load_button = ttk.Button(
            load_folder_frame,
            text="Load Folder",
            command=self.select_folder,
            style="Red.TButton",
        )
        self.load_button.grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(
            load_folder_frame, text="List Schedules", command=self.list_schedules
        ).grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="List Methods Section:").pack(pady=5)

        list_method_frame = ttk.Frame(self.root)
        list_method_frame.pack(pady=5)

        list_method_options = [
            ("1. List all sessions by module name", "module"),
            ("2. List all sessions by lecturer name", "lecturer"),
            ("3. List all sessions by location/room", "location"),
            ("4. List all sessions by date", "date"),
            ("5. List all sessions by date range", "date_range"),
            ("6. List all sessions by specific time", "specific_time"),
            ("7. List all sessions by time range", "time_range"),
            ("8. List all sessions by day", "day"),
        ]

        for text, value in list_method_options:
            ttk.Radiobutton(
                list_method_frame, text=text, variable=self.list_method, value=value
            ).pack(anchor=tk.W)

        ttk.Label(self.root, text="Sort Options Section:").pack(pady=5)

        sort_options_frame = ttk.Frame(self.root)
        sort_options_frame.pack(pady=5)

        sort_options = [
            ("1. Module Name", "description"),
            ("2. Date", "activity_dates"),
            ("3. Day", "scheduled_days"),
            ("4. Start Time", "scheduled_start_time"),
            ("5. End Time", "scheduled_end_time"),
            ("6. Location", "allocated_location_name"),
            ("7. Duration", "duration"),
            ("8. Staff Name", "allocated_staff_name"),
        ]

        for text, value in sort_options:
            ttk.Radiobutton(
                sort_options_frame, text=text, variable=self.sort_column, value=value
            ).pack(anchor=tk.W)

        ttk.Label(sort_options_frame, text="Sort Order:").pack(anchor=tk.W)
        ttk.Radiobutton(
            sort_options_frame, text="Ascending", variable=self.sort_order, value="asc"
        ).pack(anchor=tk.W)
        ttk.Radiobutton(
            sort_options_frame,
            text="Descending",
            variable=self.sort_order,
            value="desc",
        ).pack(anchor=tk.W)

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.load_button.configure(style="Green.TButton")
            self.schedules = load_data(self.folder_path)
            messagebox.showinfo("Schedules Loaded", "Schedules loaded successfully.")

    def list_schedules(self):
        if not self.folder_path:
            messagebox.showerror("Error", "Please load a folder first.")
            return

        list_method = self.list_method.get()
        sort_column = self.sort_column.get()
        sort_order = self.sort_order.get()

        # Get user input for filter criteria
        user_input = None

        if list_method == "day":
            user_input = self.get_user_date_time_input("day")
        elif list_method == "date":
            user_input = self.get_user_date_time_input("date")
        elif list_method == "date_range":
            user_input = self.get_user_date_time_input("start_date")
            if user_input is not None:
                user_input_end = self.get_user_date_time_input("end_date")
                if user_input_end is None:
                    user_input = None
        elif list_method == "specific_time":
            user_input = self.get_user_date_time_input("specific_time")
        elif list_method == "time_range":
            user_input = self.get_user_date_time_input("start_time")
            if user_input is not None:
                user_input_end = self.get_user_date_time_input("end_time")
                if user_input_end is None:
                    user_input = None
        else:
            user_input = simpledialog.askstring(
                "Input", f"Enter the {list_method.replace('_', ' ')}:"
            )

        if user_input is None and list_method not in [
            "day",
            "date",
            "date_range",
            "specific_time",
            "time_range",
        ]:
            messagebox.showerror("Error", "Please enter a filter input.")
            return

        sort_key = [(sort_column, sort_order)] if sort_column and sort_order else []
        if list_method == "date":
            filtered_schedules = list_schedules(
                self.schedules, "date", None, sort_key, date=user_input
            )
        elif list_method == "date_range":
            filtered_schedules = list_schedules(
                self.schedules,
                "date_range",
                None,
                sort_key,
                start_date=user_input,
                end_date=user_input_end,
            )
        elif list_method == "specific_time":
            filtered_schedules = list_schedules(
                self.schedules,
                "specific_time",
                None,
                sort_key,
                specific_time=user_input,
            )
        elif list_method == "time_range":
            filtered_schedules = list_schedules(
                self.schedules,
                "time_range",
                None,
                sort_key,
                start_time=user_input,
                end_time=user_input_end,
            )
        else:
            filtered_schedules = list_schedules(
                self.schedules, list_method, user_input, sort_key
            )

        # Display results in a pop-up window as a table
        self.display_schedule_table(filtered_schedules)

    def get_user_date_time_input(self, input_type):
        user_input = None
        if input_type == "day":
            user_input = simpledialog.askstring("Input", "Enter the day:")
            if user_input:
                if not user_input.lower() in (
                    "monday",
                    "tuesday",
                    "wednesday",
                    "thursday",
                    "friday",
                    "saturday",
                    "sunday",
                ):
                    messagebox.showerror(
                        "Error", "Invalid date format. Please use dd/mm/yyyy."
                    )
        elif input_type == "date":
            user_input = simpledialog.askstring(
                "Input", "Enter the date (format: dd/mm/yyyy):"
            )
            if user_input:
                try:
                    return datetime.strptime(user_input, "%d/%m/%Y")
                except ValueError:
                    messagebox.showerror(
                        "Error", "Invalid date format. Please use dd/mm/yyyy."
                    )
        elif input_type == "start_date":
            user_input = simpledialog.askstring(
                "Input", "Enter the start date (format: dd/mm/yyyy):"
            )
            if user_input:
                try:
                    return datetime.strptime(user_input, "%d/%m/%Y")
                except ValueError:
                    messagebox.showerror(
                        "Error", "Invalid date format. Please use dd/mm/yyyy."
                    )
        elif input_type == "end_date":
            user_input = simpledialog.askstring(
                "Input", "Enter the end date (format: dd/mm/yyyy):"
            )
            if user_input:
                try:
                    return datetime.strptime(user_input, "%d/%m/%Y")
                except ValueError:
                    messagebox.showerror(
                        "Error", "Invalid date format. Please use dd/mm/yyyy."
                    )
        elif input_type == "specific_time":
            user_input = simpledialog.askstring(
                "Input", "Enter the specific time (format: HH:MM:SS):"
            )
            if user_input:
                try:
                    return datetime.strptime(user_input, "%H:%M:%S").time()
                except ValueError:
                    messagebox.showerror(
                        "Error", "Invalid time format. Please use HH:MM:SS."
                    )
        elif input_type == "start_time":
            user_input = simpledialog.askstring(
                "Input", "Enter the start time (format: HH:MM:SS):"
            )
            if user_input:
                try:
                    return datetime.strptime(user_input, "%H:%M:%S").time()
                except ValueError:
                    messagebox.showerror(
                        "Error", "Invalid time format. Please use HH:MM:SS."
                    )
        elif input_type == "end_time":
            user_input = simpledialog.askstring(
                "Input", "Enter the end time (format: HH:MM:SS):"
            )
            if user_input:
                try:
                    return datetime.strptime(user_input, "%H:%M:%S").time()
                except ValueError:
                    messagebox.showerror(
                        "Error", "Invalid time format. Please use HH:MM:SS."
                    )
        return user_input

    def display_schedule_table(self, schedules):
        table_window = tk.Toplevel(self.root)
        table_window.title("Schedule Table")

        tree = ttk.Treeview(table_window)
        tree["columns"] = (
            "Description",
            "Activity Dates",
            "Scheduled Days",
            "Start Time",
            "End Time",
            "Location",
            "Duration",
            "Staff Name",
        )
        tree.heading("#0", text="Module Name")

        for col in tree["columns"]:
            width = 250 if col in ["Description", "Module Name"] else 100
            tree.column(col, width=width, anchor=tk.W)
            tree.heading(col, text=col)

        for schedule in schedules:
            tree.insert(
                "",
                "end",
                text=schedule.description,
                values=(
                    schedule.description,
                    schedule.activity_dates,
                    schedule.scheduled_days,
                    schedule.scheduled_start_time,
                    schedule.scheduled_end_time,
                    schedule.allocated_location_name,
                    schedule.duration,
                    schedule.allocated_staff_name,
                ),
            )

        tree.pack(expand=True, fill="both")

        # Add a button to generate Excel timetable
        generate_excel_button = ttk.Button(
            table_window,
            text="Generate Excel",
            command=lambda: self.generate_excel_timetable(schedules),
        )
        generate_excel_button.pack(pady=10)

    def generate_excel_timetable(self, schedules):
        if not self.folder_path:
            messagebox.showerror("Error", "Please load a folder first.")
            return

        # Generate the Excel timetable
        excel_workbook = export_timetable_to_excel(schedules)

        # Ask user for the save location and filename for the Excel workbook
        save_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx", filetypes=[("Excel Workbook", "*.xlsx")]
        )

        if save_path:
            excel_workbook.save(save_path)
            messagebox.showinfo(
                "Export Complete", "Timetable exported to Excel successfully."
            )


if __name__ == "__main__":
    root = tk.Tk()

    style = ttk.Style()
    style.configure("Red.TButton", background="red")
    style.configure("Green.TButton", background="green")

    app = ScheduleApp(root)
    root.mainloop()
