import random
print('TRAGAPERRAS')

numero1 = random.randint(0, 5)
numero2 = random.randint(0, 5)
numero3 = random.randint(0, 5)

play = input('Escribe jugar en minusculas si quieres jugar: ')
 
while play != 'jugar':
    print('Error, escribe jugar en minusculas si queires jugar sino pulsa ctrl + c')
    play = input('Escribe jugar en minusculas si quieres jugar: ')

print(numero1, numero2, numero3)

if numero1 == numero2 == numero3:
    print('¡has ganado!')
else:
    print('HAS PERDIDO :(')