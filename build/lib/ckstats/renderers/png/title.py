from PIL import ImageFont
from ...constants import *

def draw(chart, drawer):
    font = ImageFont.truetype("DejaVuSans", 24)
    text_width,text_height = font.getsize(chart['title'])
 
    left = CHART_WIDTH/2 - text_width/2
    top  = TITLE_HEIGHT/2 - text_height/2
 
    drawer.text((left, top), chart['title'], "#4040a0", font)
