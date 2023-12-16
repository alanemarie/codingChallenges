'''Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''


def checkPair(values, k):
    # this variable is useful to check if the numbers in the pair are the same
    half = 0

    for i in range(len(values)):
        v = (values[i] - k)
        if v < 0:
            v *= -1

        if v == k/2:
            half += 1
        else:
            half += 2

        if v in values and half > 1:
            return True
    return False



def main():
    values = [10,15,3,7]
    k = 17

    result = checkPair(values, k)
    print(result)



if __name__ == '__main__':
   main()


            
