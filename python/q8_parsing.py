#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

def read_data(data):
  teams = {}
  with open(data,'rb') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
      if index ==0:
        cat = row
      else:
        teams[row[cat.index('Team')]] = int(row[cat.index('Goals')])-int(row[cat.index('Goals Allowed')])
      index+=1
  return teams



def get_min_score_difference(teams):
  minName = 'Default'
  minNum = 100
  for key,value in teams.iteritems():
    if abs(value) < minNum:
      minNum = abs(value)
      minName = key
  print 'The team with the smallest number is: ',minName,' with ',minNum



get_min_score_difference(read_data('football.csv'))
