def fib(n):
  if n ==1 or n==2:
    return 1
  return fib(n-1) + fib(n-2) 

cache =[0,1,1]+ [None for i in range(50)]#important
print(fib(40))

def fibCache(n):
  if cache[n]:
    return cache[n]
  cache[n] = fibCache(n-1) + fibCache(n-2)
  #print(cache)
  return cache[n]
  
print(fibCache(40))     

  