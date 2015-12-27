# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

ls - list the contents of a directory
cd "FILENAME HERE" - change directory to the designated file location
clear - clear the screen
ssh - "IP-ADDRESS" ssh into a remote computer
man - "COMMAND NAME HERE" gives the manual on a given  command
cp - "FILENAME DESTINATION" - copy files
mv - "FILENAME DESTINATION" - moves files
mkdir - "DIRECTORYNAME" - makes a directory
rmdir - "DIRECTORYNAME" - remove a directory
rm - "FILENAME" -removes files
---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

list contents of a directory, ls -a , doesn't ignore files starting with . , ls -lh is a human readable file size, you can use both to not ignore files starting with . and make it a human readable file size as well so ls -a -lh, and ls -l makes it a long listing style instead of block, so you could do all three to get the ., size, and long listing format, any combination would be meaningful

---


---

What does `xargs` do? Give an example of how to use it.

It splits up a string through spaces or newlines to execute the substrings as individual arguments, this can be useful because it gives you more flow control and can make long lists of arguments easy to execute. By default it just prints out whatever you input back to the command line. So for example suppose you had 4 files: prog1.py prog1.pyc prog2.py prog2.pyc
and you wanted to delete just the files with the ".py" extension, a way to do this would be this:
find . -name "*.py" | xargs rm -rf

so find would return a list of files with the ".py" extension, then this command pipelines the response into xargs which then removes the files one by one, sort of like a for loop in python where one is iterating through a list.

---

