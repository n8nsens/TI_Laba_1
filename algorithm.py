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
