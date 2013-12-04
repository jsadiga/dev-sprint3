# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name:shishira

def rotate_word(word,num):
	newword=''
	for char in word:
		n=ord(char)
		newn=n+num
		if newn>122:
			newn=96+(newn-122)
			char1=chr(newn)
			newword=newword+char1
		else:
			char1=chr(newn)
			newword=newword+char1
	return newword

print rotate_word('xyz',1)









