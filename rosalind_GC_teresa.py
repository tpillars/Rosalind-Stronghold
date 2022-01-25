# python template code for exercise ID GC (Computing GC Content)
# your code *must* define a function called run to work

def run(fasta_str) :
  # calculate the %GC content of each DNA sequence in the fasta records of fasta_str
  # fasta_str is a single string with each line separated by a newline character
  # retain the sequence name and gc content of the sequence with the highest %gc
  # print out the sequence name with the print function on its ownline
  # then print out the %GC of the sequence with the print function on the next line
    percent_current = 0
    percent_largest = 0
    ID_current = ''
    ID_largest = ''
    temp_str = ''
    dic = {}
    fasta_str = fasta_str.strip('\n')
    new_str = fasta_str.split('\n')
    for line in new_str:
       
        if line[0] == ">":
            name = line
            dic[name] = ''
        else:
            dic[name] = line
    for key, value in dic.items():
        ID_current = key
        counter = 0
        for i in value:
            if i == "G" or i == "C":
                counter += 1
        percent_current = (counter/len(value))*100
        if percent_current > percent_largest:
            percent_largest = percent_current
            ID_largest = ID_current
    print(ID_largest[1:],'\n', percent_largest)
