import collections

text = input("Enter your message.  ")
text = text.upper()
key_number = input("Choose a key number. ")
key_number = int(key_number)
def cipher(text,key_number):
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    upper = collections.deque(lowercase)
    lower = collections.deque(uppercase)
    const = ''.join(lower)

    lower.rotate(key_number)
    upper.rotate(key_number)

    upper = ''.join(upper)
    lower = ''.join(lower)

    table = text.maketrans(const,lower)

    print(text.translate(table))

cipher(text,key_number)
