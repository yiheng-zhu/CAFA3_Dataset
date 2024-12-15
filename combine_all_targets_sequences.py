import os
import sys

def format_sequence(sequence_dir, combine_seqeucne_file):

    f = open(combine_seqeucne_file, "w")

    name_list = os.listdir(sequence_dir)
    for name in name_list:

        f1 = open(sequence_dir + "/" + name, "r")
        text = f1.read()
        f1.close()

        sequence = ""

        for line in text.splitlines():
            line = line.strip()
            if (line.startswith(">")):
                if (len(sequence) > 0):
                    f.write(">" + name + "\n" + sequence + "\n")

                name = line[1:]
                sequence = ""
            else:
                sequence = sequence + line

        if (len(sequence) > 0):
            f.write(">" + name + "\n" + sequence + "\n")

    f.close()

if __name__=="__main__":

    format_sequence(sys.argv[1], sys.argv[2])
