import tkinter as tk
from tkinter import messagebox
import calendar, math
from datetime import datetime

def show_splash_then_main(delay_ms=1200):
    splash = tk.Tk()
    splash.overrideredirect(True)

    sw = splash.winfo_screenwidth()
    sh = splash.winfo_screenheight()
    w, h = 600, 160
    x = (sw - w) // 2
    y = (sh - h) // 3
    splash.geometry(f"{w}x{h}+{x}+{y}")
    splash.configure(bg="#2E86C1")

    tk.Label(
        splash, text="✨ Welcome to Smart Daily Routine Optimizer ✨",
        font=("Helvetica", 17, "bold"), bg="#2E86C1", fg="white"
    ).pack(expand=True, pady=(18, 0))

    tk.Label(
        splash, text="Your discipline today decides your future tomorrow.",
        font=("Helvetica", 12, "italic"), bg="#2E86C1", fg="#F0F3F4"
    ).pack()

    splash.after(delay_ms, splash.destroy)
    splash.mainloop()

class RoutineApp:
    def __init__(self, root):

        self.root = root
        root.title("Smart Daily Routine Optimizer — Final")
        root.geometry("1150x660")
        root.resizable(False, False)

        container_outer = tk.Frame(root, bd=2, relief="groove", bg="#F7F7F7")
        container_outer.pack(fill='both', expand=True, padx=8, pady=8)

        banner = tk.Label(
            container_outer,
            text="✨ Welcome! Build Your Powerful Daily Routine ✨",
            font=("Helvetica", 16, "bold"),
            bg="#2E86C1",
            fg="white",
            pady=10
        )
        banner.pack(fill='x')

        row = tk.Frame(container_outer, bg="#F7F7F7")
        row.pack(fill='both', expand=True, padx=10, pady=10)

        self.left = tk.Frame(row, width=280, bg="#F7F7F7")
        self.left.pack(side='left', fill='y', padx=(0, 12))

        self.middle = tk.Frame(row, width=580, bg="#F7F7F7")
        self.middle.pack(side='left', fill='both', expand=True, padx=(0, 12))

        self.right = tk.Frame(row, width=260, bg="#F7F7F7")
        self.right.pack(side='right', fill='y')

        self.build_left()
        self.build_middle()
        self.build_right_inputs()

        self.update_digital_clock()
        self.update_analog_clock()


    def build_left(self):

        self.date_label = tk.Label(self.left, text="", font=("Helvetica", 12), bg="#F7F7F7")
        self.date_label.pack(pady=(4, 0))

        self.time_label = tk.Label(self.left, text="", font=("Helvetica", 18, "bold"), bg="#F7F7F7")
        self.time_label.pack()

        self.canvas = tk.Canvas(self.left, width=220, height=220, bg="white", bd=2, relief="ridge")
        self.canvas.pack(pady=(10, 8))

        quote = "“Your discipline today decides your future tomorrow.”"
        tk.Label(
            self.left, text=quote,
            font=("Helvetica", 10, "bold"),
            wraplength=220, justify="center", bg="#F7F7F7"
        ).pack(pady=(4, 12))

        tk.Label(
            self.left, text="-- Focus Timer (minutes) --",
            font=("Helvetica", 10, "bold"), bg="#F7F7F7"
        ).pack(pady=(18, 4))

        row = tk.Frame(self.left, bg="#F7F7F7")
        row.pack()

        self.timer_entry = tk.Entry(row, width=6, justify='center')
        self.timer_entry.pack(side='left')
        self.timer_entry.insert(0, "25")

        tk.Button(row, text="Start", width=6, command=self.start_timer).pack(side='left', padx=4)
        tk.Button(row, text="Stop", width=6, command=self.stop_timer).pack(side='left', padx=4)
        tk.Button(row, text="Reset", width=6, command=self.reset_timer).pack(side='left', padx=4)

        self.timer_label = tk.Label(
            self.left, text="Timer: 00:00", font=("Helvetica", 11), bg="#F7F7F7"
        )
        self.timer_label.pack(pady=6)

        self.timer_running = False
        self.timer_seconds = 0


    def update_digital_clock(self):
        now = datetime.now()
        self.date_label.config(text=now.strftime("%A, %d %B %Y"))
        self.time_label.config(text=now.strftime("%I:%M:%S %p"))
        self.root.after(1000, self.update_digital_clock)


    def update_analog_clock(self):
        self.canvas.delete("all")

        cx, cy, r = 110, 110, 95
        self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="#2C3E50", width=3)

        for i in range(12):
            ang = math.radians(i * 30)
            x1 = cx + (r - 14) * math.sin(ang)
            y1 = cy - (r - 14) * math.cos(ang)
            x2 = cx + (r - 4) * math.sin(ang)
            y2 = cy - (r - 4) * math.cos(ang)
            self.canvas.create_line(x1, y1, x2, y2, width=3)

        for num, deg in {12:0, 3:90, 6:180, 9:270}.items():
            ang = math.radians(deg)
            tx = cx + (r - 28) * math.sin(ang)
            ty = cy - (r - 28) * math.cos(ang)
            self.canvas.create_text(tx, ty, text=str(num), font=("Helvetica", 12, "bold"))

        now = datetime.now()
        hour = now.hour % 12 + now.minute / 60.0
        minute = now.minute + now.second / 60.0
        second = now.second

        ha = math.radians(hour * 30)
        self.canvas.create_line(cx, cy, cx + 45 * math.sin(ha), cy - 45 * math.cos(ha),
                                width=6, fill="#2C3E50")

        ma = math.radians(minute * 6)
        self.canvas.create_line(cx, cy, cx + 85 * math.sin(ma), cy - 85 * math.cos(ma),
                                width=4, fill="#1F618D")

        sa = math.radians(second * 6)
        self.canvas.create_line(cx, cy, cx + 95 * math.sin(sa), cy - 95 * math.cos(sa),
                                width=2, fill="#E74C3C")

        self.canvas.create_oval(cx-4, cy-4, cx+4, cy+4, fill="#2C3E50")

        self.root.after(1000, self.update_analog_clock)

    def build_middle(self):

        tk.Label(
            self.middle, text="Your Personalized Success Routine",
            font=("Helvetica", 14, "bold"), bg="#F7F7F7"
        ).pack(pady=(4, 6))

        self.table = tk.Text(
            self.middle, height=26, width=68,
            font=("Courier", 11),
            bd=2, relief="ridge"
        )
        self.table.pack()
        self.table.insert("1.0", self.empty_table_text())
        self.table.configure(state='disabled')


    def empty_table_text(self):
        return (
            "+----------------------------------------+--------------+\n"
            "|                ACTIVITY                |   DURATION   |\n"
            "+----------------------------------------+--------------+\n"
            "| Wake-up Time                           |     --       |\n"
            "| Breakfast                              |     --       |\n"
            "| Study Session 1 (Morning)              |     --       |\n"
            "| Refresh Time                           |     --       |\n"
            "| Class Hours                            |     --       |\n"
            "| Lunch                                  |     --       |\n"
            "| Study Session 2 (Evening)              |     --       |\n"
            "| Hobby / Passion Time                   |     --       |\n"
            "| Dinner                                 |     --       |\n"
            "| Sleep                                  |     --       |\n"
            "+----------------------------------------+--------------+\n"
            "| Free Time                              |     --       |\n"
            "| Productivity Score                     |     --       |\n"
            "+----------------------------------------+--------------+"
        )


    def build_right_inputs(self):

        tk.Label(
            self.right,
            text="To begin this journey, let's create a powerful game-changer plan!",
            font=("Helvetica", 11, "italic"),
            wraplength=260, justify="left", bg="#F7F7F7"
        ).pack(pady=(4, 10))

        fields = [
            ("⏰ Wake-up Time (HH:MM)", "06:00"),
            ("📘 Study Hours", "3"),
            ("🏫 Class Hours", "4"),
            ("☕ Break (minutes)", "30"),
            ("😴 Sleep Hours", "8"),
            ("🍽 Total Eating Hours", "2"),
            ("🧘 Refresh Hours", "1"),
            ("❤️ Hobby/Passion Hours", "1")
        ]

        self.entries = {}
        for label, default in fields:
            row = tk.Frame(self.right, bg="#F7F7F7")
            row.pack(fill='x', pady=4)
            tk.Label(row, text=label, width=22, anchor='w', bg="#F7F7F7").pack(side='left')
            ent = tk.Entry(row, width=10)
            ent.insert(0, default)
            ent.pack(side='left')
            self.entries[label] = ent

        row_btn = tk.Frame(self.right, bg="#F7F7F7")
        row_btn.pack(pady=14)
        tk.Button(row_btn, text="Generate Routine", bg="#27AE60", fg="white",
                  width=16, command=self.generate).pack(side='left', padx=4)
        tk.Button(row_btn, text="Clear Table", width=12, command=self.clear_table).pack(side='left')

        tk.Label(self.right, text="Current Month", font=("Helvetica", 11, "bold"), bg="#F7F7F7")\
            .pack(pady=(10, 2))

        self.cal_box = tk.Text(
            self.right, height=8, width=24,
            font=("Courier", 10), bd=1, relief="solid"
        )
        self.cal_box.pack()
        self.update_calendar()



    def update_calendar(self):
        now = datetime.now()
        self.cal_box.configure(state='normal')
        self.cal_box.delete("1.0", "end")
        self.cal_box.insert("1.0", calendar.month(now.year, now.month))
        self.cal_box.configure(state='disabled')

    def convert_to_ampm(self, time_str):
        try:
            t = datetime.strptime(time_str, "%H:%M")
            return t.strftime("%-I:%M %p")
        except:
            return time_str

    def generate(self):

        try:
            wake = self.entries["⏰ Wake-up Time (HH:MM)"].get()
            study = float(self.entries["📘 Study Hours"].get())
            cls = float(self.entries["🏫 Class Hours"].get())
            brk = float(self.entries["☕ Break (minutes)"].get())
            sleep = float(self.entries["😴 Sleep Hours"].get())
            eat_total = float(self.entries["🍽 Total Eating Hours"].get())
            ref = float(self.entries["🧘 Refresh Hours"].get())
            hobby = float(self.entries["❤️ Hobby/Passion Hours"].get())
        except:
            messagebox.showerror("Invalid Input", "Please enter correct numeric values.")
            return

        wake_ampm = self.convert_to_ampm(wake)

        study1 = round(study * 0.55, 2)
        study2 = round(study - study1, 2)

        bfast = round(eat_total * 0.25, 2)
        lunch = round(eat_total * 0.45, 2)
        dinner = round(eat_total - (bfast + lunch), 2)

        break_hours = brk / 60.0

        used = study1 + study2 + break_hours + cls + sleep + eat_total + ref + hobby
        free = round(24 - used, 2)

        productivity = round((study / (study + cls)) * 100, 2) if (study + cls) > 0 else 0

        suggestion = (
            "🔥 Excellent balance! Keep the momentum."
            if productivity >= 70 else
            "🙂 Good routine. Try improving focus slightly."
            if productivity >= 50 else
            "⚠ Consider adjusting your study time slightly."
        )

        table = (
            "+----------------------------------------+--------------+\n"
            "|                ACTIVITY                |   DURATION   |\n"
            "+----------------------------------------+--------------+\n"
            f"| Wake-up Time                           |    {wake_ampm:<10}|\n"
            f"| Breakfast                              |   {bfast:5.2f} hrs  |\n"
            f"| Study Session 1 (Morning)              |   {study1:5.2f} hrs  |\n"
            f"| Refresh Time                           |   {ref:5.2f} hrs  |\n"
            f"| Class Hours                            |   {cls:5.2f} hrs  |\n"
            f"| Lunch                                  |   {lunch:5.2f} hrs  |\n"
            f"| Study Session 2 (Evening)              |   {study2:5.2f} hrs  |\n"
            f"| Hobby / Passion Time                   |   {hobby:5.2f} hrs  |\n"
            f"| Dinner                                 |   {dinner:5.2f} hrs  |\n"
            f"| Sleep                                  |   {sleep:5.2f} hrs  |\n"
            "+----------------------------------------+--------------+\n"
            f"| Free Time                              |   {free:5.2f} hrs  |\n"
            f"| Productivity Score                     |     {productivity:5.2f}%   |\n"
            "+----------------------------------------+--------------+\n\n"
            " SUGGESTION BOX : --\n\n"
            f" {suggestion:<58}  \n\n"
            f"Keep this plan today — small consistent steps create big results.\n"
            
        )

        self.table.configure(state='normal')
        self.table.delete("1.0", "end")
        self.table.insert("1.0", table)
        self.table.configure(state='disabled')


    def clear_table(self):
        self.table.configure(state='normal')
        self.table.delete("1.0", "end")
        self.table.insert("1.0", self.empty_table_text())
        self.table.configure(state='disabled')

    def start_timer(self):
        try:
            mins = int(self.timer_entry.get())
        except:
            messagebox.showerror("Error", "Enter valid minutes.")
            return

        self.timer_seconds = mins * 60
        if not self.timer_running:
            self.timer_running = True
            self.run_timer_tick()

    def run_timer_tick(self):
        if not self.timer_running:
            return

        if self.timer_seconds <= 0:
            self.timer_running = False
            self.timer_label.config(text="Timer: 00:00")
            messagebox.showinfo("Done", "Time's up! Great job.")
            return

        m, s = divmod(self.timer_seconds, 60)
        self.timer_label.config(text=f"Timer: {m:02d}:{s:02d}")
        self.timer_seconds -= 1
        self.root.after(1000, self.run_timer_tick)

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.timer_seconds = 0
        self.timer_label.config(text="Timer: 00:00")

if __name__ == "__main__":
    show_splash_then_main()
    root = tk.Tk()
    app = RoutineApp(root)
    root.mainloop()

