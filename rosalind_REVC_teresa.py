# python template code for exercise ID REVC (Complementing a Strand of DNA)
# your code *must* define a function called run to work

def run(ss) :
  # compute and print with the print() function the reverse complement of the
  #DNA sequence ss
    revc_dna = ""
    for nt in ss[::-1]:
        if nt == "T":
            revc_dna += "A"
        if nt == "A":
            revc_dna += "T"
        if nt == "C":
            revc_dna += "G"
        if nt == "G":
            revc_dna += "C"
    print(revc_dna)
