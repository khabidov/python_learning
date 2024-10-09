player1=input('enter action 1st player: ')
player2=input('enter action 2nd player: ')

if player1=='Scissors' and player2=='Paper':
    print('player1 won')
elif player1=='Rock' and player2=='Scissors':
    print('player1 won')
elif player1 == 'Paper' and player2 == 'Rock':
    print('player1 won')
elif player2 == 'Scissors' and player1 == 'Paper':
    print('player2 won')
elif player2 == 'Rock' and player1 == 'Scissors':
    print('player2  won')
elif player2 == 'Paper' and player1 == 'Rock':
    print('player2 won')
else:
    print("it's a draw!")
