def get_memo(BMI):
    if BMI <18.8:
        return('體重過輕')
    elif BMI < 22.9:
        return('正常範圍')
    elif BMI < 27:
        return('過   重')
    elif BMI < 30:
        return('輕度肥胖')
    elif BMI < 35:
        return('中度肥胖')
    elif BMI >= 35:
        return('重度肥胖')                    
   
def table():
    with open ('bmi.txt')as f:
        first = f.readline()
        tokens = first.split()
        fmt = '{:10}{:10}{:<10}{:<10}{:<10}{:<10}'
        print(fmt.format(*tokens,'BMI','Memo'))
        print('-'*60)

        for line in f:
            line = line.strip()
            tokens = line.split()
            name,genter = tokens[0],tokens[1]
            h,w = float(tokens[2]),float(tokens[3])
            bmi = round(w / ((h/100)**2),2)
            print(fmt.format(name, genter,h,w,bmi,get_memo(bmi)))
table()            
