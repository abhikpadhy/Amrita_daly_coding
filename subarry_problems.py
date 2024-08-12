##"Most of the problem statement is based on sliding window and array"

"""
    1.find the maximum sum of a subarray of a given size k within an array
    2.Find Out Pairs with given sum 'k' in an array
    3.Find the minimum difference betwen 2 elements of an array
    4.Find the maximum difference betwen 'k' and  the elements of an array
    5.Find the fibonacci series of nth no 
    6.Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
        Numbers can be 0 or negative.
    7.Compute number of integers divisible by k in range [a..b].
    8.Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    9.Given an array nums of n integers where nums[i] is in the range [1, n], 
    return an array of all the integers in the range [1, n] that do not appear in nums.
    10.Given an integer n, return true if it is a power of two. Otherwise, return false.
    An integer n is a power of two, if there exists an integer x such that n == 2x.
    11.Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

"""

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]

def max_sum_subarray(arr, k):
    """find the maximum sum of a subarray of a given size k within an array"""
    l = len(arr)
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(len(arr)-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum,window_sum)
    return   max_sum  

def max_sum_subarray_sw_method_2(arr, k):
    """find the maximum sum of a subarray of a given size k within an array"""
    current_window = 0
    max_sum = 0
    i = 0
    j = 0
    while j < len(arr):
        current_window = current_window + arr[j]
        if j-i+1 < k :
            j = j+1
        if j-i+1 == k:
            max_sum = max(max_sum,current_window)
            i=i+1
            j=j+1
            current_window = current_window - arr[i]

    return max_sum

#print(max_sum_subarray(arr, 3))
#print(max_sum_subarray_sw_method_2(arr, 3))

## Option 1
def arr_sum1(arr,k):
    "Find Out Pairs with given sum 'k' in an array"
    arr.sort()
    print(arr)
    left = 0
    right = len(arr)-1
    while (right>=left):
        if (arr[left] + arr[right] > k):
            right -=1
        elif(arr[left]+arr[right] < k):
            left +=1
        elif (arr[left] + arr [right] == k):
            right -=1
            left +=1
            return arr[left] , arr[right]
        else:
            return False
        
## Option 2        
def arr_sum2(arr,k) :
    "Find Out Pairs with given sum 'k' in an array"
    l=[]
    for i in arr:
        if (k-i) in arr:
            print(i,k-i)
            return True     
    return False 

arr =[1,2,4,5,6,7,10]
k=17
#print(arr_sum2(arr,k))         

def twoSum_index(nums,targets):
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    Ex:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    dec={}
    for i,no in enumerate(nums):
        if (targets-no) in dec:
            return dec[targets-no],i
            
        dec[no] = i    
    return None 


nums = [2,7,11,15]
targets = 9    
print(twoSum(nums,targets))

def missing_no_in_array(arr):
    n = arr[-1]
    total = n*(n+1) // 2
    print(total)
    sum_arr = sum(arr)
    print(sum_arr)
    no_missing = total - sum_arr
    print(no_missing)

arr = [1,2,4,5,6,7]    
#missing_no_in_array(arr)

def minimum_difference_in_array(arr):
    "Find the minimum difference betwen 2 elements of an array"
    arr.sort()
    min_diff = max(arr)-min(arr)
    for i in range(len(arr)-1):
        min_diff = min((arr[i+1] - arr[i]),min_diff)
    return   min_diff

def maximum_difference_in_array(arr,k):
    "Find the maximum difference betwen 'k' and  the elements of an array"
    arr.sort()
    max_diff = 0
    for i in range(len(arr)):
        if arr[i] > k:
            max_diff = max((arr[i] - k),max_diff)
        elif arr[i] < k:
            max_diff = max((k-arr[i]),max_diff)  
        elif arr[i] == k:
             max_diff = max((arr[i] - k),max_diff)    
    return   max_diff


arr =[12,42,40,65,26,70,15]
#print(minimum_difference_in_array(arr))  
print(maximum_difference_in_array(arr,61))

def fibonacci_series(n):
    """Find the fibonacci series of nth no """
    n1=0
    n2=1
    sum1 = n2
    count = 1
    while count <= n:
        n1 = n2
        n2 = sum1
        sum1 = n1+n2
        print(sum1)
        count +=1
    return sum1

print(fibonacci_series(10)) 

def get_largest_non_adj_sum(array):
    """Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
    Numbers can be 0 or negative.
    """
    if len (array)==0:
        return 0
    if len(array)==1:
        return array[0]
            
    cur_max_sum =0
    pre_max_sum=0

    for i in range(2,len(array)):
        pre_max_sum = cur_max_sum
        cur_max_sum = max(pre_max_sum,array[i-2]+array[i])
    return  cur_max_sum  

array = [2, 4, 6, 2, 5]
print(get_largest_non_adj_sum(array))


def divisible(a,b,k):
    """Compute number of integers divisible by k in range [a..b]"""
    if a==b:
        return 0
    count = 0
    l=[]
    for i in range(a,b):
        if a==0:
            i=i+1
        if i % k == 0:
           l.append(i)
           count = count+1
    return l,count 

print(divisible(0,20,3)) 

def two_sum(arr,k):
    """Given an array of integers nums and an integer target, 
    return index of the two numbers such that they add up to target.
    """
    ans = []
    track = []
    if all(isinstance(x,int) for x in arr) != True:
        return False
    for i,n in enumerate(arr):
        if k-n in arr and i not in track :
            ans.extend([(i,arr.index(k-n))])
            track.extend([i,arr.index(k-n)])
                
    return ans        
        
nums = [2,7,8,11,15]
print(two_sum(nums,10))  

def two_sum(nums,target):
    """Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    """
    for i in range(len(nums)):
	    for j in range(i+1,len(nums)):

	        if nums[i]+nums[j] == target:
	            return i,j
    return False
					 
nums = [2,7,8,11,15]
target = 10
print(two_sum(nums,target))


class Solution(object):
    """You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

    ##  Option1
    def maxProfit(self, prices):
        """
        Brute Force method O(n^2) complixity
        :type prices: List[int]
        :rtype: int
        """
        max_val = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i] < prices[j]:
                    max_val = max(max_val,prices[j]-prices[i])
        return max_val   
    ##  Option1    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0
        if all(isinstance(x, int) for x in prices) != True:
            return False
        for i in prices[1:]:
            min_price = min(min_price,i)
            max_profit = max(max_profit,i-min_price)
              
        return max_profit      
        
#prices = [7,1,5,3,6,4]   
#prices1 = [7,6,4,3,1]
#obj = Solution ()  
#print(obj.maxProfit(prices1))    

def FindProduct(arry):
    """
    :type prices: List[int]
    :rtype: int
    """
    ans = []
    for i in range(len(arry)):
        product = 1
        left = 0
        right = len(arry)-1
        while left < i:
            product = product * arry[left]
            left +=1
        while right > i:
            product = product * arry[right]
            right -=1
        ans.append(product)    
                         
    return ans     

def findDisappearedNumbers(nums):
    """Given an array nums of n integers where nums[i] is in the range [1, n], 
    return an array of all the integers in the range [1, n] that do not appear in nums."""
    set_no = set(nums)
    missing_no = []
    for num in range(1,len(nums)+1):
        if num not in set_no:
            missing_no.append(num)
    return  missing_no

##function Call
nums = [4, 3, 2, 7, 8, 2, 3, 1]  
nums = [1,1]
print(findDisappearedNumbers(nums)) 


def isPowerOfTwo(n):
    """Given an integer n, return true if it is a power of two. Otherwise, return false.
    An integer n is a power of two, if there exists an integer x such that n == 2x."""
    if n == 0 or n == 1:
        return False

    elif n % 2 != 0:
        return False
    elif n & (n-1) == 0:
        return n

 ##function Call       
n = 75
print(isPowerOfTwo(n))

def sortedSquare(nums):
    """
    Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order.
    """
    ans = [] 
    for i in nums:
        ans.append(i*i)
    ans.sort()    
    print(ans) 

nums = [-4,-1,0,3,10]  
nums=[-7,-3,2,3,11]
print(sortedSquare(nums)) 