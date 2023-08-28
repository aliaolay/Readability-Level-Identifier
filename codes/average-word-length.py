path = ".../clean-txt"
file_name = "..._clean.txt"

with open(path + "/" + file_name, 'r') as file:
    word_length = [len(word) for line in file for word in line.rstrip().split(" ")]
    word_avg = sum(word_length)/len(word_length)
    
print("Average word length: ", word_avg)
