with open('num.csv', 'w') as file:
    for i in range(2, 256):
        file.write(str(i)+'\t'+str(i)+'\t')
