import tkinter as tk
from tkinter import scrolledtext

# Main Window
root = tk.Tk()
root.title("College Helpdesk Chatbot")
root.geometry("500x600")
root.config(bg="#e6f2ff")

# Chat Area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=55, height=25, font=("Arial", 11))
chat_area.pack(pady=10)
chat_area.insert(tk.END, "Bot: Welcome to College Helpdesk Chatbot!\n")
chat_area.config(state='disabled')

# Function for reply
def chatbot_reply(user_text):
    user_text = user_text.lower()

    if user_text == "admission":
        return "Admission forms are available on official website."
    elif user_text == "fees":
        return "Fees can be paid online or in accounts office."
    elif user_text == "exam":
        return "Exams will start next month."
    elif user_text == "library":
        return "Library timing is 9 AM to 5 PM."
    elif user_text == "timings":
        return "College starts at 9 AM."
    else:
        return "Sorry, I don't understand."

# Send Function
def send_message():
    user = entry_box.get()

    if user.strip() == "":
        return

    chat_area.config(state='normal')
    chat_area.insert(tk.END, "You: " + user + "\n")

    reply = chatbot_reply(user)
    chat_area.insert(tk.END, "Bot: " + reply + "\n\n")

    chat_area.config(state='disabled')
    chat_area.yview(tk.END)

    entry_box.delete(0, tk.END)

# Button Click Function
def quick_message(text):
    entry_box.delete(0, tk.END)
    entry_box.insert(0, text)
    send_message()

# Input Box
entry_box = tk.Entry(root, width=35, font=("Arial", 12))
entry_box.pack(pady=5)

# Send Button
send_btn = tk.Button(root, text="Send", width=15, bg="green", fg="white", command=send_message)
send_btn.pack(pady=5)

# Quick Buttons
frame = tk.Frame(root, bg="#e6f2ff")
frame.pack(pady=10)

tk.Button(frame, text="Admission", width=12, command=lambda: quick_message("admission")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Fees", width=12, command=lambda: quick_message("fees")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Exam", width=12, command=lambda: quick_message("exam")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Library", width=12, command=lambda: quick_message("library")).grid(row=1, column=1, padx=5, pady=5)

# Exit Button
tk.Button(root, text="Exit", width=15, bg="red", fg="white", command=root.quit).pack(pady=10)

# Run App
root.mainloop()