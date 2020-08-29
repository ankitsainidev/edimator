## Events to track
1. Cursor Position
2. Text Buffer  -- code at particular time
3. Visual Selection -- highlight



## two approach for saving
on_every_change -- (timestamp)
			1. Cursor Position
			2. Text Buffer  -- code at particular time
			3. Visual Selection -- highlight

on_every_change -- (timestamp)
			what was the change in following
				1. Cursor Position
				2. Text Buffer  -- code at particular time
				3. Visual Selection -- highlight

### NOTE: currently using json, format is .scr.json

## Three parts
recorder  -- validator -- player(will save nothing)



## May implementations to choose from
recorder(web, gui, ncurses) --  

     .scr 

player (web, gui, ncurses)


# rough idea for validator
def is_valid_line(line1, line2):
	a, b, c = line1.split()
	a1, b2, c2 = line2.split()
	if float(a1) < float(a):
		return False
	
def validate(path):
	with open(path) as f:
		lines = f.readlines()
		for i in range(len(lines)):
			if not is_valid_line_sequence(lines[i], lines[i+1]):
				return False
		return True


import text_validator
if text_validator.validate(path):
	print('file is valid')

