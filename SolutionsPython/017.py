# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters 
# used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
spell_num = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
spell_num_tens = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
spell_num_hundreds = {100:"onehundred", 200: "twohundred", 300:"threehundred", 400:"fourhundred", 500:"fivehundred", 600:"sixhundred", 700:"sevenhundred", 800:"eighthundred", 900:"ninehundred"}

def spellNum(number):
    num_string = str(number)
    if number == 0:
        return ""
    if number < 20 and number != 0:
        return spell_num[number]
    if number > 19:
        if len(num_string) == 2:
            return spell_num_tens[int(num_string[0])] + spellNum(int(num_string[1]))
        if len(num_string) == 3:
            if number in spell_num_hundreds:
                return spell_num_hundreds[number]
            else: 
                return spell_num[int(num_string[0])] + "hundredand" + spellNum(int(num_string[1::1]))
    if number == 1000:
        return "onethousand"
    else:
        return "Error"

sum_ = 0
for x in range(0,1001):
    sum_ += len(spellNum(x))
print(sum_)
# 21124
# Runtime: 0.004s