class WeekRecord:
    name  = 'unknown'
    work_hours = 0
    wage = 0
    def __init__(self , name):
        self.name = name
        self.work_hours =[0 for i in range(7)]
    def WorkHour(self, day, hour):
        self.work_hours[day] = hour  
    def setWage(self, wage):
        self.wage = wage      
    def weekWage(self):
        total_hours = sum(self.work_hours)
        return self.wage * total_hours

def read_file():
    with open('week.txt') as f:
        first = f.readline()
        for line in f:
            line = line.strip()
            ts = line.split()
            wr = WeekRecord(ts[0])
            for i in range(1,7):
                wr.WorkHour(i,float(ts[i]))
            wr.setWage(float(ts[-1]))    
            print(wr.name , wr.weekWage())    

            
read_file()

