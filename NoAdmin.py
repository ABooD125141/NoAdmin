from tkinter import PhotoImage
from customtkinter import filedialog  
import customtkinter
import os
from tkinter import *
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.geometry("400x240")
root = customtkinter.CTk()
root.title("NoAdmin")


def generate_vbs_script(selected_program, vbs_filename):
    vbs_script = f'''
Set objShell = CreateObject("WScript.Shell")

objShell.Environment("PROCESS").Item("COMPAT_LAYER") = "RunAsInvoker"

objShell.Run """{selected_program}""", 1, True
'''

    output_filename = f"{vbs_filename}.vbs"
    with open(output_filename, "w") as file:
        file.write(vbs_script)
    print(f"Done{output_filename}")

def select_program(entry):

    # فتح نافذة اختيار الملف
    file_path = filedialog.askopenfilename(title="Select a Program", filetypes=[("ملفات التنفيذ", "*.exe")])

    if file_path:
        selected_program = os.path.abspath(file_path)
        vbs_filename = entry.get()
        generate_vbs_script(selected_program, vbs_filename)

# إعداد واجهة المستخدم

frame_1 = customtkinter.CTkFrame(master=root)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT , text="Enter the VBS File name:")
label1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1,placeholder_text="CTkEntry")
entry_1.pack(pady=10, padx=10)

select_button = customtkinter.CTkButton(master=root, text="CTkButton",fg_color="#00FFB6" ,text_color = "#000000", command=lambda: select_program(entry_1))
select_button.pack(pady=10, padx=10 ,anchor=customtkinter.CENTER)

root.mainloop()
