from datetime import datetime
import tkinter as tk
from tkinter import simpledialog

def add_note_with_window():
    # Окно для ввода данных
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно

    title = simpledialog.askstring("Заголовок", "Введите заголовок заметки:")
    if not title:
        return

    body = simpledialog.askstring("Текст", "Введите текст заметки:")
    if not body:
        return

    created_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "title": title,
        "body": body,
        "created_time": created_time
    }

    # Показываем новую заметку в новом окне
    show_note_window(note)

def show_note_window(note):
    win = tk.Tk()
    win.title("📝 Новая заметка")

    text = tk.Text(win, width=60, height=15, font=("Arial", 12))
    text.pack(padx=10, pady=10)

    text.insert(tk.END, f"Заголовок: {note['title']}\n")
    text.insert(tk.END, f"Дата: {note['created_time']}\n\n")
    text.insert(tk.END, f"{note['body']}\n")
    text.config(state=tk.DISABLED)  # делаем текст только для чтения

    win.mainloop()

if __name__ == "__main__":
    add_note_with_window()
