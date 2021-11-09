a = [1, 2, 3, 4, 5]
b = 'hello world!'


# for i in a:
#   print(i)

for i in b:
    if i != '!':
        print(i)
else:
    print('! не сущ')


food = ['манты', 'борш', 'шоро', 'пирог']
for i in food:
    print('i')
else:
    print('!!!я не ем борщ!!!')

food = ['манты', 'борщ', 'шоро', 'пирог']
food1 = ['манты',  'шоро', 'пирог']
for i in 'food':
    print(i)
for i in food1:
    if i == 'food1':
        print(food1)
else:
    print('!!!классно что нет борща!!!')


food = ['манты', 'борщ']
for i in 'food':
    print(food)
else:
    print('!!!вкусные элементы списка!!!')


food = ['манты', 'борщ', 'шоро']
for i in food:
    print(i)
else:
    print("!!!ужин был шикарным!!!")


fib = [0, 1, 1, 2, 3, 5, 8, 13, 21]

for i in range(len(fib)):
    print(i, fib[i])

fib = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(fib)):
    print(i, fib[1])
ints = [1, 2, 3, 4, 5]
strings = ['1', '2', '3', '4', '5']


for i in range(1, 11):
    print('3' + '*' + str(i) + '=' + str(3 * i))

def summ_ints():
    x = int(input()) + 1
    y = 0
    for i in range(x):
        y = y + i
    print(y)

# obj = {'minsk', 'belarus', 'moskva', 'rossiya', 'kiev', 'ukrain'}
# print(obj['moskva'])
# for i, y in obj:
#   print(i, ' this', obj[i])



if __name__ == '__main__':
   summ_ints()




