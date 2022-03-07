import csv

file = open("pavel.csv")

lasit_csv = csv.reader(file)

saturs = []

for rinda in lasit_csv:
    saturs.append(rinda)

columns = ['Gads', 'Iedzīvotāju skaits']
rows = [
  ['1947', '1 716 773'],
  ['1957', '2 040 978'],
  ['1967', '2 289 645'],
  ['1977', '2 477 449'],
  ['1987', '2 612 068'],
  ['1997', '2 444 912'],
  [2007, '2 208 840'],
  ['2017', '1 950 116']
]

saturs.append(columns)
for row in rows:
    saturs.append(row)

file.close()

with open('new_csvfails.csv', 'w', encoding="utf-8",newline='') as fails:
    csvwrite = csv.writer(fails)
    csvwrite.writerows(saturs)
