x = "There are %d types of people." % 10     #give x value
binary = "binary"      #give binary value
do_not = "don't"       # give do_not value
y = "Those who know %s and those who %s." % (binary,do_not) #give y value

print x
print y

print "I said :%r." % x   # print a sentence which include string x
print "I also said: '%s'." % y   #print a sentence which include string y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious   # print a sentence 

w = "This is the left side of ..."
e = "a string with a right side."

print w + e  #print the string w and e in a line
