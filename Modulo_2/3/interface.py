import tkinter as tk
from email_data import EmailData


class Interface(tk.Tk):
    email_data: EmailData

    def __init__(self, email_data: EmailData):
        super().__init__()
        self.title("Spam Detector")
        self.geometry("1280x720")
        self.configure(bg="#f5eef5")

        sidebar = tk.Frame(self, bg="#f2f6fc", width=280)
        sidebar.pack(side="left", fill="y", padx=0, pady=0)

        header_frame = tk.Frame(sidebar, bg="#f2f6fc", height=80)
        header_frame.pack(fill="x", pady=(0, 20), padx=0)

        tk.Label(
            header_frame,
            text="Bandeja de Correo",
            font=("Arial", 18, "bold"),
            bg="#f2f6fc",
            fg="#5f6368",
        ).pack(pady=20, padx=20, anchor="w")

        button_style = {
            "font": ("Arial", 14),
            "bg": "#f2f6fc",
            "fg": "#202124",
            "bd": 0,
            "activebackground": "#e8eaed",
            "activeforeground": "#202124",
            "highlightthickness": 0,
            "anchor": "w",
            "padx": 20,
            "pady": 12,
            "relief": "flat",
        }

        self.inbox_button = tk.Button(
            sidebar, text="Bandeja de Entrada", command=self.show_inbox, **button_style
        )
        self.inbox_button.pack(fill="x", pady=(0, 5))

        self.spam_button = tk.Button(
            sidebar, text="Bandeja de Spam", command=self.show_spam, **button_style
        )
        self.spam_button.pack(fill="x", pady=5)

        self.main_frame = tk.Frame(self, bg="#ffffff")
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.mail_listbox = tk.Listbox(
            self.main_frame,
            font=("Arial", 14),
            selectmode=tk.SINGLE,
            height=26,
            bg="#ffffff",
            highlightthickness=0,
        )
        self.mail_listbox.pack(side="bottom", fill="x")

        self.floating_button = tk.Button(
            self,
            text="Nuevo Correo +",
            font=("Arial", 14, "bold"),
            bg="#1a73e8",
            fg="white",
            bd=0,
            padx=20,
            pady=10,
            command=self.open_new_mail,
        )
        self.floating_button.place(relx=0.95, rely=0.05, anchor="ne")
        self.email_data = email_data
        self.show_inbox()

    def show_inbox(self):
        self.mail_listbox.delete(0, tk.END)
        inbox_mails = self.email_data.get_inbox()["text"]
        for mail in inbox_mails:
            self.insert_email(mail)

    def show_spam(self):
        self.mail_listbox.delete(0, tk.END)
        spam_mails = self.email_data.get_spam()["text"]
        for mail in spam_mails:
            self.insert_email(mail)

    def insert_email(self, mail):
        self.mail_listbox.insert(tk.END, mail[:50])

    def open_new_mail(self):
        new_mail_window = tk.Toplevel(self)
        new_mail_window.title("Nuevo Correo")
        new_mail_window.geometry("970x600")
        new_mail_window.configure(bg="#ffffff")
        new_mail_window.resizable(False, False)

        main_frame = tk.Frame(new_mail_window, bg="#ffffff")
        main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        form_frame = tk.Frame(main_frame, bg="#ffffff")
        form_frame.pack(padx=20, pady=15, fill=tk.BOTH, expand=True)

        tk.Label(
            form_frame, text="De:", font=("Arial", 12), bg="#ffffff", anchor="w"
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.recipient_entry = tk.Entry(form_frame, font=("Arial", 14))
        self.recipient_entry.grid(row=1, column=0, sticky="ew", pady=(0, 15))

        tk.Label(
            form_frame, text="Asunto:", font=("Arial", 12), bg="#ffffff", anchor="w"
        ).grid(row=2, column=0, sticky="w", pady=(0, 5))

        self.subject_entry = tk.Entry(
            form_frame,
            font=("Arial", 14),
            highlightthickness=1,
            highlightcolor="#1a73e8",
            highlightbackground="#dadce0",
        )
        self.subject_entry.grid(row=3, column=0, sticky="ew", pady=(0, 15))

        self.message_text = tk.Text(
            form_frame, font=("Arial", 14), wrap=tk.WORD, padx=5, pady=5, height=15
        )
        self.message_text.grid(row=4, column=0, sticky="nsew", pady=(0, 10))

        button_frame = tk.Frame(form_frame, bg="#ffffff")
        button_frame.grid(row=5, column=0, sticky="se", pady=(10, 0))

        send_button = tk.Button(
            button_frame,
            text="Enviar",
            font=("Arial", 14),
            bg="#1a73e8",
            fg="white",
            bd=0,
            padx=5,
            pady=5,
        )
        send_button.pack(anchor="se")
