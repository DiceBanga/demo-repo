# Create a functions that returns a string backwords
def solution(string):
    ans = ''
    for x in range(-1, (-1 * len(string) - 1), -1):
        ans += string[x]
    return ans


# SOLUTION
# def solution(str):
# return str[::-1]


# Tests
solution('world') == 'dlrow'
solution('hello') == 'olleh'
solution('') == ''
solution('h') == 'h'
