##import text
f = open("in.txt")
data = f.read()

##process into data structure
listy = data.rsplit('\n')

#variables for next section
trees = 0
xpos = 0
on = True

##data processing
for x in listy:
	if on == True:
		if x[xpos] == '#':
			trees = trees+1;
		
		xpos = xpos+1

		if xpos > len(x)-1:
			xpos = xpos - len(x)

		on=False
	else:
		on=True

print(trees)

