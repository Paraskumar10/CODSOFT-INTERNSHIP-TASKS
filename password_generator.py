import random
import array

max_len= int(input("ENTER THE REQUIRED PASSWORD LENGTH..!! "))
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS

ran_digit = random.choice(DIGITS)
ran_upper = random.choice(UPCASE_CHARACTERS)
ran_lower = random.choice(LOCASE_CHARACTERS)

temp_pass = ran_digit + ran_upper + ran_lower

for x in range(max_len - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)

	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
		password = password + x
print("Your Password is...")
print(password)
