import string

def vol(rad):
    return ((rad**3) *3.14 *4.0/3)


def ran_check (num, low, high):
    if num > low and num < high:
        print ('num is in the range')


def ran_bool(num, low, high):
    if num > low and num < high: # if num in range (low, high)
        return True
    else:
        return False


def up_low(s):
    upcase_count = 0;
    lowercase_count = 0
    for c in s:
        if c.islower():
            lowercase_count += 1
        if c.isupper():
            upcase_count += 1
    print('No. of Upper case: ' , upcase_count)
    print('No. of Loer case: ' , lowercase_count)


def unique_list(l):
    print (list(set(l)))

def unique_list2(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    print(x)

def multiply(numbers):
    result = 1
    for num in numbers:
        result = result * num
    print (result)

def palindrome(s):
    reverse = s[::-1]
    print (s == reverse)


def ispangram(str1):
    alphabet=string.ascii_lowercase
    alpha = set (alphabet)
  #  print(alpha)
   # sort_str = ''.join(sorted(str1))
   # lower_str = sort_str.lower()
   # print (lower_str)
    unique = set(str1.lower())
  #  print (unique)
    print (alpha <= unique)
    
    
def main():
  #  up_low('AABBCCDDFF ioowp   rivur')
  #  unique_list2([1,2,3,4,5,6,7,1,2,3,3,3,3,3,4,4,4,9])
  #  palindrome('ab')

    ispangram('abcdefghijklmnpoqrstuvwxyz23456780')

main()
