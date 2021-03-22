# Шифрование текста
def encrypt(text, key):
    encrypted_text = ''
  
    for symb in text:
        encrypted_text += chr(ord(symb) ^ eval(key))

    return encrypted_text

# Чтение из файла
with open('message.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print(text)

key = input('Enter a key\n')

encrmess = encrypt(text,key)

# Запись в файл
with open('message.txt', 'w') as file:
    file.write(encrmess)
    
# Чтение из файла шифра
with open('message.txt','r') as file:
    for line in file:
        codmess = encrypt(text,key)

print(f'Coding message = {codmess}')
