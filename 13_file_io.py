"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import os

# change directory to find text file
os.chdir(r'C:\Users\Z Dubs\lambda\Intro-Python-I-master\src')

# open text file and loop through printing all lines
with open('foo.txt') as f:
    for line in f:
        print(line, end='')

# added space for readability
print('\n')
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# Create text file (will erase existing file w/ same name) and write 3 lines
with open('bar.txt', 'w') as f2:
    f2.write('A line of arbitrary content\n')
    f2.write('A line that draws you in with interesting information about a subject\n')
    f2.write('Dont let these lines distract you from the fact that in 1998, The Undertaker \
              threw Mankind off Hell In A Cell, and plummeted 16 ft through an announcers table \n')

# open text file and loop through printing all lines
with open('bar.txt') as f2:
    for line in f2:
        print(line, end='')