import sys
import csv
# import re 

# def clean_text(text):  # function to clean the text
#     # Remove special characters and split into words
#     cleaned_text = re.sub(r'[^a-zA-Z\s\']', '', text)
#     words = cleaned_text.split()
#     return words


if (len(sys.argv)!=2):
    print("Please provide valid file path ... in the format python3 problem2.py <your file here>")
    sys.exit()

input_file=sys.argv[1]

try:
    with open (input_file) as file:
        text=(file.read())     # read the entire file as a single string

except FileNotFoundError or Exception:
    print(f"File {input_file} does not exist or cannot be opened.")
    sys.exit()


words=(text).split()    # split the string into words
word_count={}

for word in words:        # count the frequency of each word
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1     # add the word to the dictionary

def frequency(word):      # function to sort the dictionary based on the frequency
    return word[1]

sorted_word_count=dict(sorted(word_count.items(), key = frequency,reverse=True ))  # sort the dictionary based on the frequency

output_file = 'problem2Output.csv'

with open(output_file, 'w', newline='') as csvop:
    writerObj = csv.DictWriter(csvop, fieldnames=['word', 'frequency'])   # write the sorted dictionary to a csv file
    writerObj.writeheader()
    for word, frequency in sorted_word_count.items():
        writerObj.writerow({'word': word, 'frequency': frequency})   

print(f"Word frequencies have been written to {output_file}")

top_10_words = list(sorted_word_count.items())[:10]
print(f"Top 10 words are :{top_10_words}")
