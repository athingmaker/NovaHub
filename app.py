import tkinter as tk
from tkinter import scrolledtext
from g4f.client import Client

client = Client()

system_message = {
    "role": "system",
    "content": "Your name is NovaAI, you are developed by NovaHub, your main purpose is to assist the user and you are based off of GPT-4 from OpenAI"
}

messages = [system_message]

def send_message_to_model(user_message):
    try:
        messages.append({"role": "user", "content": user_message})
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )
        if response and hasattr(response, 'choices') and len(response.choices) > 0:
            bot_response = response.choices[0].message.content
            messages.append({"role": "assistant", "content": bot_response})
            return bot_response
        else:
            return "Received an empty or invalid response."
    except Exception as e:
        return f"An error occurred: {e}"

def on_send():
    user_message = user_input.get("1.0", tk.END).strip()
    if user_message:
        chat_display.insert(tk.END, f"You: {user_message}\n")
        user_input.delete("1.0", tk.END)
        bot_message = send_message_to_model(user_message)
        chat_display.insert(tk.END, f"NovaAI: {bot_message}\n")

root = tk.Tk()
root.title("NovaAI Chat")

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="normal", height=20, width=50)
chat_display.pack(padx=10, pady=10)

user_input = tk.Text(root, height=3, width=50)
user_input.pack(padx=10, pady=(0, 10))

send_button = tk.Button(root, text="Send", command=on_send)
send_button.pack(pady=5)

root.mainloop()
