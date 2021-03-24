import sys
import string

def delta_function(substring, letter, string):
	max = 0
	#concatenare dintre substring si litera
	word = substring + letter
	
	#calculare a dimensiunii cea mai mica dintre word si string
	if len(word) > len(string):
		min = len(string)
	else:
		min = len(word)
		
	#calculare stare in care se ajunge
	for i in range(min):
		if word[(len(word)-i-1):(len(word))] == string[0:i+1]:
			max = i + 1
			
	#returnare stare
	return max

if __name__ == "__main__":
	input = open(sys.argv[1])
	#citire string-uri din input
	string1 = input.readline().strip()
	string2 = input.readline().strip()
	output = open(sys.argv[2], "w")
	
	#creare lista cu toate literele A-Z
	alph = list(string.ascii_uppercase)
	
	#creare lista cu substring-urile lui string1
	substrings = [""]
	
	for i in range(1, len(string1)+1):
		substrings.append(string1[0:i])
		
	i = 0
	j = 0
	#initializare matrice delta cu valori de 0
	delta = [[0 for x in range(len(alph))] for y in range(len(substrings))]
	
	#umplere matrice delta
	for s in substrings:
		for l in alph:
			delta[i][j] = delta_function(s, l, string1)
			j = j + 1
		i = i + 1
		j = 0
	
	state = 0
	index = 0
	#parcurgere matrice delta
	for ch in string2:
		state = delta[state][ord(ch)-65]
		if (state == len(string1)):
			#scriere in output a indicilor gasiti
			output.write(str(index - len(string1) + 1) + " ")
		index = index + 1
	
	output.write("\n")
	
	input.close()
	output.close()