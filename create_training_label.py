import os
import sys
import Find_Parents as fp

def read_go(go_file):

    f = open(go_file, "r")
    text = f.read()
    f.close()

    go_dict = dict()

    type_list = ["MF", "BP", "CC"]
    for type in type_list:
        go_dict[type[1]] = dict()

    for line in text.splitlines():
        line = line.strip()
        values = line.split()
        if(values[0] not in go_dict[values[2]]):
            go_dict[values[2]][values[0]] = []
        go_dict[values[2]][values[0]].append(values[1])

    return go_dict

def create_label(origin_label_file, outputdir):

    go_dict = read_go(origin_label_file)
    type_list = ["MF", "BP", "CC"]
    obo_dict = fp.get_obo_dict()

    for type in type_list:
        label_file = outputdir + "/train_label_" + type
        f = open(label_file, "w")

        for name in go_dict[type[1]]:

            termlist = go_dict[type[1]][name]
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
        f.close()

if __name__=="__main__":

    create_label(sys.argv[1], sys.argv[2])


