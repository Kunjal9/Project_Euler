# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def multiple_of_3_and_5(num):
    list_of_i = []
    for i in range(1,num):
        if (i %5 ==0) or (i%3==0):
            list_of_i.append(i)
    return sum(list_of_i)

def three_and_five(s = 0):
    for i in range(1,1000):
        
        if (i % 3  == 0 or i%5 == 0):
            s = s + i
    return s        


if __name__ == '__main__':
    print(multiple_of_3_and_5(1000))
    print(three_and_five())