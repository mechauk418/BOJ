def solution(s):
    answer = []
    for string in s:
        count, idx, stack = 0, 0, ""
        while idx < len(string):            # 110 찾기
            if string[idx] == "0" and stack[-2:] == "11":
                stack = stack[:-2]
                count += 1
            else:
                stack += string[idx]
            idx += 1

        idx = stack.find("111")
        if idx == -1:
            idx = stack.rfind('0')
            stack = stack[:idx+1]+"110"*count+stack[idx+1:]
        else: 
            stack = stack[:idx]+"110"*count+stack[idx:]
        answer.append(stack)
    return answer