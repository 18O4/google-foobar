import base64
encrypted=input("> please input the string you were given \n")
my_eyes=str.encode(input("> please input your user name (foobar:~/ <YOUR USERNAME HERE>$) \n"))
decoded=base64.b64decode(encrypted)
decrypted=""
for i in range(0,len(decoded)):
    decrypted+=chr((my_eyes[i%len(my_eyes)] ^ decoded[i]))
print('> decrypted message: \n', decrypted)