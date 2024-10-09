word=input('Enter word ')
drow=word[::-1]
while True:
    if word==drow:
        print(f'Word {word}  is polydrom')
        break
    else:
        print(f'Word {word}  is not polydrom')
        break
