
import csv

def read_data():
  degrees = {}
  title = {}
  email = []
  with open('faculty.csv','rb') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
      if index ==0:
        cat = row
      else:
        linedeg = row[cat.index(' degree')].split()
        for deg in linedeg:
          if deg.translate(None, '.') in degrees:
            degrees[deg.translate(None, '.')] += 1
          elif deg != '0':
            degrees[deg.translate(None, '.')] = 1

        if row[cat.index(' title')].replace(" is ", " of ") in title:
          title[row[cat.index(' title')].replace(" is ", " of ")] += 1
        else:
          title[row[cat.index(' title')].replace(" is ", " of ")] = 1
        email.append(row[cat.index(' email')])
      index+=1
    print degrees,'\n'
    print title, '\n'
    print email,'\n'

read_data()
