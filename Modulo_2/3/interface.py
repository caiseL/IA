import tkinter as tk 
from tkinter import *
import pandas as pd

mail_data = pd.read_csv("./dataset/spam_assassin.csv")

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spam Detector")
        self.geometry("1280x720")
        self.configure(bg="#f5eef5")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        sidebar = tk.Frame(self, bg="#e0e0e0", width=250)
        sidebar.grid(row=0, column=0, sticky="ns")

        tk.Label(sidebar, text="Bandeja de Correo", font=("Arial", 20), bg="#e0e0e0").pack(pady=18)

        self.inbox_button = tk.Button(sidebar, text="Bandeja de Entrada", font=("Arial", 16), command=self.show_inbox)
        self.inbox_button.pack(pady=10, fill="x")

        self.spam_button = tk.Button(sidebar, text="Bandeja de Spam", font=("Arial", 16), command=self.show_spam)
        self.spam_button.pack(pady=10, fill="x")

        self.new_mail_button = tk.Button(sidebar, text="Nuevo Correo", font=("Arial", 16) , command=self.open_new_mail)
        self.new_mail_button.pack(pady=10, fill="x")

        self.main_frame = tk.Frame(self, bg="#ffffff")
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        self.mail_listbox = tk.Listbox(self.main_frame, font=("Arial", 14), selectmode=SINGLE)
        self.mail_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=self.mail_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.mail_listbox.config(yscrollcommand=scrollbar.set)

    def show_inbox(self):
        self.mail_listbox.delete(0, END)
        inbox_mails = mail_data[mail_data['target'] == 0]['text']
        for mail in inbox_mails:
            self.mail_listbox.insert(END, mail[:100] + "..." if len(mail) > 100 else mail)

    def show_spam(self):
        self.mail_listbox.delete(0, END)
        spam_mails = mail_data[mail_data['target'] == 1]['text']
        for mail in spam_mails:
            self.mail_listbox.insert(END, mail[:100] + "..." if len(mail) > 50 else mail)

    def open_new_mail(self):
        new_mail_window = tk.Toplevel(self)
        new_mail_window.title("Nuevo Correo")
        new_mail_window.geometry("800x600")
        new_mail_window.configure(bg="#f5eef5")
        frame = tk.Frame(new_mail_window, bg="#f5eef5")
        frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Remitente:", font=("Arial", 16), bg="#f5eef5", anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 0))
        self.sender_entry = tk.Text(frame, font=("Arial", 14), height=1, width=60)
        self.sender_entry.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(frame, text="Asunto:", font=("Arial", 16), bg="#f5eef5", anchor="w").grid(row=2, column=0, sticky="w", pady=(10, 0))
        self.new_mail_text = tk.Text(frame, font=("Arial", 14), width=60, height=15)
        self.new_mail_text.grid(row=3, column=0, padx=10, pady=10)

        send_button = tk.Button(frame, text="Enviar", font=("Arial", 14))
        send_button.grid(row=4, column=0, pady=20, sticky="e")




