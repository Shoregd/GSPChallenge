def say_hello(name):
    return f"hello {name}"

say_hello('Terry')
# Intended output:
#
# > say_hello("kay")
# => "hello kay"
def encode(text, key):
    cipher = make_cipher(key)

    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i)-65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 96) for i in range(1, 27)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
#print(f"""
# Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
#Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
#""")

#print(f"""
# Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
#Expected: theswiftfoxjumpedoverthelazydog
#  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
#""")


'''
Debugging with discovery
'''

def encode(text, key):
    print(f"Encode module initialises with text as: {text} and a key as: {key}")
    cipher = make_cipher(key)

    ciphertext_chars = []
    print(f'Module encrypts {text} by adding the index value of the character to 65.')
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    print(f'Decode module initialises with encrypted as: {encrypted} and a key as: {key}')
    cipher = make_cipher(key)

    plaintext_chars = []
    print(f'Module decodes the character by taking the index value of the character from 65. Amended to take 65 from index value')
    for i in encrypted:
        plain_char = cipher[ord(i)-65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 96) for i in range(1, 27)]
    print(f'alphabet variable initialised with base value as \n{alphabet}')
    cipher_with_duplicates = list(key) + alphabet
    print(f'cipher_with_dulplicates initialised as \n{cipher_with_duplicates}')
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
#print(f"""
# Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
#Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
#""")

#print(f"""
# Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
#Expected: theswiftfoxjumpedoverthelazydog
#  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
#""")

def get_most_common_letter(text):
    counter = {}
    print(f'Module initialises counter as dictionary containing: {counter}')
    print(f'For loop for each character in: \n"{text}" starts.')
    for char in text:
        print(f'*Loop iteration starts')
        counter[char] = counter.get(char, 0) + 1
        print(f'    *counter[{char}] is set to: {counter[char]}')
        print(f'*Loop iteration ends.')
    letter = sorted(counter.items(), key=lambda item: item[1])[-2][0]
    print(f'Sorts items from counter dictionary starting at: \n{counter.items()} \nresulting in: \n{letter}')
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")