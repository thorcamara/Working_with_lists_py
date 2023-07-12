listNumbers = []
greater = 0
smaller = 0
listSize = int(input('How many numbers would you like to have on your list? '))
for c in range(0, listSize):
    listNumbers.append(int(input(f'Type a number for the {c} position: ')))
    if c == 0:
        greater = smaller = listNumbers[0]
    else:
        if listNumbers[c] > greater:
            greater = listNumbers[c]
        if listNumbers[c] < smaller:
            smaller = listNumbers[c]
print('=-' * 30)
print(f'You typed the numbers \033[4;33m{listNumbers}\033[m')
print(f'The \033[4;32mGREATER\033[m number was \033[4;32m{greater}\033[m in the position(s) ', end='')
for i, v in enumerate(listNumbers):
    if v == greater:
        print(f'\033[4;34m{i}\033[m... ', end='')
print()
print(f'The \033[4;31mSMALLER\033[m number was \033[4;31m{smaller}\033[m in the position(s) ', end='')
for i, v in enumerate(listNumbers):
    if v == smaller:
        print(f'\033[4;35m{i}\033[m... ', end='')
print()
