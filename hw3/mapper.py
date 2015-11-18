fileA = sc.textFile("input1/join1_FileA.txt")

fileA.collect()

fileB = sc.textFile("input1/join1_FileB.txt")

fileB.collect()

def split_fileA(line):
    # split the input line in word and count on the comma
    s = line.split(",")
    word = s[0]
    count = s[1]
    # turn the count to an integer
    count = int(count)  
    return (word, count)

test_line = "able,991"

split_fileA(test_line)

fileA_data = fileA.map(split_fileA)
fileA_data.collect()

def split_fileB(line):
    # split the input line into word, date and count_string
    s = line.split(",")
    count_string = s[1]
    ss = s[0].split(" ")
    word = ss[1]
    date = ss[0]
    return (word, date + " " + count_string) 

fileB_data = fileB.map(split_fileB)
fileB_data.collect()

fileB_joined_fileA = fileB_data.join(fileA_data)
fileB_joined_fileA.collect()

(u'actor', (u'Feb-22 3', 22))
