from bs4 import BeautifulSoup
import re

html = '''
<p id="foo1"></p>
<p id="foo2"></p>
'''

# comparing parsers
soup = BeautifulSoup(html, "html.parser")
print(soup)

soup = BeautifulSoup(html, "html5lib")
print(soup)



html = '''
<div id="foo1" class="buzz">Hello</div>
<div id="foo2">World<div>Test<p class="buzz"></p></div></div>
<div id="bar1">Example<div>Test</div></div>

<table name="fizz" class="buzz">
  <tr>
    <th>Letters</th>
    <th>Numbers</th>
  </tr>
  <tr>
    <td>A</td>
    <td>1</td>
  </tr>
  <tr>
    <td>B</td>
    <td>2</td>
  </tr>
  <tr>
    <td>C</td>
    <td>3</td>
  </tr>
</table>
'''

soup = BeautifulSoup(html, "html5lib")

# comparing find_all with select
print(soup.find_all("div"))
print(soup.select("div"))

print(soup.find_all(["th", "td"]))
print(soup.select("th, td"))

print(soup.find_all(class_="buzz"))
print(soup.select(".buzz"))

print(soup.find_all(id=re.compile("^foo")))
print(soup.select("[id^=foo]"))


# looking at some object properties
p = soup.select_one("[id^=foo]")

print(p.find_next_sibling())
print(p.find_next_sibling("table"))

print(p.parent)
print(p.parent.parent)

print(p.attrs)
print(p.get("id"))
p["name"] = "bar"
print(p)


# two equivalent, yet very different pieces of code
matches = []
divs = soup.find("body").find_all("div", recursive=False)
for div in divs:
    if div.get("id").startswith("foo"):
        for c in list(div.children):
            try:
                buzzes = c.find(class_="buzz")
                matches.append(buzzes)
            except:
                pass

print(matches)

matches = soup.select("body > div[id^=foo] .buzz")
print(matches)
