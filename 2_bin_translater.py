def text_to_binary(text):
  binary_string = ""
  
  for character in text:
    binary_char = bin(ord(character))[2:]
    binary_string += binary_char + " "

  return binary_string[:-1]

def binary_to_text(binary_string):
  binary_characters = binary_string.split(' ')

  text = ""
  
  for binary_value in binary_characters:
    text += chr(int(binary_value, 2))

  return text

# Some tests:
text = "Hello, World!"
binary = text_to_binary(text)
print(binary)  # Output: "01101000 01100101 01101100 01101100 01101111 00100000 01010111 01011101 01101111 01110010 01101111 01110100"

text_again = binary_to_text(binary)
print(text_again)  # Output: "Hello, World!"