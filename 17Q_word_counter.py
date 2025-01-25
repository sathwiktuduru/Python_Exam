def word_counter(sentence):
    #In the given sentence each word is separated and count increases if same word repeats
    words = sentence.split()
    word_count = {}
    
    for word in words:
        word = word.lower()  # Convert to lowercase to make the count case-insensitive
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

def main():
    sentence = input("Enter a sentence: ")
    counts = word_counter(sentence)
    for word, count in counts.items():  #In dictionaries 2 items of different or same datatypes can be initialized
        print(f"{word}: {count}")
        
main()