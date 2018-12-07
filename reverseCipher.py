# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# Changes by Chris Arnold

message = input("Enter message: ") 
translated = " "

i = len(message) -1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
