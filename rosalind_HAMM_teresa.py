# python template code for exercise ID HAMM (Counting Point Mutations)
# your code *must* define a function called run to work

def run(s,t) :
  # count the number of base positions that do not have the same nucleotide
  # across DNA sequences s and t
  # print out the number of differing positions with the print function
    counter = 0
    for i,j in enumerate(s):
        for l,m in enumerate(t):
            if i==l:
                if j!=m:
                    counter +=1
    print(counter)
