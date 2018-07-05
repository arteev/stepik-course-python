alphabet = input()
crypt = input()
str_to_crypt = input()
str_to_decrypt = input()
for c in str_to_crypt:
    print(crypt[alphabet.index(c)], end="")
print()
for c in str_to_decrypt:
    print(alphabet[crypt.index(c)], end="")
