import re

##import text
f = open("in.txt")
data = f.read()

##process into data structure
listy = data.rsplit('\n\n')

#variables for next section
out = 0

##data processing
for x in listy:
	print("------")
	working = x.rsplit(' ')
	temp = []
	for y in working:
		temp = temp + y.rsplit('\n')

	
	dic = {
		"byr": "NULLBOIO",
		"iyr": "NULLBOIO",
		"eyr": "NULLBOIO",
		"hgt": "NULLBOIO",
		"hcl": "NULLBOIO",
		"pid": "NULLBOIO",
		"ecl": "NULLBOIO",
		"cid": "blank"
	}

	givePoint = True

	for i in temp:
		pair = i.rsplit(':')
		dic[pair[0]] = pair[1]
	
	for b in dic:
		if dic[b] == "NULLBOIO":
			givePoint = False
			print('1')

	if givePoint:
		##print(temp)
		if len(dic["byr"]) != 4:
			givePoint = False
			print('2')

		if dic["byr"].isnumeric() == False:
			givePoint = False
			print('3')
		else:
			if int(dic["byr"]) > 2002 or int(dic["byr"]) < 1920:
				givePoint = False
				print('4')
			
		if int(dic["eyr"]) > 2030 or int(dic["eyr"]) < 2020:
			givePoint = False
			print('5')

		if int(dic["iyr"]) > 2020 or int(dic["iyr"]) < 2010:
			givePoint = False
			print('13')

		nextPoint = False
		if dic["hgt"][-2] + dic["hgt"][-1] == "in" or dic["hgt"][-2] + dic["hgt"][-1] == "cm":
			nextPoint = True
		if not nextPoint:
			givePoint = False
			print('6')

		if dic["hgt"][-2] + dic["hgt"][-1] == "in":
			coolhgt = dic["hgt"].replace('in', '', 1)
			if coolhgt.isnumeric() == False:
				givePoint = False
				print('7')
			else:
				if int(coolhgt) > 76 or int(coolhgt) < 59:
					givePoint = False
					print('7a')

		if dic["hgt"][-2] + dic["hgt"][-1] == "cm":
			coolhgt = dic["hgt"].replace('cm', '', 1)
			if coolhgt.isnumeric() == False:
				givePoint = False
				print('7')
			else:
				if int(coolhgt) > 193 or int(coolhgt) < 150:
					givePoint = False
					print('7b')

		if dic["hcl"][0] != '#':
			givePoint = False
			print('8')
		
		coolhcl = dic["hcl"].replace('#', '', 1)
		rex = re.findall(r"[0-9a-f]{6}", coolhcl)
		if rex == []:
			givePoint = False
			print('9')

		ecol  = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
		if dic["ecl"] not in ecol:
			givePoint = False
			print('10')

		if dic["pid"].isnumeric() == False:
			givePoint = False
			print('11')

		if len(dic["pid"]) != 9:
			givePoint = False
			print('12')

	if givePoint == True:
		out = out+1
		print("We got em")
		
print(out)

