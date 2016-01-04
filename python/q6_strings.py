# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count < 10:
      print "Number of donuts: ",count
    else:
      print "Number of dounts: many"
donuts(4)
donuts(10)

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) < 2:
      return ""
    else:
      return s[0:2] + s[len(s)-2:len(s)]

print both_ends('Hello')



def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    slist = list(s)
    i = 0
    first = s[0]
    for x in slist:
      if i > 0:
        if x == first:
          slist[i] = '*'
      i+=1
    return ''.join(slist)
print fix_start('donut')
print fix_start('aardvark')
print fix_start('google')
def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    temp = list(b)
    lista = list(a)
    listb = list(b)
    listb[0],listb[1] = lista[0],lista[1]
    lista[0],lista[1] = temp[0],temp[1]
    return ''.join(lista) + ''.join(listb)
print mix_up('gnash', 'sport')

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) < 3:
      return s
    else:
      if s[len(s)-3:len(s)] == "ing":
        return s+"ly"
      else:
        return s+"ing"

print verbing('swiming')
print verbing('hail')

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    badindx = s.find("bad")
    notindx = s.find("not")
    if notindx < badindx:
      return s[0:notindx] + "good"+ s[badindx+3:]
    else:
      return s
print not_bad('This dinner is not that bad!')
print not_bad("It's bad yet not")


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    alen = len(a)
    blen = len(b)
    if alen % 2 == 0:
      if blen % 2 ==0:
        return a[0:alen/2] + b[0:blen/2] + a[alen/2:alen]+ b[blen/2:blen]
      else:
        return a[0:alen/2] + b[0:((blen-1)/2)+1] + a[alen/2:alen]+ b[((blen-1)/2)+1:blen]
    else:
        if blen % 2 ==0:
          return a[0:((alen-1)/2)+1] + b[0:blen/2] + a[((alen-1)/2)+1:alen] + b[blen/2:blen]
        else:
          return a[0:((alen-1)/2)+1] + b[0:((blen-1)/2)+1] + a[((alen-1)/2)+1:alen] + b[((blen-1)/2)+1:blen]
print front_back('Kitten', 'Donut')
