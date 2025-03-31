class SpamDetector:
    def is_spam(self, text: str) -> bool:
        transformed_text = self.transform(text)
        return self.apply_rules(transformed_text)

    def transform(self, text: str) -> str:
        return text.lower()

    def apply_rules(self, text: str) -> bool:
        return any(
            [
                self.check_for_words(text),
                self.number_of_urls(text) > 5,
            ]
        )

    def check_for_words(self, text: str) -> bool:
        words = [
            "buy",
            "discount",
            "click here",
            "meet singles",
            "money back",
            "winner",
            "prize",
            "limited time",
            "guaranteed",
            "sexually",
            "urgent",
        ]
        return any(word in text for word in words)

    def number_of_urls(self, text: str) -> int:
        return text.count("http") + text.count("www")
