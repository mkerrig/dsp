import csv
import collections

def question_6():
  faculty = {}
  with open('faculty.csv','rb') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
      if index ==0:
        cat = row
        index = 1
      else:
        linename = row[cat.index('name')].split()
        degree = row[cat.index(' degree')]
        title = row[cat.index(' title')].replace(" is ", " of ")
        email = row[cat.index(' email')]
        templist = [degree,title[0:title.index(" of")],email]
        if linename[-1] in faculty:
          faculty[linename[-1]].append(templist)
        else:
          faculty[linename[-1]] =[]
          faculty[linename[-1]].append(templist)
    print faculty

question_6()

def question_7():
  faculty = {}
  with open('faculty.csv','rb') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
      if index ==0:
        cat = row
        index = 1
      else:
        linename = row[cat.index('name')].split()
        degree = row[cat.index(' degree')]
        title = row[cat.index(' title')].replace(" is ", " of ")
        email = row[cat.index(' email')]
        templist = [degree,title[0:title.index(" of")],email]
        if len(linename[0]) < 3:
          faculty[(linename[1],linename[-1])] = templist
        else:
          faculty[(linename[0],linename[-1])] = templist
    print faculty
question_7()

def question_8():
  faculty = {}
  with open('faculty.csv','rb') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
      if index ==0:
        cat = row
        index = 1
      else:
        linename = row[cat.index('name')].split()
        degree = row[cat.index(' degree')]
        title = row[cat.index(' title')].replace(" is ", " of ")
        email = row[cat.index(' email')]
        templist = [degree,title[0:title.index(" of")],email]
        if len(linename[0]) < 3:
          faculty[(linename[1],linename[-1])] = templist
        else:
          faculty[(linename[0],linename[-1])] = templist
    getkey = lambda item: item[0][1]
    facultynew = collections.OrderedDict(sorted(faculty.items(),key=getkey))
    print facultynew

question_8()
