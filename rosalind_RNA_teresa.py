# python template code for exercise ID RNA (Transcribing DNA into RNA)
# your code *must* define a function called run to work

def run(t) :
  # print out the DNA sequence in t replacing all Ts with Us
    str = ""
    for i in t:
        if i == "T":
            str += "U"
        else:
            str += i
    print(str)
