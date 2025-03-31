from email_data import EmailData
from interface import Interface


if __name__ == "__main__":
    email_data = EmailData()
    app = Interface(email_data)
    app.mainloop()
