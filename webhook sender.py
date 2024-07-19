import tkinter as tk
from tkinter import messagebox
import requests

def send_messages():
    webhook_url = webhook_entry.get()
    message = message_entry.get()
    try:
        num_messages = int(num_messages_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Number of messages must be an integer.")
        return

    if not webhook_url or not message:
        messagebox.showerror("Missing input", "Please provide both the webhook URL and the message.")
        return

    for _ in range(num_messages):
        payload = {
            "content": message
        }
        response = requests.post(webhook_url, json=payload)
        if response.status_code != 204:
            messagebox.showerror("Error", f"Failed to send message: {response.status_code}")
            return

    messagebox.showinfo("Success", f"Successfully sent {num_messages} messages.")

# Create the main application window
root = tk.Tk()
root.title("Discord Webhook Sender")

# Webhook URL input
tk.Label(root, text="Webhook URL:").grid(row=0, column=0, padx=10, pady=10)
webhook_entry = tk.Entry(root, width=50)
webhook_entry.grid(row=0, column=1, padx=10, pady=10)

# Message input
tk.Label(root, text="Message:").grid(row=1, column=0, padx=10, pady=10)
message_entry = tk.Entry(root, width=50)
message_entry.grid(row=1, column=1, padx=10, pady=10)

# Number of messages input
tk.Label(root, text="Number of Messages:").grid(row=2, column=0, padx=10, pady=10)
num_messages_entry = tk.Entry(root, width=50)
num_messages_entry.grid(row=2, column=1, padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send", command=send_messages)
send_button.grid(row=3, columnspan=2, pady=20)

# Run the application
root.mainloop()
