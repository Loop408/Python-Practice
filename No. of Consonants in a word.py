#Number of consonants in word
n=input("Enter word: ")
c=0
vowels = ['a', 'e', 'i', 'o', 'u','A', 'E' , 'I','O','U']
for i in n:
    if i not in vowels:
        c += 1
print("Consonants:", c)
