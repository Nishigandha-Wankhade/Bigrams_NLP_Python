# I will use a Python shell to simulate the UNIX commands and get the most frequent words in the text file. 
# Here's the pipeline:
# 1. Load the text.
# 2. Use 'tr' to replace non-alphabetic characters with newline characters, convert to lowercase, and sort.
# 3. Use 'uniq -c' to count the frequency of each word.

file_path = "C:/Users/wankh/Desktop/CUMBERLAND DOCUMENTS/ZZ_FALL_2024/NLP/WEEK 2/nyt_200811.txt"

# Load the text
with open(file_path, 'r') as file:
    text = file.read()

# Use a simulated pipeline similar to "tr -sc 'A-Za-z' '\n' | tr '[:upper:]' '[:lower:]' | sort | uniq -c"
# We'll tokenize the text, convert it to lowercase, and count word frequencies.
import re
from collections import Counter

# Tokenize, convert to lowercase, and count word frequencies
words = re.findall(r'[a-zA-Z]+', text.lower())
word_count = Counter(words)

# Get the 20 most common words
most_common_words = word_count.most_common(20)
print("\n \t Most Common Words: \n", most_common_words)


#======================================================================================================================================================
# To find bigrams in the text, I will first tokenize the text into words, then create pairs of consecutive words (bigrams), and count the frequency of each bigram.

# from collections import Counter

# Tokenize the text into words
# words = re.findall(r'[a-zA-Z]+', text.lower())

# Create bigrams: pairs of consecutive words
bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]

# Count the frequency of each bigram
bigram_counts = Counter(bigrams)

# Get the 10 most common bigrams
most_common_bigrams = bigram_counts.most_common(10)
print("\n \t Most Comman Bigrams: \n", most_common_bigrams)



#=========================================================================
# Re-importing the required libraries for tokenizing and processing the text
# import re
# from collections import Counter

# Tokenize the text into words
# words = re.findall(r'[a-zA-Z]+', text.lower())

# Create trigrams: sets of three consecutive words
trigrams = [(words[i], words[i+1], words[i+2]) for i in range(len(words)-2)]

# Count the frequency of each trigram
trigram_counts = Counter(trigrams)

# Get the 10 most common trigrams
most_common_trigrams = trigram_counts.most_common(10)
print("\n \t Most Common Tri-grams: \n", most_common_trigrams)
