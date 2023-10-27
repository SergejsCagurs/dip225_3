import PyPDF2
import os

data = []

file_invoice = imput()

if not os.path.isfile(dile_invoice):
    print("0")
    exit()

pdf_file = PyPDF2.PdfReader(open(file_invoice, "rb"))
number_of_pages = len(pdf_file.pages)

page1 = pdf_file.pages[0]
page2 = pdf_file.pages[1]

text1 = page1.extract_text()
text2 = page2.extract_text()

pos1 = text1.find("Apmaksai:")
pos2 = text1.find("Elektroenerģijas patēriņš kopā")
summa = text1[pos1+10:pos2].rstrip().replace(",", ".")

pos1 = text2.find("Apjoms Mērv. Cena")
per = text2[pos1-7:pos1].rstrip()

pos1 = text1.find("Elektroenerģijas patēriņš kopā")
pos2 = text1.find("kWh")
consumption = text1[pos1 + 32:pos2].replace(",", ".").replace(",", ".").rstrip()

if consumption == "0":
    print(0)
    exit()

pos1 = text2.find("kWh")
pos2 = text2.find("Apkalpošanas maksa")
price_per_kWh = float(text2[pos1+1:pos2-7].rstrip().replace(",", "."))

per_month, per_year = per.split('.')

with open('noedpool', 'rt') as f:
    next(f)
    for line in f:
        row = line.rstrip().split(",")
        csv_date = row[0].split()[0].split('-')
        csv_month, csv_year = csv_date[1], csv_date[0]

        if csv_month == per_month and csv_year == per_year:
            data.append(float(row[2]))

def average(data):
    price = sum(data) / len(data)
    average_price = round(price, 3)
    return average_price

def overpay(average_price, consumption):
    difference = price_per_kWh - acerage_price
    overpayment = consumption * difference
    return round(overpayment, 1)

avg_price = average(data)
overpayment = overpay(avg_price, float(consumption))
print(overpayment)