""" 1.  Find the second higest occurance of charactor in a string
    2.  Find the longest common carector between 2 string
    3.  Find the frequency of word in string
    4.  Python program to remove consecutive strings.
    5.  Python Program To Recursively Remove All Adjacent Duplicates
    6.  Python Program To  Remove  duplicate charactor from a list
    7.  convert the string 'c2n3m4' to 'ccnnnmmmm' 
        by following the pattern given in the string by replacing the integer with the no of charactor
    8.  Write a Python program to find the longest word in a sentence.
    9.  Write a Python program to count the number of occurrences of a specific substring in a string
    10. Given a string array words, return the maximum value of length(word[i]) * length(word[j]) 
        where the two words do not share common letters. If no such two words exist, return 0
    11. Given a pattern "abba" and a string s "dog cat cat dog", find if s follows the same pattern.
    12. Find the longest common prefix in a list of strings
    13.  Find the Index of the First Occurrence in a String
    14. Shortest Uncommon Substring in an Array
    15. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    16. Longest valid Parentheses in a string
    17. Find the Index of the First Occurrence in a String
    18. Checks if two strings are anagrams.
    19. 3121. Count the Number of Special Characters II :
    You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, 
    and every lowercase occurrence of c appears before the first uppercase occurrence of c.
    Return the number of special letters in word.
    20. Get the number of occurrence of sub string in full string, when the sub string character coming in same order.
    21. Given 2 string str1 and str2 Count Prefix and Suffix Pairs in str2 should be str1
    22. Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
import string

s="GeeksforggGeeks"

def common_charactor(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    print(set(s1) & set(s2))

def common_charactor_1(s1,s2):
    "Find the longest common carector between 2 string"
    l=[]
    s1=s1.lower()
    s2=s2.lower()
    for i in set(s1):
        for j in set(s2):
            if i == j:
                l.append(i)
    return(l)            
#Amrita loves to eat apple and mangow . Her sister love apple but nor mangow .
#common_charactor("Aarushi","Abhik")
#print(common_charactor("Aarushi","Abhik"))                

def second_highest_occurance_char(s):
    "Find the second higest occurance of charactor in a string"
    dec = {}
    first_max_val = 0
    second_max_val = 0
    for i in s.lower():
        dec[i] = dec.get(i,0)+1
    print(dec)  
    for i in dec.values():
        if i > first_max_val:
            second_max_val = first_max_val
            first_max_val = i
        elif i > second_max_val and i < first_max_val:
            second_max_val = i    
   
    second_chr = [ch for ch,count in dec.items() if count == second_max_val ]
    return (second_chr, second_max_val)

def longest_common_substring(str1, str2):
    "Function to find longest common substring between 2 string."
    len1, len2 = len(str1), len(str2)
    max_len ,end_pos = 0,0
    
    dp = [[0 for i in range(len2+1)] for i in range(len1 + 1)]
   
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i 
            else:
                dp[i][j] = 0
    longest_common_sub_string = str1[(end_pos - max_len) : end_pos ]            
    return longest_common_sub_string, max_len

def frequence_of_words_in_string():
    "Find the frequency of word in string"
    s= input("Enter the string: ")
    s=s.split(' ')
    dec={}
    for i in s:
    #    dec[i] = dec.get(i,0)+1
        if i not in dec:
            dec[i]=0
        dec[i] += 1    

    return dec    

l1=['a','b','c']
l2=[1,2,3]

def list_to_dect(l1,l2):
   "convert list to dectionary"
   dec = dict(zip(l1,l2))
   print("Dec: ",dec)
   "convert dec touple"
   for i in dec.items():
       print("touple: ", i)

s="geeksforgeeks"

def frequent_occurance_char(s):
    "Write a Python program to find the most frequent character in a string."
    s=s.lower()
    dec={}
    for i in s:
        dec[i]=dec.get(i,0)+1
    max_char_count = max(dec.values())    
    max_char = [k for k,v in dec.items() if v == max_char_count][0]
    return max_char,max_char_count

#Option1
def remove_duplicate_charactor_1(s):
    #https://www.geeksforgeeks.org/remove-consecutive-duplicates-string/
    "Python program to remove consecutive duplicate charactor in a strings."
    new_str=''
    i=0
    j=0
    while j < len(s):
        #If both elements are same then skip.
        if s[i] == s[j]:
            j+=1
        #If both elements are not same then append new element.    
        elif s[i] != s[j]:
            new_str = new_str +s[i]
            i=j
            j+=1   
    new_str = new_str + s[j-1]        
    return new_str

#OPTION-2
def remove_duplicate_charactor_2(s):
    "Python program to remove consecutive duplicate charactor in a strings."
    new_elements=s[0]
    for i in range(1,len(s)):
       if s[i] != s[i-1]:
           new_elements = new_elements+s[i]
    return    new_elements

def isPalindrome(s):
    if len(s) == 0:
        return False
    elif s == s[::-1]:
        return True

def recursively_remove_duplicate_charactor(s):
    "Python Program To Recursively Remove All Adjacent Duplicates"
    #https://www.tutorialspoint.com/remove-all-adjacent-duplicates-in-string-in-python
    stk=[]
    st=''
    i=0
    while i<len(s):
        #Remove from the stack if match found with last element of stack with current element
        if stk and stk[-1]==s[i]:
            stk.pop(-1)
            i+=1
        #add the element to the stack if the stack is empty or last element of stack does not match with current element of string
        else:
            stk.append(s[i])
            i+=1
    st=''.join(i for i in stk)
    return st    

#OPTION1
def remove_duplicate_charactor_list_1(l):
    """Python Program To  Remove  duplicate charactor from a list"""
    stk = [l[0]]
    
    for i in range(1,len(l)):
        if l[i-1] != l[i]:
            stk.append(l[i])
    return(stk)    

#OPTION2 
def remove_duplicate_charactor_list_2(l):
    """Python Program To  Remove  duplicate charactor from a list"""
    var = ''
    temp =[]
    for i in l:
         if i != var:
             temp.append(i)
         var= i  
    return temp

## OPTION 1
str1 ="c2n3m4"
def check_str(str1):
    """convert the string 'c2n3m4' to 'ccnnnmmmm' 
    by following the pattern given in the string by replacing the integer with the no of charactor"""
    new_str = ''
    new_chr = ''
    num = 0
    for ch in str1:
        if ch.isalpha:
            print("the chr is string")
            new_chr = ch
        else:
            no = int(ch)
            print("the chr is int")
            new_str =new_str+(new_chr*no)

    return(new_str)

## OPTION 2   'c2n3m4' to 'ccnnnmmmm' 
def check_str(str1):
    ch =''
    for i in range(1,len(str1)):
        if str1[i].isdigit():
            ch = ch+ str1[i-1]*int(str1[i] ) 
        elif str1[i].isalpha():
            continue
        else:
            return False        
    return ch

## OPTION 1
def check_int_char_in_string(s) :
    output = s[0]
    char = s[0]
    count = 0
    for ch in s:
        if ch == char:
            count += 1
        else:
            output = output+str(count)+ch
            count = 1
            char = ch
    output = output+str(count)
    return output  

## OPTION 2 'ccnnnmmmm' to 'c2n3m4' 
def check_int_char_in_string(str1):
    dec={}
    ch=''
    for i in str1:
        dec[i] = dec.get(i,0)+1
    
    for k,v in dec.items():
        ch = ch+k+str(v)
    return ch 

str1 ="ccnnnmmmm"

def longest_word_in_sentence(sentence):
    "Write a Python program to find the longest word in a sentence."
    str1 = sentence.split(" ")
    longest_word = max(str1,key=len)
    return longest_word 

def count_substring_occurrences(str1, sub):
    "Write a Python program to count the number of occurrences of a specific substring in a string"
    index, count = 0, 0
    while True:
        index = str1.find(sub,index)
        if index == -1:
            break
        count +=1
        index +=1
    return  count

def max_product(words):
    """Given a string array words, return the maximum value of length(word[i]) * length(word[j]) 
    where the two words do not share common letters. If no such two words exist, return 0.
    Example 1:

    Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    Output: 16
    Explanation: The two words can be "abcw", "xtfn".
    """
    max_wrod = 0
  
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if not set(words[i]) & set(words[j]):
                max_wrod =max(max_wrod,(len(words[i])*len(words[j])) ) 
    if max_wrod == 0:
        return "No such pair"
    else:
        return  0     
      
class Solution_wordPattern:
    ##option 1
    def wordPattern_option1(pattern, s):
        """Given a pattern "abba" and a string s "dog cat cat dog", find if s follows the same pattern.
        Examples:
        Input: pattern = "abba", s = "dog cat cat dog"
        Output: true
        Input: pattern = "abba", s = "dog cat cat fish"
        Output: false
        Input: pattern = "aaaa", s = "dog cat cat dog"
        Output: false
        """
        words = s.split(' ')
        if len(set(pattern)) != len(set(words)):
            return False
            
        pt_map = {}
        used_words = set()
        
        for ch,word in zip(pattern, words):
            if ch not in pt_map:
                if word in used_words:
                    print("Duplicate word found  for the charactor patten")
                    return False
                pt_map[ch] = word
                used_words.add(word)
            elif pt_map[ch] != word: 
                print("Word does not match with existing charactor patten")
                return False
        return True 

def wordPattern_option2(self, pattern, str1):
        ##OPtion 2
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pt_dect = {}
        st_dect ={}
        words = str1.split(' ')
        if len(pattern) != len(words):
            return False
        for pt,s in zip(pattern, words):
            if pt not in pt_dect:
                pt_dect[pt] = s
            if s not in st_dect:
                st_dect[s]=pt
            if pt_dect[pt] != s or st_dect[s] != pt :
                return False
        print(pt_dect)    
        print(st_dect)
        return True    
            
##function Call
pattern = "abba" 
str1 = "dog cat cat dog"       
obj = Solution_wordPattern()        
obj.wordPattern(pattern,str1)

def longest_common_prefix(strs):
    """Find the longest common prefix in a list of strings"""
    prefix = ''
    #max_len = 0
    str1 = strs[0]
    for i in range (len(str1)):
        for s in strs[1::]:
            if i == len(s) or str1[i] != s[i]:
                return prefix
        prefix = prefix+s[i]
    return prefix   

def str_substr_first_occurrence(s,substr):
    """ Find the Index of the First Occurrence in a String"""
    for i in range(len(s)-len(substr)+1):
        if s[i:i+len(substr)] == substr:
            return i
    return -1    

def shortest_uncommon_substring(arr):
    """Shortest Uncommon Substring in an Array"""    
    def get_substring(s):
        """find all the substring of the given string"""
        sub_str=list()
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub_str.append(s[i:j])
        return list(set(sub_str))
    
    def uncommon_substr(arr):
        all_substr = list()
        for s in arr:
            all_substr = all_substr+get_substring(s)
        
        sub_str_count = {i:all_substr.count(i) for i in all_substr}
    uncommon_substr(arr)

def generateParenthesis(n):
    """Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""
    def backtrack(s='',openp=0,closep=0):
        if openp==closep==n:
            return ans.append(s)
        
        if openp < n:
            backtrack(s+'(',openp+1,closep)
        if closep < openp:
            backtrack(s+')',openp,closep+1)
        
    ans=[]
    backtrack()
    return ans   

##function Call    
print(generateParenthesis(3))   

def valid_parentheses_pair(s):
    """valid Parentheses in a string"""
    stk = []
    dec = {')':'(',']':'[','}':'{'}
    for i in s:
        if i in dec.values() :
            stk.append(i)
        elif stk and dec[i]==stk[-1]:
            stk.pop()
        else:
            return False
    if stk == []:
        return True
    else:
        return False

def str_str(s, sub):
    """Find the Index of the First Occurrence in a String"""
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)] == sub:
           return i
    return -1

## OPTION 1
def are_anagrams(s1, s2):
    """Checks if two strings are anagrams."""
    def dec_count(s):
        dec = {}
        for i in s:
            dec[i] = dec.get(i,0)+1
        return dec    

    def anagram(s1,s2):
        dec1 = {}
        dec2={}
        if len(s1) != len(s2):
            return False
        dec1=dec_count(s1)
        dec2=dec_count(s2)
        if  dec1 == dec2:
            print("strings are anagram")
        else:
            print("Strings are not anagram")
    anagram(s1,s2)

## OPTION 2  
from collections import Counter
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    if Counter(s1.lower()) == Counter(s2.lower()):
        return True          

#are_anagrams(s1, s2)

##option 1
def numberOfSpecialChars(word):
    """You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
        Return the number of special letters in word.
        https://leetcode.com/problems/count-the-number-of-special-characters-i/description/
    """
    lower=set()
    upper = set()
    for i in word:
        if i.islower():
            lower.add(i)
        else:        
            upper.add(i.lower())

    return (lower & upper)

##option 2
def numberOfSpecialChars_2(s):
    #count = 0
    s=set(s)
    track = []
    for i in s:
        if i.islower() and  i.lower() not in track and i.upper() in s :
            print(i)
            track.append(i.lower())
        if i.isupper() and i.lower() not in track and  i.lower() in s:   
            print(i)
            track.append(i.lower())
    print(track)        
    count = len(track)            
    return count 

#import string

#s="AbBCab"
def numberOfSpecialChars(s):
    """ 3121:Count the Number of Special Characters II :
    You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, 
    and every lowercase occurrence of 'c' appears before the first uppercase occurrence of 'c'.
    Return the number of special letters in word.
    https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/
    """
    ch_lower={}
    ch_upper={}
    count = 0
    for indx,ch in enumerate(s):
        #print(ch)
        if ch.isupper():
            if ch.lower() not in ch_upper:
                ch_upper[ch.lower()]=indx
        elif ch.islower() and s.rfind(ch) != -1 and ch.lower() not in ch_lower:
            ch_lower[ch.lower()] = s.rfind(ch)

    for k in ch_lower.keys():
        if k in ch_upper.keys():
            if ch_lower[k] < ch_upper[k]:
                count +=1
    return count 

## OPTION2
def numberOfSpecialChars2(word):
    track_lower={}
    track_upper={}
    count=0
    for i,ch in enumerate(word):
        if ch.islower() and ch.upper() in word :
            track_lower[ch.lower()]=i
        if ch.isupper() and ch.lower() in word and ch.lower() not in track_upper:
            track_upper[ch.lower()]=i
            
    for i in track_lower:
        if int(track_lower[i]) < int(track_upper[i]):
            count+=1
    return count    

def find_substr_recursively_in_order(s,sub):
    """
    Nutanix:ques
    Get the number of occurrence of sub string in full string, when the sub string character coming in same order.
    string = ‘qasetfghoertypdfgvstsdsgstsdvxcvodsfdhdosdfsdfstadsaoasdadpasdasd’
    substring = ‘top’
 
    To this above example : we are looking of `t` at the string. Once we get the `t` next search will be for `o` and then `p`.
    Once we identified `t` then we will only look for `o`, in-case `t` or `p` comes then start searching `t` again.
    Similar to this once `o` comes the `t` and `o` is invalid.
    """
    ch = ''
    for i,c in enumerate(s):
        if s[i] in sub:
            ch = ch +s[i]
            
    print(ch) #removes all the leters from 's' other the letters present in 'sub' in a order  output: totttootop
    print(ch.count(sub))   # count how mane times 'sub' string occures in 'ch' output : 1
    return ch.count(sub)  

def countPrefixSuffixPairs(arr):
    """ 3042. Count Prefix and Suffix Pairs I:-
    Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
    isPrefixAndSuffix(str1, str2) returns true if str1 is both a 
    prefix and a suffix of str2, and false otherwise.
    For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, 
    but isPrefixAndSuffix("abc", "abcd") is false.
    Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.
    the can have no of string but the str1 index should be less then str2 index and return the answer as no of such pair
    Input: words = ["pa","papa","ma","mama"]
Output: 2
Explanation: In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("pa", "papa") is true.
i = 2 and j = 3 because isPrefixAndSuffix("ma", "mama") is true.
Therefore, the answer is 2.  
    """
    count=0
    for i,ch in enumerate(arr):
        for j in arr[(i+1):]:
            if j.startswith(ch) and j.endswith(ch):
                count+=1
    return count 

def firstUniqChar(s):
    """Given a string s, find the first non-repeating character in it and return its index.
      If it does not exist, return -1.
    """
    for i,ch in enumerate(s):
        if s.count(ch) == 1:
            return i
    return "-1"        

class Solution_commonChars:
    from collections import Counter
    def commonChars(self, words):
        
        """Given a string array words, return an array of all characters that show up in all strings within the words 
        (including duplicates). You may return the answer in any order.
        :type words: List[str]
        :rtype: List[str]
        """
        ans =[]
        count = Counter(words[0])
        for word in words[1::]:
            count = count & Counter(word)
        print(count)
        for ch,count in count.items():
            ans.extend([ch] * count)  
        return ans    

##function Call    
words = ["bella", "label", "roller"]
c = Solution_commonChars()
print(c.commonChars(words))  # Output: ['e', 'l', 'l']

def custom_sort_string(order, s):
    """
    You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically, 
if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.
Example 1:
Input:  order = "cba", s = "abcd" 
Output:  "cbad" 
Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
    """
    order_map = {ch:i for i,ch in enumerate(order)}
    print(order_map)
    # 'sorted' will iterated 'x' variable over 's' .  key parameter specifies a function that is called on each element 
    #executes the lambda Function to  decide the order and . Default is None
    #order_map.get(x, len(order)) fetches the index of x from the order_map dictionary.
    #If x is not found in order_map, it returns len(order).
    sorted_s = sorted(s,key=lambda x: order_map.get(x, len(order)))
    
     
    print(sorted_s)
    return ''.join(sorted_s)
           
order = "cba"
s = "abcd"
print("Permuted string:", custom_sort_string(order, s))

def reverseStr(s, k):
    """
    Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
    If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
    then reverse the first k characters and leave the other as original.
    EX:
    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"
    """
    new_str = ''
    i = 0
    while i < len(s):
        s1=s[i:i+k]
        new_str=new_str+s1[::-1]+s[i+k:i+2*k]
        i = i+2*k
     
    return new_str 
          
s = "abcdefg" 
s = "abcd"
k = 2   
print(reverseStr(s, k))



#words = ["bella","label","roller"]        
#obj = Solution_commonChars()  
#print(obj.commonChars(words) )  


#suit()
#list_to_dect(l1,l2)
#print(count_substring_occurrences("geegsforgeegs","gee") )    
#words = ["a","aa","aaa","aaaa"]
#words = ["a","ab","abc","d","cd","bcd","abcd"]
#print(max_product(words))   
#strs = ["flower","flow","flight"]
#print(longest_common_prefix(strs)) 
#s = "leetcode"
#substr = "leet"
#print(str_substr_first_occurrence(s,substr))
#arr=["abc","bcd","abcd"]
#print(shortest_uncommon_substring(arr))
#print(generateParenthesis(3))
s = "aaBAbcBC"        
print(numberOfSpecialChars(s))  
s='qasetfghoertypdfgvstsdsgstsdvxcvodsfdhdosdfsdfstadsaoasdadpasdasdtyop'
sub = 'top'
print(find_substr_recursively_in_order(s,sub)) 
s="abacbad"        
print(firstUniqChar(s))

words = ["bella","label","roller"]        
obj = Solution_commonChars()  
print(obj.commonChars(words) )  


