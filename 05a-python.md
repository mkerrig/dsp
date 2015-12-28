# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

The syntax is pretty similar with the key difference being that tuples use parantheses whereas lists use square brackets. The most major functional difference is that you can't change the entries in a tuple where as you can in a list. Tuples will work in a dictionary because the data in a python dict has to be immutable, whereas a list is mutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets are basically lists without duplicates. Another thing about sets is that all the objects in the set have to be hashable, so sets are also unordered. Because sets are hashed, seeing if an entry exists in a set is considerably faster than in a list, however if you are to iterate through every object in a set vs. a list, the set is slower.


list example:

list = [a,b,1,2,3,3] #intitializing a list

print list[1:5] #prints [b,1,2,3]

print list[0] #prints 0 

set example:

setlist  = [1,2,3,3] #create a list called setlist

set = set(setlist) # make the list a set, the set conatains {1,2,3}

set =  {1,2,3} #how to make a set directly, use curly braces

print set #prints set([1,2,3])



---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Python's lambda is basically Python's version of an inline function. It's used to make an anonymous function to quickly return an expression rather than defining an entire new function. An example of how it could be used in a tuple sort function would be as follows:

getkey = lambda item: item[0]

list = [[3, 12], [7, 61], [6, 22], [28, 87], [1,101]]

sorted(list,key=getkey) #returns [[1,101],[3, 12], [6, 22], [7, 61], [28, 87]]


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

Python list comprehensions are a way to enumerate lists in a way that is much closer to natural human language.
basic example, the two expressions do the same thing:

list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

list = [2**i for i in range(13)]

map equivalence: 

num = [1, 2, 3] 

doublenum = map(lambda x: x * 2, num) #map

doublenum = [x * 2 for x in values] #list comprehension both return [2,4,6]

filter equivalence:

names = ['Aidan', 'Amy', 'Bobby', 'Derrick', 'Cassandra', 'Alex', 'Joe']

a_names = filter(lambda s: s.startswith('A'), names) #filter

a_names = [ name for name in names if name.startswith('A')] #list comprehension both return ['Aidan','Amy','Alex']

They can do the same exact things, and from what I understand time to run is pretty similar

set comprehension, the following two do the same:

set = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096}

set = {2**i for i in range(13)}

dictionary comprehension example, the following two are the same:

dictionary  = {0: 0, 1: 1, 2: 4, 3: 9}

dictionary = {n: n**2 for n in range(4)} 


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





