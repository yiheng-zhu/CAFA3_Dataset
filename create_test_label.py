import os
import sys

import Find_Parents as fp
import sys
import os

def read_go(go_file):

    go_dict = dict()
    f = open(go_file, "r")
    text = f.read()
    f.close()

    for line in text.splitlines():
        line = line.strip()
        values = line.split()
        if(values[0] not in go_dict):
            go_dict[values[0]] = []
        go_dict[values[0]].append(values[1])

    return go_dict

def create_label_file(go_file, label_file, name_list_file):

    go_dict = read_go(go_file)
    name_list = go_dict.keys()
    obo_dict = fp.get_obo_dict()

    f = open(label_file, "w")
    f1 = open(name_list_file, "w")

    for name in name_list:

        termlist = go_dict[name]
        parentlist = []
        for term in termlist:
            parentlist = parentlist + fp.find_parents(obo_dict, term)

        parentlist = list(set(parentlist))
        if (len(parentlist) > 0):
            line = name + "  "
            parentlist = sorted(parentlist)
            for parent in parentlist:
                line = line + parent + ","
            line = line.strip(",")
            f.write(line + "\n")
            f1.write(name + "\n")

    f.close()
    f1.close()


if __name__=="__main__":

    type_list = ["MF", "BP", "CC"]

    for type in type_list:
        go_file = sys.argv[1] + "/leafonly_" + type + "O.txt"
        label_file = sys.argv[2] + "/" + type + "/test_protein_label"
        name_list_file = sys.argv[2] + "/" + type + "/test_protein_list"
        create_label_file(go_file, label_file, name_list_file)





