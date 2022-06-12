'''
Student: Bruno Morgado
Student# 301-154-898
'''

'''
Write a recursive method that takes a string as argument and determines if the string has more vowels than consonants.
Test the method by asking the user to enter a string. Hint: Write your recursive method to first count vowels and consonants.
'''

VOWELS = 'aeiou'


def vowel(letter):          
        
    return 1 if letter in VOWELS else 0


def has_more_vowels(input_string):
    
    letters = input_string.lower().replace(' ', '')
    last = len(letters) - 1

    def get_vowels(letters, last):

        if(last == 0):
            return vowel(letters[last])
        else:
            return vowel(letters[last]) + get_vowels(letters, last-1)

    count_vowels = get_vowels(letters, last)

    return count_vowels > (len(letters) - count_vowels), count_vowels, (len(letters)-count_vowels)


def main():

    string = ''

    while string != 'q':
        
        string = input('\nPlease type the string you want to check. Type "Q" to exit: ').lower().strip()

        if string == 'q':
            return
        answer = has_more_vowels(string)

        if(answer[0]):
            print(f'\n{string} has more vowels than consonants: {answer[1]} vowels and {answer[2]} consonants')
        else:
            print(f'\n{string} has more consonants than vowels: {answer[2]} consonants and {answer[1]} vowels')


if __name__ == '__main__':
    main()


