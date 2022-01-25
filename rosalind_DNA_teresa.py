# python template code for exercise ID DNA (Counting DNA Nucleotides)
# your code *must* define a function called run to work

def run(s) :
  # use the print() function to print out counts of A, C, G, and T in s on one
  # line separated by spaces
    dict = {
    "A":0,
    "C":0,
    "G":0,
    "T":0,
    }
    for index,nt in enumerate(s):
        if nt in dict:
            dict[nt] += 1
    nt_count = list(dict.values())
    print(*nt_count)
