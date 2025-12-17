import customtkinter as ctk
from tkinter import END, messagebox

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# ---------------- STARTUP WINDOW ----------------
start = ctk.CTk()
start.geometry("320x260")
start.title("Welcome")

ctk.CTkLabel(
    start,
    text="Welcome",
    font=("Arial", 20, "bold")
).pack(pady=15)

phone_entry = ctk.CTkEntry(
    start,
    placeholder_text="Your phone number",
    width=220
)
phone_entry.pack(pady=8)

contact_entry = ctk.CTkEntry(
    start,
    placeholder_text="Contact name or number",
    width=220
)
contact_entry.pack(pady=8)

def open_chat():
    phone = phone_entry.get().strip()
    contact = contact_entry.get().strip()

    if not phone or not contact:
        messagebox.showwarning("Missing info", "Please fill in all fields")
        return

    start.destroy()
    open_chat_window(phone, contact)

ctk.CTkButton(
    start,
    text="Continue",
    command=open_chat
).pack(pady=20)

# ---------------- MAIN CHAT WINDOW ----------------
def open_chat_window(phone, contact):
    app = ctk.CTk()
    app.geometry("420x700")
    app.title("Chat")

    # -------- TOP BAR --------
    top_bar = ctk.CTkFrame(app, height=60, fg_color="#075E54")
    top_bar.pack(fill="x")

    contact_name = ctk.CTkLabel(
        top_bar,
        text=contact,
        text_color="white",
        font=("Arial", 18, "bold")
    )
    contact_name.pack(side="left", padx=15)

    def simulate_call():
        add_message(f"📞 Calling {contact}…", sender="system")

    call_btn = ctk.CTkButton(
        top_bar,
        text="📞",
        width=40,
        fg_color="#075E54",
        hover_color="#0b7a67",
        command=simulate_call
    )
    call_btn.pack(side="right", padx=15)

    # -------- CHAT AREA --------
    chat_frame = ctk.CTkScrollableFrame(app, fg_color="#ECE5DD")
    chat_frame.pack(fill="both", expand=True)

    def add_message(text, sender="me"):
        if sender == "system":
            label = ctk.CTkLabel(
                chat_frame,
                text=text,
                text_color="gray",
                font=("Arial", 12, "italic")
            )
            label.pack(pady=6)
            return

        bubble_color = "#DCF8C6" if sender == "me" else "#FFFFFF"
        anchor = "e" if sender == "me" else "w"
        pad_x = (80, 10) if sender == "me" else (10, 80)

        bubble = ctk.CTkLabel(
            chat_frame,
            text=text,
            fg_color=bubble_color,
            text_color="black",
            corner_radius=12,
            wraplength=240,
            justify="left"
        )
        bubble.pack(anchor=anchor, padx=pad_x, pady=5)

    # Example message
    add_message("Hey! This looks just like WhatsApp now 😎", sender="other")

    # -------- BOTTOM BAR --------
    bottom_bar = ctk.CTkFrame(app, height=60, fg_color="#F0F0F0")
    bottom_bar.pack(fill="x")

    message_entry = ctk.CTkEntry(
        bottom_bar,
        placeholder_text="Type a message",
        width=300,
        corner_radius=20
    )
    message_entry.pack(side="left", padx=10, pady=10)

    def send_message():
        msg = message_entry.get()
        if msg.strip():
            add_message(msg, sender="me")
            message_entry.delete(0, END)

    send_btn = ctk.CTkButton(
        bottom_bar,
        text="➤",
        width=40,
        corner_radius=20,
        command=send_message
    )
    send_btn.pack(side="right", padx=10)

    app.mainloop()

start.mainloop()
