def longestPalindromicSubstring(string: str) -> int:
    length = len(string)  # calculating size of string
 # if the given string is empty then size will be 0 and if length==1 then, answer will be 1(single character will always be a palindrome)
    if (length < 2):
        return length 
    start = 0
    longest_length = 1
    for i in range(length):
        start = i - 1
        end = i + 1
        while (end < length and string[end] == string[i]):
            end = end + 1
        while (start >= 0 and string[start] == string[i]):
            start = start - 1
        while (start >= 0 and end < length and string[start] == string[end]):
            start = start - 1
            end = end + 1
        curr_length = end - start - 1
        if (longest_length < curr_length):
            longest_length = curr_length
            start = start + 1
    print("Longest possible palindromic substring is:", end=" ")
    print(string[start:start + longest_length])
    return longest_length

if __name__ == "__main__":
    print("Length of Longest Palindromic Substring is: " + str(longestPalindromicSubstring("thealgorithms")))

#This program takes time complexity to find the longest palindromic substring
#This program takes O(1) space complexity to find the longest palindromic substring

