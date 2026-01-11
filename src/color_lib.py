class color:
    @staticmethod
    def rgb_text(r, g, b, text):
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

