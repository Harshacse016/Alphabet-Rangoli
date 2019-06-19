'''

You are given an integer,N . Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----     left = e-d-c- and right = d-e-
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e      from this above part is upper including this line
--e-d-c-b-c-d-e--      this line is lower part
----e-d-c-d-e----
------e-d-e------
--------e--------


'''
def print_rangoli(size):
    a = ['-','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    space = (size-1)*2         # no of spaces to be printed
    left = 1                   # this is used for printing the alphabets like e d c
    right = 0                  # this is used for printing the alphabets after left one like d e   
    ll = size                  # this is for getting the alphabets index
    s = ""

    #upper part

    for i in range(size):

        ll = size
        s = ""

        for j in range(space):      # this is for printing sapces
            print(a[0],end="")
        
        for j in range(left):       # this will append all the alphabets into a string s
            s = s + a[ll]
            if(left != 1):          # this is for starting alphabet should not contain '-' this character
                s = s + a[0]
            ll -= 1

        ll += 2

        for j in range(right):      # this is same as above
            s = s + a[ll]
            if(j != right-1):       # this is for last alphabet should not contain '-'
                s = s + a[0]
            ll += 1

        print(s,end="")             # we print the string

        for j in range(space):      # this is for printing the last spaces
            print(a[0],end="")
        
        space -= 2                  # this spaces must be reduced for each loop because the alphabets will inc for each loop
        left += 1                   # the alphabets should be inc
        right += 1                  # the alphabets will inc

        print("\r")                 # new line

    space = 2
    left = size-1
    right = size-2

    #lower part this is same as above

    for i in range(size-1):

        ll = size
        s = ""

        for j in range(space):
            print(a[0],end="")
        
        for j in range(left):
            s = s + a[ll]+a[0]
            ll -= 1

        ll += 2

        for j in range(right):
            s = s + a[ll] + a[0]
            ll += 1

        print(s,end="")

        for j in range(space-1):
            print(a[0],end="")
        
        space += 2
        left -= 1
        right -= 1

        print("\r")

if __name__ == '__main__':
    n = int(input("ENTER THE NUMBER TO DISPLAY:"))
    print_rangoli(n)