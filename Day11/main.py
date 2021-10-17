##import text
f = open("in.txt")
data = f.read()

##process into list structure
listy = data.rsplit('\n')

def adj(I, x, y):
	out = 0
	if y > 0:
		if x > 0:
			if I[y-1][x-1] == "#":
				out = out + 1
		if I[y-1][x] == "#":
			out = out + 1
		if x < len(I[0])-1:
			if I[y-1][x+1] == "#":
				out = out + 1
	if x > 0:
		if I[y][x-1] == "#":
			out = out + 1
	if x < len(I[0])-1:
		if I[y][x+1] == "#":
			out = out + 1
	if y < len(I)-1:
		if x > 0:
			if I[y+1][x-1] == "#":
				out = out + 1
		if I[y+1][x] == "#":
			out = out + 1
		if x < len(I[0])-1:
			if I[y+1][x+1] == "#":
				out = out + 1
	return(out)

def run(I):
	out = I
	y = 0
	x = 0
	while y < len(I):
		while x < len(I[y]):
			if I[y][x] != '.':
				friends = adj(I, x, y)
				print(friends)
				if I[y][x] == 'L' and friends == 0:
					out[y][x] = '#'
				if I[y][x] == '#' and friends > 3:
					out[y][x] = 'L'
			x = x +1 
		y = y +1
	
	return(out)

#part 1
def part1(I):
	y = 0
	while y < len(I):
		I[y] = list(I[y])
		y = y + 1

	last = []
	cur = run(I)

	while last != cur:
		for x in cur:
			print(x)

		last = cur
		cur = run(I)

		





#part 2
def part2(I):
	out = 0
	
	for x in I:
		
		out = out+1
	
	return out

ans1 = part1(listy)
ans2 = part2(listy)

print("Answers:")
print(ans1)
print(ans2)

