# Language to numerical converter 

# This is a simple conversion of a sentence, a breakdwon of its letter and the creation of a number sequence output.

def convert_to_number_sequence(input_sentence):
    result = []
    for word in input_sentence.split():
        word_sequence = [] # Keep null
        for letter in word:
            if letter.isalpha():
                letter_value = ord(letter.lower()) - 96
                word_sequence.append(str(letter_value))
        result.append(''.join(word_sequence))
    return ' '.join(result)


# Loop to keep asking for input (I like tea and biscuits)
while True:
    user_sentence = input("Please enter a sentence! or type 'exit' to quit: ")

    # Check if the user wants to exit
    if user_sentence.lower() == 'exit':
        break

    number_sequence = convert_to_number_sequence(user_sentence)
    print("Your number sequence:", number_sequence)

# I may add more to this soon