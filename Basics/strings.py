# Using strings 
#Python strings are inmutable
i_am = 'I\'m'
empty = ''
multiline = '''a
b
c'''
str1 = 'a'
str2 = 'b'
char_1 = 'a'
char_2 = ' '  # space

print(i_am) # I'm
print(len(i_am))    # 3
print(len(empty))   # 0
print(len(multiline))	# 5
print(str1 + str2)	# ab
print(5 * 'a')		# aaaaa
print('b' * 4)		# bbbb
print(ord(char_1))	# 97
print(ord(char_2))	# 32
print(chr(97))		# a
print(chr(945))		# alpha symbol

the_string = 'silly walks'
for character in the_string:
    print(character, end=' ')	# s i l l y   w a l k s 

alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)	# True
print("F" in alphabet)	# False
print(min("aAbByYzZ"))	# A
print(max("aAbByYzZ"))	# z
print("aAbByYzZaA".index("b"))	# 2
print(list("abcabc"))	# ['a', 'b', 'c', 'a', 'b', 'c']
print("abcabc".count("b"))	# 2
print('aBcD'.capitalize())	# Abcd
print('[' + 'alpha'.center(20) + ']')	# [       alpha        ]
print("epsilon".endswith("on"))	# True
print("Eta".find("ta"))		# 1
print("Eta".find("mma"))	# -1
print('lambda30'.isalnum())		# True
print('lambda'.isalnum())		# True
print('30'.isalnum())			# True
print('@'.isalnum())			# False
print('lambda_30'.isalnum())	# False
print(''.isalnum())				# False
print("Moooo".isalpha())	# True
print('Mu40'.isalpha())		# False
print('2018'.isdigit())		# True
print("Year2019".isdigit())	# False
print("Moooo".islower())	# False
print('moooo'.islower())	# True
print(' \n '.isspace())		# True
print(" ".isspace())		# True
print("mooo mooo mooo".isspace())	# False
print("Moooo".isupper())	# False
print('moooo'.isupper())	# False
print('MOOOO'.isupper())	# True
print("*".join(["omicron", "pi", "rho"]))	# omicron*pi*rho
print("SiGmA=60".lower())	# sigma=60
print("www.cisco.com".lstrip("w"))	# .cisco.com
print("pythoninstitute.org".lstrip("py"))	# thoninstitute.org
print("pythoninstitute.org".lstrip("org"))	# pythoninstitute.org
print("This is it!".replace("is", "are"))	# Thare are it!
print("tau tau tau".rfind("ta"))    # 8
print("tau tau tau".rfind("ta", 9))		# -1
print("tau tau tau".rfind("ta", 3, 9))	# 4
print("cisco.com".rstrip(".com"))		# cis
print("[" + " upsilon ".rstrip() + "]")	# [ upsilon]
print("phi       chi\npsi".split())		# ['phi', 'chi', 'psi']
print("omega".startswith("meg"))	# False
print("omega".startswith("om"))		# True
print("[" + "   aleph   ".strip() + "]")	# [aleph]
print("I know that I know nothing.".swapcase())		# i KNOW THAT i KNOW NOTHING.
print("I know that I know nothing. Part 1.".title())	# I Know That I Know Nothing. Part 1.
print('alpha' == 'alpha')	# True
print('alpha' != 'Alpha')	# True
print('alpha' < 'alphabet')	# True

first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)	# ['alpha', 'gamma', 'omega', 'pi']
first_greek_2 = first_greek.sort()	# ['alpha', 'gamma', 'omega', 'pi']