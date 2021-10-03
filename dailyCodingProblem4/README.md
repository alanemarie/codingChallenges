## Description

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

## My comments:


 We can have a O(n) solution using O(n) sorting algoritmhs such as bucket sort and then search
 for the smallest integer using binary search (O(log n)), but then we will need O(n) extra space.

 The solution presented here is based in the one described in
 https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

 The key idea is first separating the negatives from the positive values by traversing the array, putting the negative values in front of the
 positive ones.

 After the separation, we will use a strategy that treats the values inside the array as positions.
 The positive values are marked with a negative symbol to indicate which values had been already traversed in the array.
 This marking works as follows: if the absolute value x is strictly less than the size of the array, then we mark the position corresponding to its
 value with a negative sign.
 After running this step in all positions of the array, we return the first index that had been not marked with a negative sign.
 Consider the following array (after the separation of positives from negatives): [-1,5,3,1].
  - We have that abs(-1) < 4 (the size of the array). We does not need to mark the first position of the array with a negative sign because it is already negative.
  - We have that 5 > 4. Since the fifth position does not exist in the array, we pass.
  - We have that 3 < 4. We mark the third position with a negative size to indicate that the number 3 has been traversed: [-1,5,-3,1].
  - We have that 1 < 4. We does not need to mark the first position of the array with a negative sign because it is already negative.
  - We finish traversing the array. Therefore, since the second position is positive (because we does not find he number 2 in the array), then we
    return 2 as the smallest missing integer.

 Note that if the input array only has negative numbers, than we return number 1 as the smallest missing integer.
 In the case that, after the separation and the marking steps, there is no number having negative sign, than we return the size of the array as the
 smallest missing integer.
