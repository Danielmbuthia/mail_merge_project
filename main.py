# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


letter_start = 'Input/letters/starting_letter.txt'
names = 'Input/Names/invited_names.txt'

with open(names) as name:
    names_list = name.readlines()

for name in names_list:
    formatted_name = name.replace("\'n", "")
    with open(letter_start) as letter:
        letter_data = letter.readlines()
        list_word = ""
        for word in letter_data:
            string_replaced_name = (word.replace('[name]', formatted_name))
            list_word += string_replaced_name
        with open(f'Output/ReadyToSend/invitation_for_{formatted_name}.txt', 'w') as invite_letter:
            invite_letter.write(list_word.strip())
