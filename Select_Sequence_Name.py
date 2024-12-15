import sys
import os

def read_sequence(sequence_file):

    f = open(sequence_file, "rU")
    text = f.read()
    f.close()
    sequence_dict=dict()

    for line in text.splitlines():
        if(line.strip().startswith(">")):
            name=line.strip().split()[0][1:]
        else:
            sequence=line.strip()
            sequence_dict[name]=sequence

    return sequence_dict

def read_name(name_file):

    f = open(name_file, "rU")
    text = f.read()
    f.close()

    return text.splitlines()

def select_sequence(origin_sequence_file, select_sequence_file, name_file):

    name_list = read_name(name_file)
    sequence_dict = read_sequence(origin_sequence_file)

    f=open(select_sequence_file, "w")

    for name in sequence_dict:
        if(name in name_list):
            f.write(name+"\n")
            f.write(sequence_dict[name]+"\n")

    f.flush()
    f.close()

if __name__=="__main__":

    select_sequence(sys.argv[1], sys.argv[2], sys.argv[3])

