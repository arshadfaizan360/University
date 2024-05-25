def q1(list):
    product = list[0]
    for integer in list[1:]:
        product *= integer
    return product
# print(q1([1,2,3]))

def q2(list):
    condition = True
    current = list[0]
    for element in list[1:]:
        if current > element:
            condition = False
        current = element
    return condition
# print(q2([1,1,2,4,3,3]))

def q3(list1, list2):
    combined_list = []
    for item in list1:
        if item in list2:
            combined_list.append(item)
    return combined_list
# print(q3([1,2,3,4,5],[4,5,6,7,8]))

def q4(list):
    lengths = []
    for item in list:
        lengths.append(len(item))
    return lengths
# print(q4(['fsjlk', 'ads', 'f']))

def q5(list, substring):
    containing = []
    for item in list:
        if substring in item:
            containing.append(item)
    return containing
# print(q5(['asdfa', 'sdafd', 'uoewi'],'a'))

def q6(list):
    current_word = ''
    current_char_count = 0
    for string in list:
        unique_chars = ''
        for char in string:
            if char not in unique_chars:
                unique_chars += char
        if len(unique_chars) > current_char_count:
            current_word = string
            current_char_count = len(unique_chars)
    return current_word
# print(q6(['gfg', 'is', 'best', 'for', 'geeksc']))

def q7(lists):
    current_list = []
    current_char_count = float('inf')
    for list in lists:
        char_count = 0
        for item in list:
            char_count += len(item)
        if char_count < current_char_count:
            current_list = list
            current_char_count = char_count
    return current_list
# print(q7([['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]))

def q8(number):
    number = str(number)
    product = 0
    for digit in number:
        digit = int(digit)
        if digit % 2 != 0:
            if product == 0:
                product = digit
            else:
                product *= digit
    return product
# print(q8(13579))

def q9(n):
    current_divisor = n
    while True:
        current_divisor -= 1
        if n % current_divisor == 0:
            return current_divisor
# print(q9(6500))
        
def q10(string):
    distinct_characters = []
    string = string.lower()
    for char in string:
        if char not in distinct_characters:
            distinct_characters.append(char)
    return distinct_characters
# print(q10('Ignoring case'))

def q11(string, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = string.split()
    matching_words = []
    for word in words:
        consonants = 0
        for letter in word:
            if letter.lower() not in vowels:
                consonants += 1
        if consonants == n:
            matching_words.append(word)
    return matching_words
# print(q11('this is our time', 1))

def q12(words):
    even_length_words = []
    for word in words:
        if len(word) % 2 == 0:
            even_length_words.append(word)
    even_length_words.sort(key=len)
    return even_length_words
# print(q12(['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']))