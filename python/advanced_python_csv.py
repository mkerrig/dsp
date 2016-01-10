import csv

def read_data():
  email = []
  with open('faculty.csv','rb') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
      if index ==0:
        cat = row
        index = 1
      else:
        email.append(row[cat.index(' email')])
  return email

def write_data(list):
  with open('emails.csv','wb') as f:
    write = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    write.writerow(['Email'])
    for email in list:
      write.writerow([email])

write_data(read_data())
