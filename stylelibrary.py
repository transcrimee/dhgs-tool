class color:
    @staticmethod
    def rgb_text(r, g, b, text):
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m" # RGB for example: 255, 255, 255
class style: # This is being used to wrap up all the functions under one like style.bold_style or etc
    @staticmethod
    def bold_style(text):
      return f"\033[1m{text}\033[0m" # To be honest i didn't know what this was until now so I learned I guess something text styles (SGR Parameters)
    def italic_style(text):
      return f"\033[3m{text}\033[0m"
    def bold_italic_style(text):
       return f"\033[1;3m{text}\033[0m"
    def dim_style(text):
       return f"\033[2m{text}\033[0m"
    def underline_style(text):
       return f"\033[4m{text}\033[0m"
    def blinking_style(text):
       return f"\033[5m{text}\033[0m"
    def invert_style(text):
       return f"\033[7m{text}\033[0m"
    def strikethrough_style(text):
       return f"\033[9m{text}\033[0m"
# ------------ testing down here -----------------        
print(color.rgb_text(100, 255, 100, "This is custom green text"))
print(style.bold_style( "This is custom bold text"))
print(style.italic_style( "This is custom bold text"))
print(style.bold_italic_style( "This is custom bold text"))
print("------- now for less important ones -------")
print(style.dim_style( "This is custom bold text"))
print(style.underline_style( "This is custom bold text"))
print(style.blinking_style( "This is custom bold text"))
print(style.invert_style( "This is custom bold text"))
print(style.strikethrough_style( "This is custom bold text"))
# ------------- testing up here ------------------  