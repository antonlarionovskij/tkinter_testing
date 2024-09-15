import tkinter as Tk
from tkinter import *
from tkinter import ttk
from datetime import datetime

# Версия tkinter
print(Tcl().eval("info patchlevel"))

# Функции
def finish():
    root.destroy() # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

# Создание окна
root = Tk() # окно root

# Размеры и смещения
root.geometry("300x250+400+250") # размеры окна "Ширина х Высота" и его смещение "+ координата X вправо + координата Y вниз", если не указывать, будет небольшое смещение и размеры будут соответственно содержанию
#root.resizable(False, False) # запрет на изменение размера (первый параметр -ширина, второй - высота)
# root.minsize(200, 150) # минимально возможные размеры окна
# root.maxsize(400, 300) # максимально возможные размеры окна

# Иконки
root.iconbitmap(default=r'C:\Users\A.N.Larionovskii\PycharmProjects\django_site\venv\Lib\site-packages\rest_framework\static\rest_framework\docs\img\grid.png') # иконка перед заголовком, прописывается путь к ней. Если не указано - будет иконка пера
# icon = PhotoImage(file=r'C:\Users\A.N.Larionovskii\PycharmProjects\django_site\venv\Lib\site-packages\rest_framework\static\rest_framework\docs\img\grid.png')
# root.iconphoto(False, icon)

# Атрибуты окна
#root.attributes("-fullscreen", True) # полноэкранный режим, закрытие - Alt+F4
#root.attributes("-alpha", 0.5) # окно будет полупрозрачным
#root.attributes("-toolwindow", True) # отключение верхней панели окна за исключением заголовка и крестика закрытия

# Текст
root.title("Заголовок окна") # если не указывать - заголовок будет 'tk'
label = Label(text="Hello, World!") # текстовая метка
label.pack() # размещение мерки в окне
Label(text=f'Версия tkinter: {Tcl().eval("info patchlevel")}').pack()

# Отчеты
root.update_idletasks()
print(root.geometry()) # Выведет размеры и смещения окна

# Перехват событий
root.protocol("WM_DELETE_WINDOW", finish) # При событии закрытия окна вызывается функция finish, которая закрывает окно и приложение и выводит на консоль текст

# Виджеты
# btn = Button(text="Клик") # Кнопка из пакета tkinter
# btn_ttk = ttk.Button(text="Клик") # Кнопка из пакета ttk
# btn.pack() # Размещаем кнопку btn в окне
# btn_ttk.pack() # Размещаем кнопку btn_ttk в окне

# Параметры виджета
# btn = Button()
# btn.pack()
# btn["text"] = "Send" # устанавливаем параметр text
# btn_text = btn["text"] # получаем значение параметра text
# print(btn_text)
# btn_ttk = ttk.Button()
# btn_ttk.pack()
# btn_ttk.config(text="Send mail") # устанавливаем параметр text через метод config

# Получение информации о виджете
# def print_info(widget, depth=0): # получение информации о всех виджетах в окне
#     widget_class = widget.winfo_class()
#     widget_width = widget.winfo_width()
#     widget_height = widget.winfo_height()
#     widget_x = widget.winfo_x()
#     widget_y = widget.winfo_y()
#     print(" "*depth + f"class = {widget_class}, width = {widget_width}, height = {widget_height}, x = {widget_x}, y = {widget_y}")
#     for child in widget.winfo_children():
#         print_info(child, depth+1)
#
# root.update() # обновляем информацию о виджетах
# print_info(root)

# Кнопки
btn = ttk.Button(text="Button", command=lambda: Label(text=f'Сейчас: {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}').pack())
btn.pack()

root.mainloop() # показ окна