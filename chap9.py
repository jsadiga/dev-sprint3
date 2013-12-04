# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name:shishira

#Chap 9.1
# fin=open('words.txt')
# for line in fin:
# 	word=line.strip()
# 	if len(word)>20:
# 		print word

# Chap 9.2
# def has_no_e(word):
# 	for char in word:
# 		if char=='e':
# 			return False

# 	return True


# fin=open('words.txt')
# noe=0
# withe=0
# for line in fin:
# 	word=line.strip()
# 	if has_no_e(word):
# 		noe=noe+1
# 		print word
# 	else:
# 		withe=withe+1
# noeper=(100*noe)/(withe+noe)
# print noeper

#Chap 9.3
def avoids(word,noword):
	for char in word:
		if char in noword:
			return False

	return True
		







	


		


				
			







			
	

		
	



				
		

