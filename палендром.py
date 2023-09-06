def is_palendrome(string):
    return string == string[::-1]

print(is_palendrome(input('Веди слово: ')))