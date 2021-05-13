import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def search_fname():
    file_path = filedialog.askopenfilename()
    return file_path

def save_fname():
    file_path = filedialog.asksaveasfilename()
    return file_path
