'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
n1 = 1
n2 = 1
list_1 = []
while(n1 < 4000000):
    nth = n1 + n2
    n1 = n2
    n2 = nth
    if (n1 % 2 == 0 and n1 <= 4000000):
        list_1.append(n1)

print(sum(list_1))