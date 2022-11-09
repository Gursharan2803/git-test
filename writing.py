def writefile(hello):
    with open(hello,"w") as f:
        f.write("hello i am gursharan singh ")
        f.write("i love physics")
        f.close()




def readFile(hello):
    with open(hello,"r") as f:
        for line in f:
            if (line):
                print(line)
        f.close()