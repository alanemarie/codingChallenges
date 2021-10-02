#Problem from Uber:

#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?


#We can compute the product of all numbers and then divide this number by each
#value in the given array, although we have to take care if such value is 0.
#This easy solution is O(n).

#The solution below is based in the one available in
#https://www.geeksforgeeks.org/a-product-array-puzzle/.

######

# - input: array of integers l
# - output: array of integers prod returning the products
# 
# Complexity: O(n)

def multiply(l):
    n = len(l)

    #array of the accumulated sum of the predecessors of a position in the array 
    left = [1]*n

    #array of the accumulated sum of the sucessors of a position in the array 
    right = [1]*n

    #array of products left*right for each value in the given list l 
    prod = [1]*n


    #this loop computes the accumulated sum of the predecessors, except
    #from the first position
    for i in range(1,n):
        left[i] = left[i-1]*l[i-1]

    #this loop computes the accumulated sum of the sucessors, except
    #from the last position
    #we walk on list l in reverse order
    for i in range(n-2,-1,-1):
        right[i] = right[i+1]*l[i+1]
    
    for i in range(0,n):
        prod[i] = left[i]*right[i]
       
    return prod
       

def main():
    l = [3,2,1]
    prod = multiply(l)

    for i in range(0,len(l)):
        print("l["+str(i)+"]: "+str(l[i]) + " mult:" + str(prod[i]))

if __name__ == "__main__":
    main()
