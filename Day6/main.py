print("------")

##import text
f = open("in.txt")
data = f.read()

##process into data structure
listy = data.rsplit('\n\n')

#variables for next section
out = 0

##data processing
for x in listy:
	pple = x.rsplit('\n')

	yes = []
	no = []
	
	##	for quest in person:
		##	if quest not in yes:
			##	yes.append(quest)

	for ques in pple[0]:
		if ques not in yes:
			yes.append(ques)

	for person in pple:
		for quest in yes:
			if quest not in person:
				no.append(quest)

	for wrong in no:
		if wrong in yes:
			yes.remove(wrong)

	print(yes)
	out = out + len(yes)
		

print(out)

