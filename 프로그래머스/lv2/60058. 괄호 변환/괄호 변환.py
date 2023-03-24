from collections import deque
def div(s):
    open_p = 0
    close_p = 0

    for i in range(len(s)):
        if s[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return s[:i + 1], s[i + 1:]

def bal(s):
    list_s = list(s)

    if list_s.count('(') == list_s.count(')'):
        return True
    else:
        return False

def right(s):

    stack = []

    for char in s:
        if not stack:
            if char == ')':
                return False
            else:
                stack.append(char)
                continue

        if stack[-1]=='(' and char == ')':
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        return True
    else:
        return False

def solution(p):
    answer = ''

    if p=='':
        answer = ''
        return answer

    if right(p):
        return p

    u,v = div(p)

    if right(u):
        return u+solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for i in u[1:len(u)-1]:

            if i=='(':
                answer += ')'
            else:
                answer += '('


        return answer