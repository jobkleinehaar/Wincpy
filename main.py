# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorrer_player1 = 'Ruud Gullit'
scorrer_player2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorrer_player1 + " " + str(goal_0) + "," + " " + scorrer_player2 + " " + str(goal_1)
print(scorers)

report = f'{scorrer_player1} scored in the {goal_0}nd minute\n{scorrer_player2} scored in the {goal_1}th minute'
print(report)

player = 'Job KleineHaar'
space_position = player.find(" ")
first_name = player[0:space_position]
print(first_name)

last_name = player[space_position+1:]
last_name_len = len(last_name)
print(last_name_len)
print(last_name)

name_short = first_name[0] + '. ' + last_name
print(name_short)

chant = (first_name + '!') + " " + (first_name + '!') + " " + (first_name + '!')
print(chant)

good_chant = (chant != last_name_len)
print(good_chant)