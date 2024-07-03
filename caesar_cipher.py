def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
        
    result = []
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

def frequency_analysis(text):
    frequencies = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            frequencies[char] = frequencies.get(char, 0) + 1
    most_frequent_char = max(frequencies, key=frequencies.get)
    return (ord(most_frequent_char) - ord('e')) % 26

def auto_decrypt(text):
    shift = frequency_analysis(text)
    return caesar_cipher(text, shift, decrypt=True), shift
