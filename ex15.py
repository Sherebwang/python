from sys import argv

script, filename = argv    # give two parameter

txt = open(filename)       # open the file and give it to txt

print "Here's your file %r:" % filename
print txt.read()         # read txt and print its content

print "Type the filename again:"
file_again = raw_input(">")     # another way to get the filename

txt_again = open(file_again)

print txt_again.read()

#txt.close()
#txt_again.close()
