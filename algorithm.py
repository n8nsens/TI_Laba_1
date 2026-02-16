import string

def get_inverse_key(k, n=26):
    for i in range(1, n):
        if (k * i) % n == 1:
            return i
    return None

def process_decimation(text, key_val, mode='encrypt'):
    alphabet = string.ascii_lowercase
    only_digits = "".join(filter(str.isdigit, str(key_val)))
    
    if not only_digits:
        error_msg = "Ошибка: ключ должен быть числом"
        return error_msg
    
    k = int(only_digits)
    n = 26

    if get_inverse_key(k, n) is None:
        error_msg = f"Ошибка: ключ {k} не взаимно простой с числом 26"
        return error_msg

    if mode == 'decrypt':
        k = get_inverse_key(k, n)

    result = []
    for char in text:
        is_upper = char.isupper()
        low = char.lower()
        
        if low in alphabet:
            x = alphabet.index(low)
            new_index = (x * k) % n
            new_char = alphabet[new_index]
            result.append(new_char.upper() if is_upper else new_char)
        elif char == " ":
            result.append(char)
        else:
            continue
            
    return "".join(result)

def process_vigenere(text, key_val, mode='encrypt'):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    n = len(alphabet)
    key_chars = [c.lower() for c in key_val if c.lower() in alphabet]
    
    if not key_chars:
        error_msg = "Ошибка: Ключ должен содеражать русские буквы"
        print(error_msg)
        return error_msg
    
    result = []
    key_index = 0 
    for char in text:
        is_upper = char.isupper()
        low = char.lower()
        
        if low in alphabet:
            x = alphabet.index(low)
            k = alphabet.index(key_chars[key_index % len(key_chars)])
            if mode == 'encrypt':
                new_index = (x + k) % n
            else:
                new_index = (x - k + n) % n
                
            new_char = alphabet[new_index]
            result.append(new_char.upper() if is_upper else new_char)
        
            key_index += 1
            
        elif char == " ":
            result.append(char)
        else:
            continue 
            
    return "".join(result)
