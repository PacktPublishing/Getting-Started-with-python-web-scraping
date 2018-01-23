from bs4 import BeautifulSoup
import csv, requests

url = "https://en.wikipedia.org/wiki/List_of_English_monarchs"
header = {"From": "Packt.com Getting Started with Python Web Scraping"}

# get the HTML from the given website
response = requests.get(url, headers=header)

if response.status_code != 200:
    print("Error:", response.status_code, response.reason)
    exit()

html = response.text

# parse the HTML for the monarch name and reign period
soup = BeautifulSoup(html, "html5lib")
for r in soup.select(".reference"):
    r.replace_with("")

table = []
for a in soup.select(".wikitable td b a")[:-1]:
    name = a.text
    cell = a.find_parent("td")
    contents = cell.text.split("\n")

    try:
        date1 = contents[contents.index("–") - 1]
        date2 = contents[contents.index("–") + 1]
    except:
        date1 = contents[-3].replace("–", "")
        date2 = contents[-2]

    row = [name.strip(), date1.strip(), date2.strip()]
    print(row)
    table.append(row)

# write the data to a CSV file
with open("monarchs.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(table)