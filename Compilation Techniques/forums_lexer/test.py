with open("test.txt") as file:
    data_line = file.read().splitlines()


def pos(char): 
    line_count = 1
    col_count = 1
    words_per_line = []
    for i in data_line:
        words_per_line.append(i)
    for i in range(0, len(words_per_line)):
        if char in words_per_line[i]:
            line_count += i 
            col_count += words_per_line[i].index(char)
    return line_count, col_count 

print(pos("this")[1])
