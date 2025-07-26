import tkinter as tk
from tkinter import ttk
import pandas as pd

# List to store failure data

data = []

def calculate_rpn():
    try:
        failure = entry_failure.get()
        severity = int(entry_severity.get())
        occurrence = int(entry_occurrence.get())
        detection = int(entry_detection.get())
        rpn = severity * occurrence * detection

        data.append({
            "Failure Mode": failure,
            "Severity": severity,
            "Occurrence": occurrence,
            "Detection": detection,
            "RPN": rpn
        })

        # Add to table
        table.insert("", "end", values=(failure, severity, occurrence, detection, rpn))

        # Show result
        if rpn > 100:
            result_label.config(text=f"⚠️ High RPN: {rpn}", fg="red")
        else:
            result_label.config(text=f"✅ RPN OK: {rpn}", fg="green")

        # Clear input fields
        entry_failure.delete(0, tk.END)
        entry_severity.delete(0, tk.END)
        entry_occurrence.delete(0, tk.END)
        entry_detection.delete(0, tk.END)

    except ValueError:
        result_label.config(text="❌ Please enter valid numbers!", fg="orange")

def export_to_csv():
    df = pd.DataFrame(data)
    df.to_csv("fmea_data.csv", index=False)
    result_label.config(text="✅ Data saved to fmea_data.csv", fg="blue")

# GUI setup
root = tk.Tk()
root.title("FMEA Tool - Failure Mode and Effects Analysis")

tk.Label(root, text="Failure Mode").grid(row=0, column=0)
entry_failure = tk.Entry(root)
entry_failure.grid(row=0, column=1)

tk.Label(root, text="Severity (1-10)").grid(row=1, column=0)
entry_severity = tk.Entry(root)
entry_severity.grid(row=1, column=1)

tk.Label(root, text="Occurrence (1-10)").grid(row=2, column=0)
entry_occurrence = tk.Entry(root)
entry_occurrence.grid(row=2, column=1)

tk.Label(root, text="Detection (1-10)").grid(row=3, column=0)
entry_detection = tk.Entry(root)
entry_detection.grid(row=3, column=1)

tk.Button(root, text="Calculate RPN", command=calculate_rpn).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Export to CSV", command=export_to_csv).grid(row=5, column=0, columnspan=2)

result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Table to show all entries
cols = ("Failure Mode", "Severity", "Occurrence", "Detection", "RPN")
table = ttk.Treeview(root, columns=cols, show='headings')
for col in cols:
    table.heading(col, text=col)
table.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

heading_label = tk.Label(root, text="FMEA Risk Calculator", font=("Arial", 16, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, pady=10)




root.mainloop()
