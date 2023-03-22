def text_to_binary(text):
  binary_string = ""
  
  for character in text:
    binary_char = bin(ord(character))[2:]
    binary_char = binary_char.zfill(8)
    binary_string += binary_char + " "

  return binary_string[:-1]

def binary_to_text(binary_string):
  binary_characters = binary_string.split(' ')

  text = ""
  
  for binary_value in binary_characters:
    text += chr(int(binary_value, 2))

  return text

def text_to_binary_unit_test():
  # Setup
  initial_text = "abcdefghijklmnopqrstuvqxyz 1234567890"
  correct_bin = "01100001 01100010 01100011 01100100 01100101 01100110 01100111 01101000 01101001 01101010 01101011 01101100 01101101 01101110 01101111 01110000 01110001 01110010 01110011 01110100 01110101 01110110 01110001 01111000 01111001 01111010 00100000 00110001 00110010 00110011 00110100 00110101 00110110 00110111 00111000 00111001 00110000"

  # Exercise
  retrieved_bin = text_to_binary(initial_text)

  # Vertify
  if correct_bin == retrieved_bin:
    print("Unit Test Status: Successful | Translation from text to binary works correctly.")
  else:
    print(f"Unit Test Status: Error | There's an issue in translation from text to binary...\nExpected Output: {correct_bin}\nRetreaved output: {retrieved_bin}")

def bin_to_text_unit_test():
  # Setup
  initial_bin = "01100001 01100010 01100011 01100100 01100101 01100110 01100111 01101000 01101001 01101010 01101011 01101100 01101101 01101110 01101111 01110000 01110001 01110010 01110011 01110100 01110101 01110110 01110001 01111000 01111001 01111010 00100000 00110001 00110010 00110011 00110100 00110101 00110110 00110111 00111000 00111001 00110000"
  correct_text = "abcdefghijklmnopqrstuvqxyz 1234567890"

  # Exercise
  retrieved_text = binary_to_text(initial_bin)

  # Vertify
  if correct_text == retrieved_text:
    print("Unit Test Status: Successful | Translation from bin to text works correctly.")
  else:
    print(f"Unit Test Status: Error | There's an issue in translation from binary to text...{correct_text}\nRetreaved output: {retrieved_text}")


text_to_binary_unit_test()
bin_to_text_unit_test()