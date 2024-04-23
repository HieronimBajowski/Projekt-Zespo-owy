import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta, date
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        self.root.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.option_var = tk.StringVar(value="")
        self.option_menu = ttk.Combobox(self.root, textvariable=self.option_var, values=["", "Day", "Week", "Month"], state="readonly")
        self.option_menu.pack(pady=20)
        self.option_menu.bind("<<ComboboxSelected>>", self.on_option_selected)

        # Pole, w którym będzie wyświetlane okno kalendarza
        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack(pady=10)

    def on_option_selected(self, event):
        selected_option = self.option_var.get()
        if selected_option == "":
            self.clear_calendar_frame()
        elif selected_option == "Day":
            self.create_day_view()
        elif selected_option == "Week":
            self.create_week_view()
        elif selected_option == "Month":
            self.create_month_view()

    def create_day_view(self):
        # Usunięcie poprzedniego okna kalendarza, jeśli istnieje
        self.clear_calendar_frame()

        current_date = datetime.now()

        year_label = tk.Label(self.calendar_frame, text=current_date.strftime("%Y"), font=("Helvetica", 12))
        year_label.pack(pady=10)

        month_label = tk.Label(self.calendar_frame, text=current_date.strftime("%B"), font=("Helvetica", 28))
        month_label.pack(pady=10)

        day_label = tk.Label(self.calendar_frame, text=current_date.strftime("%d"), font=("Helvetica", 78))
        day_label.pack(pady=10)

        day_of_week_label = tk.Label(self.calendar_frame, text=current_date.strftime("%A"), font=("Helvetica", 12, "bold"))
        day_of_week_label.pack(pady=10)

    def create_week_view(self):
        # Usunięcie poprzedniego okna kalendarza, jeśli istnieje
        self.clear_calendar_frame()

        current_date = datetime.now()
        current_weekday = current_date.weekday()
        week_start = current_date - timedelta(days=current_weekday)
        week_end = week_start + timedelta(days=6)

        year_month_label = tk.Label(self.calendar_frame, text=week_start.strftime("%Y"), font=("Helvetica", 12))
        year_month_label.pack(pady=(10, 5))  # Dodaj większą przerwę przed miesiącem

        month_label = tk.Label(self.calendar_frame, text=week_start.strftime("%B"), font=("Helvetica", 28))
        month_label.pack(pady=5)

        week_number_label = tk.Label(self.calendar_frame, text=week_start.strftime("Week %W"), font=("Helvetica", 12))
        week_number_label.pack(pady=5)

        days_frame = tk.Frame(self.calendar_frame)
        days_frame.pack()

        for i in range(7):
            day = week_start + timedelta(days=i)

            day_frame = tk.Frame(days_frame)
            day_frame.pack(side="left", padx=10)

            day_number_label = tk.Label(day_frame, text=day.strftime("%d"), font=("Helvetica", 26))
            day_number_label.pack()

            day_label = tk.Label(day_frame, text=day.strftime("%A"), font=("Helvetica", 12))
            if i == current_weekday:
                day_label.config(fg="blue")
            day_label.pack()

    def create_month_view(self):
        # Usunięcie poprzedniego okna kalendarza, jeśli istnieje
        self.clear_calendar_frame()

        current_date = datetime.now()
        year = current_date.year
        month = current_date.month

        year_label = tk.Label(self.calendar_frame, text=year, font=("Helvetica", 12))
        year_label.pack(pady=(10, 5))

        month_label = tk.Label(self.calendar_frame, text=calendar.month_name[month], font=("Helvetica", 28))
        month_label.pack(pady=5)

        days_frame = tk.Frame(self.calendar_frame)
        days_frame.pack()

        for i, day_name in enumerate(calendar.day_abbr):
            day_name_label = tk.Label(days_frame, text=day_name, font=("Helvetica", 12, "bold"))
            day_name_label.grid(row=0, column=i, padx=10)

        cal = calendar.monthcalendar(year, month)
        for week_num, week in enumerate(cal, start=1):
            for day_num, day in enumerate(week):
                if day != 0:
                    day_label = tk.Label(days_frame, text=str(day), font=("Helvetica", 16))
                    day_label.grid(row=week_num, column=day_num, padx=10, pady=5)
                    if day == current_date.day:
                        day_label.config(fg="blue")

    def clear_calendar_frame(self):
        # Usunięcie wszystkich widgetów z pola kalendarza
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

root = tk.Tk()
app = CalendarApp(root)
root.mainloop()
