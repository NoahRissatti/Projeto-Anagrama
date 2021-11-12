count = 0
fra = input('Digite uma palavra:')
fra1 = fra.lower().replace(' ','')
anagrama = input('Digite o anagrama da palavra:')
anagrama1= anagrama.lower().replace(' ','')
if len(fra1) == len(anagrama1):
    for letra in anagrama:
        if letra in fra1:
            count +=1
    if count == len(fra1):
        print('São anagramas')
    else:
        print('Não são anagramas')
else:
    print('Não são anagramas')