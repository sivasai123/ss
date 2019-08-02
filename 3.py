s=str(input())
if (s=='a' or s=='A' or s=='e' or s=='E' or s=='i' or s=='I' or s=='o' or s=='O' or s=='u' or s=='U'):
    print('Vowel')
elif (s>='a' and s<='z') or (s>='A' and s<='Z'):
    print('Consonant')
else:
    print('invalid')
