import sys

def read_name(name_list_file):

    f = open(name_list_file, "r")
    text = f.read()
    f.close()

    return text.splitlines()


def check(file1, file2):

    name_list1 = read_name(file1)
    name_list2 = read_name(file2)

    print(set(name_list1)-set(name_list2))

if __name__ == '__main__':

    check(sys.argv[1], sys.argv[2])