import pdfkit
import os

# def convert_html_to_pdf(html_page,save_name):
#     pdfkit.from_url(html_page,save_name)  



#convert_html_to_pdf ('https://www.google.com','timeTable.pdf')


path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_url("file:///S:/Semesters/semester%206/BTP/timetable_maker-master%20Himesh%20Jain/timetable_maker-master/1.html", "Morning_timetable.pdf", configuration=config)



path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_url("file:///S:/Semesters/semester%206/BTP/timetable_maker-master%20Himesh%20Jain/timetable_maker-master/2.html", "Evening_timetable.pdf", configuration=config)