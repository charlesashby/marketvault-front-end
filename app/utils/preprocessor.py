

class TextPreprocessor:

    @staticmethod
    def clean_str(string: str):
        return string.replace("&amp;", "&")
