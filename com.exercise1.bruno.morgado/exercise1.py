'''
Student: Bruno Morgado
Student# 301-154-898
'''

'''
Create a recursive algorithm to compute the product of two positive integers, m and n, using only addition and subtraction.
Implement the Java or Python code. Hint: You need subtraction to count down from m or n and addition to do the arithmetic
needed to get the right answer. Check linearSum method from Week 5 examples.
'''

def positive_integer_multiplier(m: int, n: int):

    try:
        
        if not type(m) is int or not type(n) is int:
            raise TypeError("\n****** Only integers are allowed ******\n")

        if m < 0 or n < 0:
            raise ValueError("\n****** Only positive integers are allowed ******\n")

        if m == 0 or n == 0:
            return 0 

        return m + positive_integer_multiplier(m, n-1)
    
    except Exception as e:
        
        print(e)

def main():

    x = positive_integer_multiplier(3, 2)

    print(x)


if __name__ == '__main__':
    main()