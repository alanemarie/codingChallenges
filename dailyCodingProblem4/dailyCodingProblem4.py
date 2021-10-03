#This problem was asked by Stripe.
#
#Given an array of integers, find the first missing positive integer in linear time and constant space.
#In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
#You can modify the input array in-place.
#
#
#
#
#[My comments]:
#
# We can have a O(n) solution using O(n) sorting algoritmhs such as bucket sort and then search
# for the smallest integer using binary search (O(log n)), but then we will need O(n) extra space.
#
# The solution presented here is based in the one described in
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
#
# The key idea is first separating the negatives from the positive values by traversing the array, putting the negative values in front of the
# positive ones.
#
# After the separation, we will use a strategy that treats the values inside the array as positions.
# The positive values are marked with a negative symbol to indicate which values had been already traversed in the array.
# This marking works as follows: if the absolute value x is strictly less than the size of the array, then we mark the position corresponding to its
# value with a negative sign.
# After running this step in all positions of the array, we return the first index that had been not marked with a negative sign.
# Consider the following array (after the separation of positives from negatives): [-1,5,3,1].
#  - We have that abs(-1) < 4 (the size of the array). We does not need to mark the first position of the array with a negative sign because it is already negative.
#  - We have that 5 > 4. Since the fifth position does not exist in the array, we pass.
#  - We have that 3 < 4. We mark the third position with a negative size to indicate that the number 3 has been traversed: [-1,5,-3,1].
#  - We have that 1 < 4. We does not need to mark the first position of the array with a negative sign because it is already negative.
#  - We finish traversing the array. Therefore, since the second position is positive (because we does not find he number 2 in the array), then we
#    return 2 as the smallest missing integer.
#
# Note that if the input array only has negative numbers, than we return number 1 as the smallest missing integer.
# In the case that, after the separation and the marking steps, there is no number having negative sign, than we return the size of the array as the
# smallest missing integer.



######
# - input: l (array of integers)
# - output: array with negative numbers preceding the positives and also a boolean (True if l has only negatives, False otherwise).
#
# This function shifts all the negative values before the positives and also counts the number of negatives to return if the array
# has only negatives or not.
#
# Complexity: O(n) 
######
def shiftIntegers(l):
    negativeIndex = 0
    cont = 0

    for i in range(0,len(l)):
        if l[i] < 0:
            aux = l[i]
            l[i] = l[negativeIndex]
            l[negativeIndex] = aux
            negativeIndex += 1
            cont += 1

    if cont == len(l):
        return True
    else:
        return False
            
  
######
# - input: l (array of integers)
# - output: the smallest positive missing integer
#
# This function treats each values as indexes of the array l.
#
# Complexity: O(n) (and constant extra space)
######
def findSmallestMissingInteger(l):

    #shift integers and count the amount of negative values
    onlyNegatives = shiftIntegers(l)

    #returns 1 only if l has only negatives
    if onlyNegatives:
        return 1
    else:

        #this part of the function marks the positions with the negative sign (-) if the value was read in the array
        # e.g.: if the value 3 was read in the array (and the size of the array is at least 3), then we mark the
        # number that is in the third position with the negative sign
        for i in range(0,len(l)):
            if(abs(l[i])-1 < len(l) and l[abs(l[i]-1)-1] > 0):
                l[abs(l[i])-1] = -l[abs(l[i])-1]

        # this part looks for the smallest position that is positive. It means that the array has no value corresponding
        # to that index.
        # e.g.: if the position 2 has a positive number inside, it means that the value 2 does not exist in the array.
        j = 0
        for i in range(0,len(l)):
            if l[i] > 0:
                return j+1
            else:                
                j += 1
                
    return len(l)+1
    

def main():
    l = [3,4,-1,1]
    i = findSmallestMissingInteger(l)
    print("The smallest missing integer is "+str(i))
    

if __name__ == "__main__":
    main()
