import random

print('===  WELCOME TO THE SLOT MACHINE  ===')

coins = ['🪙', '🪙']

# Main loop: the game continues as long as there are coins left
while len(coins) > 0:
    print(f"\nYour current coins: {len(coins)} -> {''.join(coins)}")
    
    play = input('Type "play" to spin (or "exit" to quit): ').lower().strip()
    
    if play == 'exit':
        print(f"\nYou leave the casino with {len(coins)} coins. Good game!")
        break
        
    if play != 'play':
        print(' Invalid input. Please type "play" or "exit".')
        continue 


    numero1 = random.randint(0, 5)
    numero2 = random.randint(0, 5)
    numero3 = random.randint(0, 5)

    print("\n Spinning reels... ")
    print(f"Results: [ {numero1} ] [ {numero2} ] [ {numero3} ]")

    if numero1 == numero2 == numero3:
        print(' YOU WIN THE JACKPOT! You win 2 coins ')
        coins.append('🪙')
        coins.append('🪙')
    else:
        print('YOU LOSE. You lose 1 coin ')
        coins.pop()


if len(coins) == 0:
    print("\n💀 You ran out of coins! GAME OVER 💀")
    print('REMEMBER THAT YOU CAN ALWAYS TRADE 1KG OF COCAINE FOR 5 COINS.')
