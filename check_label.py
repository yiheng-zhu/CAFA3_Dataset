import sys

def read_label(labelfile):

    f = open(labelfile, "r")
    text = f.read()
    f.close()

    label_dict = dict()
    for line in text.splitlines():
        line = line.strip()
        gene = line.split()[0]
        term_list = line.split()[1].split(",")
        label_dict[gene] = term_list

    return label_dict

def check(file1, file2):

    label_dict1 = read_label(file1)
    label_dict2 = read_label(file2)

    for gene in label_dict1:

        list1 = label_dict1[gene]
        list2 = label_dict2[gene]

        new_list = list(set(list1)-set(list2))
        if(len(new_list)!=0):
            print(gene)


if __name__ == '__main__':

    check(sys.argv[1], sys.argv[2])