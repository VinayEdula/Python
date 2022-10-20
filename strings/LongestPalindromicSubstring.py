
'''
Algorithm:
1.	Maintain a variable ‘ longest_length = 1 ‘ (for storing longest palindromic substring length) and ‘ start =0 ‘ (for storing index of longest palindromic substring length).
2.	The idea is very simple, we will traverse through the entire string with i=0 to i<(length of string) while traversing, initialize ‘start‘ and ‘end‘ pointer such that start= i-1 and end= i+1.
3.	keep incrementing ‘end’ until str[end]==str[i]  similarly keep decrementing ‘start’ until str[start]==str[i].
4.	Finally we will keep incrementing ‘end’ and decrementing ‘start’ until str[start]==str[end].
5.	calculate length=end-start-1, if length > longest_length then longest_length = length and start = start+1 .
6.	Print the longest palindromic substring and return longest_length.
'''

def longestPalindromicSubstring(string: str) -> int:
    ''' if the given string is empty then size will be 0.
    if length==1 then, answer will be 1(single character will always be a palindrome) '''
    length = len(string)  # calculating the length of string
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
    print("Length of Longest Palindromic Substring is: " + str(longestPalindromicSubstring("hacktoberfest")))
    print("Length of Longest Palindromic Substring is: " + str(longestPalindromicSubstring("malayalam")))



#This program takes time complexity to find the longest palindromic substring
#This program takes O(1) space complexity to find the longest palindromic substring
