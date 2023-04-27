import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from bs4 import BeautifulSoup

def open_file():
    file_path = filedialog.askopenfilename(initialdir = "/", title = "Select HTML file", filetypes = (("HTML files", "*.html"), ("all files", "*.*")))
    parse_file(file_path)

def parse_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            soup = BeautifulSoup(content, "html.parser")
            classes = set()
            ids = set()

            for tag in soup.find_all():
                class_attr = tag.get("class")
                if class_attr:
                    for class_name in class_attr:
                        classes.add(class_name)
                        
                id_attr = tag.get("id")
                if id_attr:
                    ids.add(id_attr)

            classes = list(classes)
            ids = list(ids)
            classes.sort()
            ids.sort()

            css = ""
            for class_name in classes:
                css += "." + class_name + "{\n\n}\n\n"

            for id_name in ids:
                css += "#" + id_name + "{\n\n}\n\n"

            file_name = file_path.split("/")[-1].split(".")[0] + ".css"
            with open(file_name, "w") as css_file:
                css_file.write(css)
                
            messagebox.showinfo("Information", "CSS file has been created successfully.")
    except:
        messagebox.showerror("Error", "An error occurred while parsing the HTML file.")

root = tk.Tk()
root.title("HTML to CSS Converter")

frame = tk.Frame(root)
frame.pack(pady = 10)

open_file_button = tk.Button(frame, text = "Open HTML file", command = open_file)
open_file_button.pack()

root.mainloop()
