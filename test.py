import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        task_listBox.selection_clear(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)
        task_entry.delete(0, tk.END)
        task_listBox.selection_clear(0, tk.END)

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="DarkOrange")
        task_entry.delete(0, tk.END)
        task_listBox.selection_clear(0, tk.END)

def on_closing():
    # Проверка наличия невыполненных задач
    all_tasks = task_listBox.get(0, tk.END)
    completed_tasks = [task_listBox.itemcget(i, 'bg') == "DarkOrange" for i in range(task_listBox.size())]
    if any(not completed for completed in completed_tasks):
        messagebox.showwarning("Предупреждение", "Вы не можете закрыть программу, пока все задачи не будут выполнены.")
    else:
        root.destroy()

root = tk.Tk()
root.title("Лист задач")
root.configure(background="CadetBlue1")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="CadetBlue1")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=36, bg="CadetBlue3")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, width=30, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, width=30, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, width=30, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач:", bg="CadetBlue1")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, bg="CadetBlue")
task_listBox.pack(pady=10)

text1 = tk.Label(root, text="© Alex Yordan, 2024", bg="CadetBlue1")
text1.pack(pady=5)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()