import os
import pandas as pd

from spam_classifier import SpamClassifier


database_path = "./dataset/spam_data.csv"


class EmailBox:
    inbox: list[str] = []
    spam: list[str] = []


class EmailData:
    mail_data: pd.DataFrame

    def __init__(self) -> None:
        database_exists = self.database_exists()
        if not database_exists:
            self.create_database()
        self.mail_data = pd.read_csv(database_path)
        print(self.get_inbox()["text"])

    def database_exists(self) -> bool:
        return os.path.exists(database_path)

    def create_database(self) -> None:
        mail_data = pd.read_csv("./dataset/spam_assassin.csv")

        classifier = SpamClassifier()
        guesses = 0
        spam_guesses = 0
        inbox_guesses = 0

        for mail in mail_data.itertuples():
            index, text, target = mail
            spam_result = classifier.classify_email(text, target)
            mail_data.at[index, "target"] = 1 if spam_result.detected_as_spam else 0

            if spam_result.is_spam:
                spam_guesses += 1
            else:
                inbox_guesses += 1

            if spam_result.is_spam == spam_result.detected_as_spam:
                guesses += 1

        mail_data.to_csv(database_path, index=False)

        print(f"Total guesses: {self.show_percentage(guesses, len(mail_data))}")

        total_spam = mail_data["target"].sum()
        print(f"Spam guesses: {self.show_percentage(spam_guesses, total_spam)}")

        missed_spam = total_spam - spam_guesses
        print(f"Missed spam: {self.show_percentage(missed_spam, total_spam)}")

        total_inbox = len(mail_data) - total_spam
        print(f"Inbox guesses: {self.show_percentage(inbox_guesses, total_inbox)}")

    def show_percentage(self, value: int, total: int) -> str:
        return f"{value}/{total} ({round(100 * value / total, 2)}%)"

    def insert_data(self, text: str, target: int) -> None:
        data = pd.DataFrame({"text": [text], "target": [target]})
        data.to_csv(database_path, mode="a", header=False, index=False)

    def get_inbox(self) -> pd.DataFrame:
        return self.mail_data[self.mail_data["target"] == 0]

    def get_spam(self) -> pd.DataFrame:
        return self.mail_data[self.mail_data["target"] == 1]
