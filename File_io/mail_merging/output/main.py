PLACE_HOLDER = "[name]"

with open("../input/Names/name.txt") as names:
    names = names.readlines()

with open("../input/Letters/starting_letter.txt") as letters:
    file_letters = letters.read()
    for send_to_name in names:
        stripped_name = send_to_name.strip()
        new_letter = file_letters.replace(PLACE_HOLDER, stripped_name)
        with open(f"./ready_to_send/to_{stripped_name}.txt", mode="w") as new_files_to_send:
            new_files_to_send.write(new_letter)
