numb =5
x = 'ps_%s'%numb + '_%s'%numb
print(x)

matrix_play =[ [i for i in range(numb)] for j in range(3)]
matrix_play2 =[list(x) for x in zip(*matrix_play)]
#matrix_play2 = zip(*matrix_play)
print(matrix_play)
print(matrix_play2)
id = {}
x = open('user list.txt')

for line in x:
    user = line.strip().split(':')
    print(user)
    id[user[0]] = user[1]

print(id)

y = x.readline()
print('file = ', y)