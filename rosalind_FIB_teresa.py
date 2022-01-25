# python template code for exercise ID FIB (Rabbits and Recurrence Relations)
# your code *must* define a function called run to work

def run(n,k) :
  # print out the number of rabbit pairs that exist after n months if each
  # pair of living rabbits producs a litter of k rabbit pairs
    fn1 = 1
    fn2 = 1
    fn = 1  
    for rabbit in range(2, n):
        fn = fn1 + fn2*k
        fn2 = fn1
        fn1 = fn
    print(fn)
