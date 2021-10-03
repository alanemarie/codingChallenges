## Description

Problem from Uber:

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?


## Comments

We can compute the product of all numbers and then divide this number by each
value in the given array, although we have to take care if such value is 0.
This easy solution is O(n).

The solution below is based in the one available in
[https://www.geeksforgeeks.org/a-product-array-puzzle/](https://www.geeksforgeeks.org/a-product-array-puzzle/)

The idea is the creation of two arrays (left and right), where one computes the product of the predecessors of each value of the array, and the other computes the product of 
the sucessors of each value of the array. The final product will correspond, for each value, to the product of the predecessors bu the sucessors.

This solution is O(n), since build the left, the right, and the final array with the products can be done in O(n) (having one loop for each of these arrays.

[Solution](https://github.com/alanemarie/codingChallenges/tree/main/dailyCodingProblem2)
