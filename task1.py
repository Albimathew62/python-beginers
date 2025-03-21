#Write a program that counts the number of vowels and consonants in a string?

char1=input("enter the characters:")
vowels=['a','e','i','o','u','A','E','I','O','U']
vowel=0
consonant=0

for i in char1:
    if i in vowels:
        vowel+=1
    else:
        consonant+=1
print("no of vowels:",vowel)
print("no of consonants:",consonant)
