## Sliding window problems

s1="GEEKSFORGEEKS"

def check_str_not_invalide(s):
    if len(s) == 0 :
        return False
    else:
        return s
            
def check_lowercase(s):
    if s.islower:
        return s
    else:
        return s.lower()

def longest_substring(s):
    """This method finds the length of longest substring os the given substring"""

    substring = ''
    max_len = 0
    
    for i in s:
        if i not in substring:
            substring = substring +i
            max_len = max(max_len,len(substring))

        else:
            substring = substring.split(i)[1]+i    

    return  max_len      

#print(longest_substring(s1))

def get_min_string(s):
    """Find the smallest substring that contains all of the unique characters of the string"""
    min_len = len(s)
    sub_str = ''
    unique_ch = set(s)
    print("length of unique chr :", len(unique_ch))

    for i in range(len(s)-len(unique_ch)+1):
        for j in range(i+len(unique_ch),len(s)+1):
            windows = s[i:j]
            if all(ch in windows for ch in unique_ch):
                if len(windows) < min_len :
                    sub_str = windows
                    min_len = len(windows)
    
   
    return  sub_str, min_len   

def longest_substring_of_k_disting_char(s,k):
    """Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters."""
    sub_str = ''
    max_len = 0
    s=check_str_not_invalide(s)

    for i in range(len(s)-k+1):
        for j in range(i+k,len(s)):
            windows = s[i:j]
            if len(set(windows)) == k:
               if len(windows) > max_len:
                max_len = len(windows)
                sub_str = windows
    return sub_str , max_len

def get_min_string_of_pattern(s,pt):
    """Get the smallest window in a string containing all characters of given pattern"""
    s=check_str_not_invalide(s)
    min_len = len(s)
    sub_str = ''
    for i in range(len(s)):
        for j in range(i+len(pt),len(s)):
            windows = s[i:j]
            if all(ch in windows for ch in pt):
                if len(windows) < min_len:
                    min_len = len(windows)
                    sub_str = windows
    return  sub_str, min_len              


#print(get_min_string(s1))  
#print(longest_substring_of_k_disting_char(s1,3))       
print(get_min_string_of_pattern("figehaeci", 'aei'))
