class Student:
    def __init__(self,name , math, chi, eng , bio):
        self.name = name
        self.math = math
        self.chi = chi
        self.eng = eng
        self.bio = bio
    def info(self):
        return'{:<10}{:<10}{:<10}{:<10}{:<10}'.format(self.name,self.math,self.chi,self.eng,self.bio)
    
def get_math_avg(sts):
    return sum([st.math for st in sts]) / len(sts) 
def get_chi_avg(sts):
    return sum([st.chi for st in sts]) / len(sts)
def get_eng_avg(sts):
    return sum([st.eng for st in sts]) / len(sts)
def get_bio_avg(sts):
    return sum([st.bio for st in sts]) / len(sts) 

def pr_sts(sts):
    for st in sts:
        print(st.info())

def select_math_larger(sts, score):
    chosen = []
    for st in sts:
        if st.math > score:
            chosen.append(st)
    return  chosen      

def pr_sts2(sts):
    for st in sts:
        print(st.info())    

def select_chinese_less(sts, score):
    chosen = []
    for st in sts:
        if st.chi > score:
            chosen.append(st)
    return  chosen      

def pr_sts3(sts):
    for st in sts:
        print(st.info())

def select_biology_higher_avg(sts):
    chosen2 = []
    for st in sts:
        if st.bio > bio_avg:
            chosen2.append(st)
    return  chosen2      

def pr_sts4(sts):
    for st in sts:
        print(st.info())

def select_english_lowest(sts):
    chosen3 = []
    for st in sts:    
        if st.eng < chosen3.eng:              
            chosen3.append(st)
    return chosen3   
def pr_sts5(sts):
    for st in sts:
        print(st.info())

def select_total_highest(sts):  
    chosen4 = []
    for st in sts:
        if st
      

def read_scores():
    with open('students.txt')as f:
        sts =[]
        line = f.readline()
        print(line)
        for line in f:
            ts = line.strip().split()
            #print(ts)
            name = ts[0]
            math = float(ts[1])
            chi = float(ts[2])
            eng = float(ts[3])
            bio = float(ts[4])
            st = Student(name, math, chi, eng, bio)
            sts.append(st)
            print(st.info())
            


    math_avg = get_math_avg(sts)
    chi_avg = get_chi_avg(sts)
    eng_avg = get_eng_avg(sts)
    bio_avg = get_bio_avg(sts)
    fmt ='{:<10}{:<10}{:<10}{:<10}{:<10}'
    print(fmt.format('avg:', math_avg, chi_avg, eng_avg, bio_avg))
    
    print('-'*50)
    lst1 = select_math_larger(sts, 90)
    pr_sts(lst1)

    print('-'*50)
    lst2 = select_chinese_less(sts, 80)
    pr_sts2(lst2)

    print('-'*50)
    lst3 = select_biology_higher_avg(sts)
    pr_sts3(lst3)

    print('-'*50)
    lst4 = select_english_lowest(sts)
    pr_sts4(lst4) 

    print('-'*50)
    lst5 = select_total_highest(sts)
    pr_sts5(lst5)

    
read_scores()            

