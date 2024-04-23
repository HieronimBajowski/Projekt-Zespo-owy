import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta, date
import calendar


class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        self.root.geometry("800x600")

        self.current_date = datetime.now()
        self.current_option = None

        self.create_widgets()

    def create_widgets(self):
        self.option_var = tk.StringVar(value="")
        self.option_menu = ttk.Combobox(self.root, textvariable=self.option_var, values=["", "Day", "Week", "Month"],
                                        state="readonly")
        self.option_menu.pack(pady=20)
        self.option_menu.bind("<<ComboboxSelected>>", self.on_option_selected)

        # Pole, w którym będzie wyświetlane okno kalendarza
        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack(pady=10)



    def show_week_view(self):
        self.clear_calendar_frame()

        year_month_label = tk.Label(self.calendar_frame, text=self.current_date.strftime("%Y"), font=("Helvetica", 12))
        year_month_label.pack(pady=(10, 5))

        month_label = tk.Label(self.calendar_frame, text=self.current_date.strftime("%B"), font=("Helvetica", 28))
        month_label.pack(pady=5)

        week_number_label = tk.Label(self.calendar_frame, text=self.current_date.strftime("Week %W"),
                                     font=("Helvetica", 12))
        week_number_label.pack(pady=5)
        # Dodanie przycisków strzałek
        left_arrow_button = tk.Button(self.calendar_frame, text="<", font=("Helvetica", 16), padx=10, pady=5,
                                      command=self.prev_view)
        left_arrow_button.pack(side="left", padx=10)

        for i in range(7):
            day = self.current_date + timedelta(days=i - self.current_date.weekday())

            day_frame = tk.Frame(self.calendar_frame)
            day_frame.pack(side="left", padx=10)

            day_number_label = tk.Label(day_frame, text=day.strftime("%d"), font=("Helvetica", 26))
            day_number_label.pack()

            day_label = tk.Label(day_frame, text=day.strftime("%A"), font=("Helvetica", 12))
            day_label.pack()



        right_arrow_button = tk.Button(self.calendar_frame, text=">", font=("Helvetica", 16), padx=10, pady=5,
                                       command=self.next_view)
        right_arrow_button.pack(side="right", padx=10)
    def on_option_selected(self, event):
        selected_option = self.option_var.get()
        if selected_option == "":
            self.clear_calendar_frame()
            self.current_option = None
        elif selected_option == "Day":
            self.current_option = "Day"
            self.current_date = datetime.now()  # Ustaw obecną datę
            self.show_day_view()
        elif selected_option == "Week":
            self.current_option = "Week"
            self.current_date = datetime.now()  # Ustaw obecną datę
            self.show_week_view()
        elif selected_option == "Month":
            self.current_option = "Month"
            self.current_date = datetime.now()  # Ustaw obecną datę
            self.show_month_view()

    def show_day_view(self):
        self.clear_calendar_frame()

        year_label = tk.Label(self.calendar_frame, text=self.current_date.strftime("%Y"), font=("Helvetica", 12))
        year_label.pack(pady=10)

        month_label = tk.Label(self.calendar_frame, text=self.current_date.strftime("%B"), font=("Helvetica", 28))
        month_label.pack(pady=10)

        day_label = tk.Label(self.calendar_frame, text=self.current_date.strftime("%d"), font=("Helvetica", 78))
        day_label.pack(pady=10)

        day_of_week_label = tk.Label(self.calendar_frame, text=self.current_date.strftime("%A"),
                                     font=("Helvetica", 12, "bold"))
        day_of_week_label.pack(pady=10)

        # Dodanie przycisków strzałek
        left_arrow_button = tk.Button(self.calendar_frame, text="<", font=("Helvetica", 16), padx=10, pady=5,
                                      command=self.prev_view)
        left_arrow_button.pack(side="left", padx=10)

        right_arrow_button = tk.Button(self.calendar_frame, text=">", font=("Helvetica", 16), padx=10, pady=5,
                                       command=self.next_view)
        right_arrow_button.pack(side="right", padx=10)

    def show_month_view(self):
        self.clear_calendar_frame()

        year_label = tk.Label(self.calendar_frame, text=self.current_date.strftime("%Y"), font=("Helvetica", 12))
        year_label.pack(pady=(10, 5))

        month_label = tk.Label(self.calendar_frame, text=self.current_date.strftime("%B"), font=("Helvetica", 28))
        month_label.pack(pady=5)

        days_frame = tk.Frame(self.calendar_frame)
        days_frame.pack()

        for i, day_name in enumerate(calendar.day_abbr):
            day_name_label = tk.Label(days_frame, text=day_name, font=("Helvetica", 12, "bold"))
            day_name_label.grid(row=0, column=i, padx=10)

        cal = calendar.monthcalendar(self.current_date.year, self.current_date.month)
        for week_num, week in enumerate(cal, start=1):
            for day_num, day in enumerate(week):
                if day != 0:
                    day_label = tk.Label(days_frame, text=str(day), font=("Helvetica", 16))
                    day_label.grid(row=week_num, column=day_num, padx=10, pady=5)

        # Dodanie przycisków strzałek pod kalendarzem
        left_arrow_button = tk.Button(self.calendar_frame, text="<", font=("Helvetica", 16), padx=10, pady=5,
                                      command=self.prev_view)
        left_arrow_button.pack(side="left", padx=10)

        right_arrow_button = tk.Button(self.calendar_frame, text=">", font=("Helvetica", 16), padx=10, pady=5,
                                       command=self.next_view)
        right_arrow_button.pack(side="right", padx=10)

    def clear_calendar_frame(self):
        # Usunięcie wszystkich widgetów z pola kalendarza
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

    def prev_view(self):
        if self.current_option == "Day":
            self.current_date -= timedelta(days=1)
            self.show_day_view()
        elif self.current_option == "Week":
            self.current_date -= timedelta(weeks=1)
            self.show_week_view()
        elif self.current_option == "Month":
            self.current_date = self.current_date.replace(day=1) - timedelta(days=1)
            self.show_month_view()

    def next_view(self):
        if self.current_option == "Day":
            self.current_date += timedelta(days=1)
            self.show_day_view()
        elif self.current_option == "Week":
            self.current_date += timedelta(weeks=1)
            self.show_week_view()
        elif self.current_option == "Month":
            next_month_days = calendar.monthrange(self.current_date.year, self.current_date.month)[1]
            self.current_date = self.current_date.replace(day=next_month_days) + timedelta(days=1)
            self.show_month_view()


root = tk.Tk()
app = CalendarApp(root)
root.mainloop()
