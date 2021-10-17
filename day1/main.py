##import text
f = open("in.txt")
data = f.read()

##process into data structure
listy = data.rsplit('\n')
num1 = -1
num2 = -1
num3 = 100000000

for x in listy:
	for y in listy:
		for z in listy:
			if int(x)+int(y)+int(z) == 2020:
				num1=x
				num2=y
				num3=z


print(num1 + ' '  + num2 + ' ' + num3)
print(int(num1)+int(num2)+int(num3))
print(int(num1)*int(num2)*int(num3))

