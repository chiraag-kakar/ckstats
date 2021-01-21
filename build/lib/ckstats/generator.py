from PIL import Image, ImageDraw
from reportlab.pdfgen.canvas import Canvas
 
from .constants import *
from .renderers import renderers
 
def generate_chart(chart, filename):
 
    # Select the output format.
 
    if filename.lower().endswith(".pdf"):
        format = "pdf"
    elif filename.lower().endswith(".png"):
        format = "png"
    else:
        print("Unsupported file format: " + filename)
        return
 
    # Prepare the output file based on the file format.
 
    if format == "pdf":
        output = Canvas(filename)
    elif format == "png":
        image  = Image.new("RGB", (CHART_WIDTH, CHART_HEIGHT),
                           "#ffffff")
        output = ImageDraw.Draw(image)
 
    # Draw the various chart elements.
 
    renderers.draw(format, "title",  chart, output)
    renderers.draw(format, "x_axis", chart, output)
    renderers.draw(format, "y_axis", chart, output)
    if chart['series_type'] == "bar":
        renderers.draw(format, "bar_series", chart, output)
    elif chart['series_type'] == "line":
        renderers.draw(format, "line_series", chart, output)
 
    # Finally, save the output to disk.
 
    if format == "pdf":
        output.showPage()
        output.save()
    elif format == "png":
        image.save(filename, format="png")
