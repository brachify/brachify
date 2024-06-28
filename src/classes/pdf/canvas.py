from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

from datetime import datetime

class FooterCanvas(canvas.Canvas):
    """
    A custom canvas is needed to generate the date and page number at the bottom of the pdf.
    https://www.blog.pythonlibrary.org/2013/08/12/reportlab-how-to-add-page-numbers/
    """

    def __init__(self, *args, **kwargs):
        """Constructor"""
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        """
        On a page break, add information to the list
        """
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """
        Add the page number to each page (page x of y)
        """
        page_count = len(self.pages)
        date_time = self.get_current_date_time()
        
        for page in self.pages:
            self.__dict__.update(page)
            self.setFillColor(colors.grey)
            self.draw_page_number(page_count)
            self.draw_export_date(date_time)
            canvas.Canvas.showPage(self)
            
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        """
        Add the page number
        """
        page = "Page %s of %s" % (self._pageNumber, page_count)
        self.setFont("Helvetica", 9)
        self.drawRightString(7.5*inch, 0.5*inch, page) # (x_location, y_location_from_bottom, string)

    def draw_export_date(self, date_time):
        """
        Add the pdf export date
        """
        text = f"PDF produced on {date_time}"
        self.setFont("Helvetica", 9)
        self.drawString(1*inch, 0.5*inch, text) # (x_location, y_location_from_bottom, string)

    def get_current_date_time(self):
        """
        Get the current date and time and return with desired formatting as a string.
        """
        # datetime object containing current date and time
        now = datetime.now()
        
        # Month dd, YYYY H:M:S (with month's fullname and 24-hour clock)
        dt_string = now.strftime("%B %d, %Y %H:%M:%S")
        return dt_string
