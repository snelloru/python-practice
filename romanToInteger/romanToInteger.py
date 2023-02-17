class Solution:
 def romanToInt(self, s):
    roman_symbols_dict = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
    final_int = 0
    index=0
    print(len(s))
    while index < len(s):
        if index+1 < len(s) and s[index] + s[index+1] in roman_symbols_dict:
            final_int+= roman_symbols_dict[s[index] + s[index+1]]
            index = index + 1
        else: 
            final_int = final_int + roman_symbols_dict[s[index]]
        index+=1

    return final_int

