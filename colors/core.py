# Save the original print function to a different name
import builtins
import re
def overwrite(func):
  """
    A decorator function that can be used to overwrite existing functions.
  """
  def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
  wrapper.__name__ = func.__name__
  return wrapper

class RGBColor:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

colors = {
    'white': RGBColor(255,255,255),
    'black': RGBColor(0,0,0),#gray-ish on vscode's terminal, but ok
    'red': RGBColor(255, 0, 0),
    'green': RGBColor(0, 255, 0),
    'blue': RGBColor(0, 0, 255),
    'brown': RGBColor(139, 69, 19),
    'purple': RGBColor(128, 0, 128),
    'orange': RGBColor(255, 165, 0),
    'pink': RGBColor(255, 192, 203),
    'yellow': RGBColor(255, 255, 0),
    'cyan': RGBColor(0, 255, 255),
    'magenta': RGBColor(255, 0, 255),
    'gold': RGBColor(255, 215, 0),
    'lime': RGBColor(0, 255, 0),
    'teal': RGBColor(0, 128, 128),
    'maroon': RGBColor(128, 0, 0),
    'navy': RGBColor(0, 0, 128),
    'indigo': RGBColor(75, 0, 130),
    'silver': RGBColor(192, 192, 192),
    'violet': RGBColor(238, 130, 238),
    'turquoise': RGBColor(64, 224, 208),
    'orchid': RGBColor(218, 112, 214),
    'aqua': RGBColor(0, 255, 255),
    'olive': RGBColor(128, 128, 0),
    'coral': RGBColor(255, 127, 80),
    'salmon': RGBColor(250, 128, 114),
    'lavender': RGBColor(230, 230, 250),
    'tan': RGBColor(210, 180, 140),
}

def multicolored(color_text_pairs):
    for color_name, text in color_text_pairs:
        rgb_color = colors.get(color_name)
        if rgb_color:
            colored_text = "\033[38;2;{};{};{}m{} \033[39m".format(rgb_color.r, rgb_color.g, rgb_color.b, text)
            builtins.print(colored_text, end="")
        else:
            builtins.print(text, end="")

def colored(color_name, text):
    rgb_color = colors.get(color_name)
    if rgb_color:
        return "\033[38;2;{};{};{}m{} \033[39m".format(rgb_color.r, rgb_color.g, rgb_color.b, text)
    else:
        return text


def apply_color_tags(text):
    color_pattern = re.compile(r'<([a-zA-Z]+)>(.*?)<\/\1>')
    matches = color_pattern.findall(text)
    
    for match in matches:
        tag, content = match
        if tag in colors:
            rgb_color = colors[tag]
            colored_text = "\033[38;2;{};{};{}m{} \033[39m".format(rgb_color.r, rgb_color.g, rgb_color.b, content)
            text = text.replace("<{}>{}</{}>".format(tag, content, tag), colored_text)
    return text

def print(text_with_tags, *args, **kwargs):
    colored_text = apply_color_tags(text_with_tags)
    builtins.print(colored_text, end="",*args, **kwargs)



def neo_print(color: str, text: str, *args, **kwargs):
    builtins.print(colored(color, text), *args, **kwargs)