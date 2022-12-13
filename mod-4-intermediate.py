#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    alphabet = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letter_number = (ord('@')+(alphabet.index(letter))+shift) 
    if letter_number >= 91:
        return chr(letter_number - 26)
    elif letter == " ":
        return letter
    else:
        return chr(letter_number)

    
def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    import string

    alphabet_string = string.ascii_uppercase
    shifted = alphabet_string[shift:] + alphabet_string[:shift]
    table = str.maketrans(alphabet_string, shifted)

    final_message = message.translate(table)

    return (final_message)

    A = ord('A')
    return ''.join(
        chr((ord(char) - A + shift) % 26 + A) if 'A' <= char <= 'Z' else char
        for char in message.upper())


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    alphabet = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    alphabet_2 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letter_number = (ord('@')+(alphabet.index(letter))+(alphabet_2.index(letter_shift))) 
    if letter_number >= 91:
        return chr(letter_number - 26)
    elif letter == " ":
        return letter
    else:
        return chr(letter_number)

    
def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    message_int = [ord(i) for i in message]
    final_answer = ''
    for i in range(len(message_int)):
        if message[i].isalpha():
            value = (message_int[i] + key_as_int[i % key_length]) % 26
            final_answer += chr(value + 65)
        else:
            final_answer += message[i]
    return final_answer


# In[ ]:





# In[ ]:




