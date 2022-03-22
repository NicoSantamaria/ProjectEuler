# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters 
# used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
def sum_spelling(spell_num, spell_num_tens):
    return sum(len(spellNum(x, spell_num, spell_num_tens)) for x in range(1001))


def spellNum(number, spell_num, spell_num_tens):
    """
    Spells a number from 1-1000
    :param number (int):
    return (string): The number spelled in English, no spaces
    """
    num_string = str(number)

    if number == 0:
        return ""

    # Returns corresponding string from spell_num dict
    if number < 20 and number != 0:
        return spell_num[number]

    if number > 19:

        # If two digit number, return concatenation of tens place and ones place
        if len(num_string) == 2:
            return spell_num_tens[int(num_string[0])] + spellNum(int(num_string[1]), spell_num, spell_num_tens)
        
        # For three digit numbers
        if len(num_string) == 3:

            if not number % 100:
                return spell_num[number / 100] + "hundred"
                
            else:
                return spell_num[int(num_string[0])] + "hundredand" + spellNum(int(num_string[1::1]), spell_num, spell_num_tens)
    
    if number == 1000:
        return "onethousand"

    else:
        return "Error"


sum_spelling(
    {
        1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
        11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
        19:"nineteen"
    },
    {
        2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"
    }
)
# 21124
# Runtime: 0.159s

"""
NOTES:
I could do this more elegantly and probably a bit quicker if I were
to rewrite the code to pull from a single dict (rather than two), but
this works well enough.
"""