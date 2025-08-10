# Solution for Lab 3: Working with Lists

def remove_even_numbers(numbers):
    """Removes even numbers from the list."""
    return [num for num in numbers if num % 2 != 0]

# Solution for Lab 4: String Manipulation

def reverse_words(sentence):
    """Reverses the order of words in a sentence."""
    return ' '.join(sentence.split()[::-1])

# Solution for Lab 5: Dictionary Operations

def count_word_frequencies(text):
    """Counts the frequency of each word in the text (case-insensitive)."""
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
