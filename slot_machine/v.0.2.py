import random

print('===  BIENVENIDO A LA TRAGAPERRAS  ===')


coins = ['🪙', '🪙']

# Bucle principal: el juego sigue mientras queden monedas
while len(coins) > 0:
    print(f"\nTus monedas actuales: {len(coins)} -> {''.join(coins)}")
    
    play = input('Escribe "jugar" para tirar (o "salir" para retirarte): ').lower().strip()
    
    if play == 'salir':
        print(f"\nTe retiras del casino con {len(coins)} monedas. ¡Buena jugada!")
        break
        
    if play != 'jugar':
        print(' Entrada no válida. Escribe "jugar" o "salir".')
        continue 


    numero1 = random.randint(0, 5)
    numero2 = random.randint(0, 5)
    numero3 = random.randint(0, 5)

    print("\n Girando rodillos... ")
    print(f"Resultados: [ {numero1} ] [ {numero2} ] [ {numero3} ]")

    if numero1 == numero2 == numero3:
        print(' ¡HAS GANADO EL JACKPOT! Ganas 2 monedas ')
        coins.append('🪙')
        coins.append('🪙')
    else:
        print('HAS PERDIDO. Pierdes 1 moneda ')
        coins.pop()


if len(coins) == 0:
    print("\n💀 ¡Te has quedado sin monedas! GAME OVER 💀")
    print('RECUERDA QUE SIEMPRE PUEDES CAMBIAR 1KG DE COCA¡NA 5 MONEDAS.')
