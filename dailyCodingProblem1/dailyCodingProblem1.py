#Problem from Google:

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

######

# - input: list of integers l and integer value k
# - output: True if l has two numbers a and b where a+b=k and False otherwise
# 
# Complexity: Expected O(n)

def findSum(l, k):
    hash = {}
    half = 0

    #time complexity: O(n)
    for x in l:
        hash[x] = k-x 
        if(float(k-x) == k/2):
            half += 1

    #this loop checks if the hash has some value that lies inside l
    #search operation in hash is expected O(1)
    
    #time complexity: expected O(n)
    for key in hash:
        if hash.get(key) in hash:
            if((float(hash[key]) == k/2 and half >= 2) or hash[key] != k/2):
                print(str(key)+ "+" +str(hash.get(key)))
                return True

    return False

######


def main():
    l = [10,15,3,7]
    k = 15
    print(findSum(l,k))
    
if __name__ == "__main__":
    main()
