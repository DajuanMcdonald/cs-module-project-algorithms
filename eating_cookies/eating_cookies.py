'''
Input: an integer
Returns: an integer
UNDERSTAND:
----------
for 1 container with n elements there are x ways to consume[distribute] all elements

PLAN:
-----
use a cache

EXECUTE:
-------
'''
def eating_cookies(n, cache):
    # Your code here
    # Base Case
    if n < 0:
        return 0
    if n <= 1:
        cache[n] = 1
        return 1

    # set container/cache and x ways
    if cache[n] > 0:
        # if container not empty, x ways = cache's count
        ways_to_consume = cache[n]
    else:
        # otherwise x ways = consumption on demand
        ways_to_consume = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        # reset cache
        cache[n] = ways_to_consume
    #return x ways
    return ways_to_consume

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    # list comprehension for i in range
    print(f"There are {eating_cookies(num_cookies, [0 for i in range(num_cookies+1)])} ways for Cookie Monster to each {num_cookies} cookies")