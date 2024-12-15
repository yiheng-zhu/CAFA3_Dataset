import sys

def format_sequence(origin_sequnece_file, format_sequence_file):

    f = open(origin_sequnece_file, "r")
    text = f.read()
    f.close()

    sequence = ""

    f = open(format_sequence_file, "w")

    for line in text.splitlines():
        line = line.strip()
        if(line.startswith(">")):
            if(len(sequence)>0):
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



