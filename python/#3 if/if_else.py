scissor = '가위'
rock = '바위'
paper = '보'

mine = scissor
yours = rock

if mine==yours:
	result = 'draw'
else:
	if yours == scissor:
		if mine == rock:
			result = 'win'
		else:
			result = 'lose'
	else:
		if yours == rock:
			if mine == paper:
				result = 'win'
			else:
				result = 'lose'
		if yours == paper:
			if mine == scissor:
				result = 'win'
			else:
				result = 'lose'
print(mine,':',yours)
print(result)

# elif