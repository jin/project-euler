#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(product):
    product = str(product)
    for index in range(len(product)/2):
        if (product[index] != product[-1-index]):
            return False
    return True



def main():
    largestPal = 0
    for firstDigit in range(100,999):
        for secondDigit in range(100,999):
            if (isPalindrome(firstDigit * secondDigit)) and ((firstDigit * secondDigit) > largestPal):
                largestPal = firstDigit * secondDigit
    print largestPal

main()
                