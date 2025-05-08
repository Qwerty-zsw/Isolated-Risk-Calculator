import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        capital = float(entry_capital.get())
        risk_percent = float(entry_risk.get())
        stop_percent = float(entry_stop.get())
        leverage = float(entry_leverage.get())

        risk_amount = capital * (risk_percent / 100)
        position_size = risk_amount / (stop_percent / 100)
        leveraged_position_size = position_size / leverage

        result = (
            f"📊 Result\n"
            f"━━━━━━━━━━━━━━━\n"
            f"💰 Total Money: ${capital:.2f}\n"
            f"⚠️ Total Risk: {risk_percent}% → ${risk_amount:.2f}\n"
            f"🛑 Stop Loss {stop_percent}%\n"
            f"⚙️ Leverage: x{leverage}\n"
            f"━━━━━━━━━━━━━━━\n"
            f"✅ NO Leverage: ${position_size:.2f}\n"
            f"🚀 YES Leverage: ${leveraged_position_size:.2f}"
        )
        result_text.config(state="normal")
        result_text.delete("1.0", "end")
        result_text.insert("end", result)
        result_text.config(state="disabled")
    except ValueError:
        result_text.config(state="normal")
        result_text.delete("1.0", "end")
        result_text.insert("end", "❌ Number Please")
        result_text.config(state="disabled")


# ---------- UI Setup ----------
root = tk.Tk()
root.title("🧮 Isolated Risk Calculator")
root.geometry("540x620")
root.configure(bg="#121212")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Tahoma", 11), background="#121212", foreground="#e0e0e0")
style.configure("TButton", font=("Tahoma", 11), background="#4CAF50", foreground="white", padding=8)
style.map("TButton", background=[("active", "#388E3C")])

# ---------- Custom Entry Style ----------
def create_input(master, label_text, icon):
    container = tk.Frame(master, bg="#1e1e1e", bd=1, relief="solid")
    container.pack(pady=8, padx=15, fill="x")

    lbl = tk.Label(container, text=f"{icon} {label_text}", font=("Tahoma", 10), bg="#1e1e1e", fg="#bbbbbb", anchor="w")
    lbl.pack(fill="x", padx=10, pady=(6, 0))

    entry = tk.Entry(container, font=("Tahoma", 12), bg="#2a2a2a", fg="#ffffff", relief="flat", insertbackground="white")
    entry.pack(fill="x", padx=10, pady=(4, 8))
    return entry

# Inp
entry_capital = create_input(root, "Total Money ($)", "💰")
entry_risk = create_input(root, "Total Risk (%)", "📉")
entry_stop = create_input(root, "Stop Loss (%)", "🛑")
entry_leverage = create_input(root, "Leverage", "⚙️")

# Btn
ttk.Button(root, text="🔢 محاسبه کن", command=calculate).pack(pady=20)

# Res
result_frame = tk.Frame(root, bg="#2c2c2c", bd=2, relief="ridge")
result_frame.pack(padx=15, pady=10, fill="both", expand=True)

result_text = tk.Text(result_frame, font=("Tahoma", 11), bg="#2c2c2c", fg="white", wrap="word", state="disabled", bd=0)
result_text.pack(padx=10, pady=10, fill="both", expand=True)

# ---------- Run ----------
root.mainloop()
