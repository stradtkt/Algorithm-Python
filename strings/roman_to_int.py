def roman_to_int(s: "str") -> "int":
    num = 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(s) - 1):
        if(roman[s[i]] < roman[s[i+1]]):
            num -= roman[s[i]]
        else:
            num += roman[s[i]]
    return num + roman[s[-1]]

if __name__ == '__main__':
    roman = "MDXXXIII"
    print(roman_to_int(roman))