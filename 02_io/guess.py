import random
def guess():
    x = random.randint(10,20)
    print(x)
    max_guess = 10
    cur_guess =1
    while True :
      if cur_guess >= max_guess:
          print('you lose')
          break
      try:
        num = int(input('please input:'))
        cur_guess +=1
        if num >x:
          print("too large")
        elif num < x:
          print('too small')
        else:
          print('hooray!!!')
          break
      except:
            print('wrong input.....') 
guess()       





    