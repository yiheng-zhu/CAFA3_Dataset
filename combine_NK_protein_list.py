import sys
import os

def read_name_list(name_file):

    f = open(name_file, "r")
    text = f.read()
    f.close()

    return text.splitlines()

def combine_protein_sequences(inputdir, test_protein_list_file):

    type_list = ["MF", "BP", "CC"]
    test_protein_list = []

    for type in type_list:
        test_protein_list.extend(read_name_list(inputdir + "/" + type.lower() + "o_all_type1.txt"))

    test_protein_list = list(set(test_protein_list))

    f = open(test_protein_list_file, "w")
    for name in test_protein_list:
        f.write(name + "\n")
    f.close()

if __name__=="__main__":

    combine_protein_sequences(sys.argv[1], sys.argv[2])