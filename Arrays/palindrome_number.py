def is_palindrome(n):
    return str(n) == str(n)[::-1]

 
n=int(input("Enter a number: "))
print(is_palindrome(n))  