from tkinter import *
from tkinter import messagebox
import psutil

# Function to check processes
def check_process():
    result_box.delete(1.0, END)

    suspicious = [
        "keylogger.exe",
        "logger.exe",
        "spy.exe",
        "hacktool.exe"
    ]

    found = False

    for process in psutil.process_iter():
        try:
            process_name = process.name()

            if process_name.lower() in suspicious:
                found = True

                result_box.insert(
                    END,
                    f"⚠ Suspicious Process Found: {process_name}\n"
                )

                messagebox.showwarning(
                    "Security Alert",
                    f"Suspicious Process Detected!\n\n{process_name}"
                )

        except:
            pass

    if not found:
        result_box.insert(
            END,
            "✓ No Suspicious Process Detected\n"
        )

        messagebox.showinfo(
            "System Status",
            "No Suspicious Process Detected"
        )


# Function to monitor system resources
def monitor_system():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    cpu_label.config(text=f"CPU Usage: {cpu}%")
    ram_label.config(text=f"RAM Usage: {ram}%")


# Function to generate report
def generate_report():
    report = result_box.get(1.0, END)

    with open("system_report.txt", "w") as file:
        file.write("KEYLOGGER DETECTION REPORT\n")
        file.write("==========================\n\n")
        file.write(report)

    messagebox.showinfo(
        "Report",
        "Report Generated Successfully!"
    )


# GUI Window
root = Tk()
root.title("Keylogger Detection & System Monitoring")
root.geometry("700x500")

title = Label(
    root,
    text="KEYLOGGER DETECTION & SYSTEM MONITORING",
    font=("Arial", 14, "bold")
)
title.pack(pady=10)

Button(
    root,
    text="Check Process",
    command=check_process
).pack(pady=5)

Button(
    root,
    text="Monitor System",
    command=monitor_system
).pack(pady=5)

Button(
    root,
    text="Generate Report",
    command=generate_report
).pack(pady=5)

cpu_label = Label(root, text="CPU Usage: ")
cpu_label.pack()

ram_label = Label(root, text="RAM Usage: ")
ram_label.pack()

result_box = Text(root, height=15, width=80)
result_box.pack(pady=10)

root.mainloop()


    