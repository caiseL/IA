from dataclasses import dataclass

from spam_detector import SpamDetector


@dataclass
class SpamResult:
    is_spam: bool
    detected_as_spam: bool


class SpamClassifier:
    spam_detector: SpamDetector

    def __init__(self):
        self.spam_detector = SpamDetector()

    def show_percentage(self, value: int, total: int) -> str:
        return f"{value}/{total} ({round(100 * value / total, 2)}%)"

    def classify_email(self, email: str, target: int) -> SpamResult:
        is_spam = target == 1
        is_spam_from_detector = self.spam_detector.is_spam(email)
        return SpamResult(is_spam, is_spam_from_detector)
