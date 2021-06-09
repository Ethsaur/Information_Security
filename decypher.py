#Inputs: Cypher message, Cypher key
#Outputs: De-cyphered message
#This project should also output a 
#cypher when given a message you want encripted


cypher = 's8tusw3g77t'		  				#what was recieved, no spaces
key = 'bg5yxakielf'					    		#what the key og the cypher is, no spaces
final = ''


trans1 = []								        	#transition lists
trans2 = []
trans3 = []

i = 0									            	#index values

for x in cypher:				      			#read in the values of the cypher and input them as #values in a list
	x = cypher[i]
	if x == 'a':
		trans1.append(0)
	if x == 'b':
		trans1.append(1)
	if x == 'c':
		trans1.append(2)
	if x == 'd':
		trans1.append(3)
	if x =='e':
		trans1.append(4)
	if x == 'f':
		trans1.append(5)
	if x == 'g':
		trans1.append(6)
	if x == 'h':
		trans1.append(7)
	if x == 'i':
		trans1.append(8)
	if x == 'j':
		trans1.append(9)
	if x == 'k':
		trans1.append(10)
	if x == 'l':
		trans1.append(11)
	if x == 'm':
		trans1.append(12)
	if x == 'n':
		trans1.append(13)
	if x == 'o':
		trans1.append(14)
	if x == 'p':
		trans1.append(15)
	if x == 'q':
		trans1.append(16)
	if x == 'r':
		trans1.append(17)
	if x == 's':
		trans1.append(18)
	if x == 't':
		trans1.append(19)
	if x == 'u':
		trans1.append(20)
	if x == 'v':
		trans1.append(21)
	if x == 'w':
		trans1.append(22)
	if x == 'x':
		trans1.append(23)
	if x == 'y':
		trans1.append(24)
	if x == 'z':
		trans1.append(25)
	if x == '0':
		trans1.append(26)
	if x == '1':
		trans1.append(27)
	if x == '2':
		trans1.append(28)
	if x == '3':
		trans1.append(29)
	if x == '4':
		trans1.append(30)
	if x == '5':
		trans1.append(31)
	if x == '6':
		trans1.append(32)
	if x == '7':
		trans1.append(33)
	if x == '8':
		trans1.append(34)
	if x == '9':
		trans1.append(35)
	i += 10		
#end of cypher read in
#print(trans1)

i = 0

for x in key:						        		#read in the key and input them in a list as #values
	x = key[i]
	if x == 'a':
		trans2.append(0)
	if x == 'b':
		trans2.append(1)
	if x == 'c':
		trans2.append(2)
	if x == 'd':
		trans2.append(3)
	if x =='e':
		trans2.append(4)
	if x == 'f':
		trans2.append(5)
	if x == 'g':
		trans2.append(6)
	if x == 'h':
		trans2.append(7)
	if x == 'i':
		trans2.append(8)
	if x == 'j':
		trans2.append(9)
	if x == 'k':
		trans2.append(10)
	if x == 'l':
		trans2.append(11)
	if x == 'm':
		trans2.append(12)
	if x == 'n':
		trans2.append(13)
	if x == 'o':
		trans2.append(14)
	if x == 'p':
		trans2.append(15)
	if x == 'q':
		trans2.append(16)
	if x == 'r':
		trans2.append(17)
	if x == 's':
		trans2.append(18)
	if x == 't':
		trans2.append(19)
	if x == 'u':
		trans2.append(20)
	if x == 'v':
		trans2.append(21)
	if x == 'w':
		trans2.append(22)
	if x == 'x':
		trans2.append(23)
	if x == 'y':
		trans2.append(24)
	if x == 'z':
		trans2.append(25)
	if x == '0':
		trans2.append(26)
	if x == '1':
		trans2.append(27)
	if x == '2':
		trans2.append(28)
	if x == '3':
		trans2.append(29)
	if x == '4':
		trans2.append(30)
	if x == '5':
		trans2.append(31)
	if x == '6':
		trans2.append(32)
	if x == '7':
		trans2.append(33)
	if x == '8':
		trans2.append(34)
	if x == '9':
		trans2.append(35)
	i += 1
#end of key read in
#print(trans2)

i = 0

for x in trans1:					          		#based on the cypher list, subtract the values of cypher list from the key list in new list
	trans3.append(trans2[i] - trans1[i])
	i += 1
#end of list addition
#print(trans3)

i = 0

for x in trans3:					            	#make sure the values are all postive integers		
	if x > 35:							             	#not really needed
		trans3[i] = x - 35
	if x < 0:
		trans3[i] = x + 36
	i += 1
#print(trans3)

for x in trans3:					          		#translate the combined list and read out the actual message as a string
	if x == 0:
		final += str('a')
	if x == 1:
		final += str('b')
	if x == 2:
		final += str('c')
	if x == 3:
		final += str('d')
	if x == 4:
		final += str('e')
	if x == 5:
		final += str('f')
	if x == 6:
		final += str('g')
	if x == 7:
		final += str('h')
	if x == 8:
		final += str('i')
	if x == 9:
		final += str('j')
	if x == 10:
		final += str('k')
	if x == 11:
		final += str('l')
	if x == 12:
		final += str('m')
	if x == 13:
		final += str('n')
	if x == 14:
		final += str('o')
	if x == 15:
		final += str('p')
	if x == 16:
		final += str('q')
	if x == 17:
		final += str('r')
	if x == 18:
		final += str('s')
	if x == 19:
		final += str('t')
	if x == 20:
		final += str('u')
	if x == 21:
		final += str('v')
	if x == 22:
		final += str('w')
	if x == 23:
		final += str('x')
	if x == 24:
		final += str('y')
	if x == 25:
		final += str('z')
	if x == 26:
		final += str('0')
	if x == 27:
		final += str('1')
	if x == 28:
		final += str('2')
	if x == 29:
		final += str('3')
	if x == 30:
		final += str('4')
	if x == 31:
		final += str('5')
	if x == 32:
		final += str('6')
	if x == 33:
		final += str('7')
	if x == 34:
		final += str('8')
	if x == 35:
		final += str('9')
#end of final translation
print(final)
