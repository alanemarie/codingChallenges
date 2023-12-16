'''Problem from Uber:

Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except the one at i. 
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6]. 

Follow-up: what if you can't use division?'''

def multiply(values):
    left = [1]*len(values) #this list stores the accumulated product of the predecessors of i 
    right = [1]*len(values) #this list stores the accumulated product of the sucessors of i 
    newValues = [1]*len(values) #this list stores the product of all predecessors and sucessors of i

    # for loop -- left list
    for i in range(len(left)):
        if i == 0:
            left[i] = values[i]
        else:
            left[i] = left[i-1] * values[i]

    # for loop -- right list
    for i in range(len(right)-1,-1,-1):
        if i == len(values)-1:
            right[i] = values[i]
        else:
            right[i] = right[i+1] * values[i]

    # for loop -- product of predecessors and sucessors
    for i in range(len(values)):
        if i == 0:
            newValues[i] = right[i+1]
        elif i == len(values)-1:
            newValues[i] = left[i-1]
        else:
            newValues[i] = left[i-1] * right[i+1]

    return newValues


def main():

    values = [1,2,3,4,5]

    result = multiply(values)
    print(result)


if __name__ == '__main__':
   main()

    
