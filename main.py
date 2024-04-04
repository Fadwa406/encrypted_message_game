import string 

def encrypt(shift, message):
  
  alphabet = string.ascii_lowercase

  encrypted_message = ""

  for letter in message:
    if letter.lower() in alphabet:
      original_position = alphabet.index(letter.lower())
      # I can change + to - to make the code reversed to take the encrpted message to show the decrypted one
      new_position = (original_position + shift ) % 26
      encrypted_letter = alphabet[new_position]
      
      if letter.isupper():
        encrypted_letter = encrypted_letter.upper()
        
      encrypted_message += encrypted_letter

    else:
      encrypted_message += letter

  print(encrypted_message)


user_message = input("Please enter the message: ")
shift_number = int(input("Please enter a shift number: "))
encrypt(shift = shift_number, message = user_message)
    
  






     
  
