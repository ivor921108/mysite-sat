def read():
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            tokens = line.split()
            print(tokens)
            name = tokens[0]
            num = int(tokens[1])
            single = int(tokens[2])    
            print(name,num*single)
            total += num *single
        print('total:',total)


read()        