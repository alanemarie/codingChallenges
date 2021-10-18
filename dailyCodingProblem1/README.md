## Description

Problem from Google:

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?

### Naive solution:

Given the number c, check all pairs of numbers to find if there is some (a,b) where a+b = c. 

### Efficient solution:

Given the number c, create a hash table where each key is a number of the list and each value associated to a key x 
corresponds to k-c. 
Time to create the hash: O(n)

Check if there is some value of the hash that is in the hash.
Time to check the hash: expected O(n) (because search operations in a hash are expected O(1)).

[Tricky part]:

If the k value is equal to the double of some value in the given list, the output will return wrong answer.
For example, consider the list [1,2,3] and k=4. The algorithm will return 2 (because 2x2=4 and k-x (4-2) is a key in the hash table).
Therefore, we have to check if there is more than one element in the list that is equal to k/2.
