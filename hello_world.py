# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Yousef"
print( "Hello", name )	# with a comma
print( "Hello " + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 37
print( "Hello",name )	# with a comma
print( "Hello"  + f" {name}")
print("Hello "+str(name)) 	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} and {} .".format(fave_food1,fave_food2) ) # with .format()
print( f"I Love to eat {fave_food1} and {fave_food2}." ) # with an f string

fave_quote ="imagination is more important than knowledge"
print(fave_quote.capitalize())
print(fave_quote.upper())
print(fave_quote.center(90))
print(fave_quote.title())
