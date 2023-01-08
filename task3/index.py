# Задание 1
def convert_to_binary(number: int) -> str:
    base = 2
    if number == 0:
        return "0"
    result = ""
    while(number > 0):
        remainder = number % base
        result = str(remainder) + result
        number = int(number / base)
    return result 

# Задание 2
def is_palindrome(stroka: str) -> bool:
    punctuations = [':', ',', '.', '!', '?', '(', ')', '-', '_']
    stroka = stroka.lower()
    stroka = stroka.replace(' ', '')
    for punctuation in punctuations:
        if punctuation in stroka:
            stroka = stroka.replace(punctuation, '')

    return stroka == stroka[::-1]

number = int(input())
print(convert_to_binary(number))
print(is_palindrome(input()))