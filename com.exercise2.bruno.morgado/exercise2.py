'''
Student: Bruno Morgado
Student# 301-154-898
'''

'''
Write a short recursive Java method that determines if a string s is a palindrome,
that is, it is equal to its reverse. Examples of palindromes include 'racecar' and 'mom'.
Test the method by asking the user to provide string entries to be checked.
Hint: Check the equality of the first and last characters and recur (but be careful to return the correct value for both odd and even-length strings).
'''

def check_palindrome(word):

    if(len(word) < 2):
        return True
    elif(word[0] == word[-1]):
        return check_palindrome(word[1:-1])  
    
    return False


def main():

    word = ''

    while word != 'q':
        
        word = input('\nPlease type the word you want to check. Type "Q" to exit: ').lower().strip()
        if word == 'q':
            return
        answer = check_palindrome(word)

        if(answer):
            print(f'\n{word} is a palindrome')
        else:
            print(f'\n{word} is NOT a palindrome')


if __name__ == '__main__':
    main()
