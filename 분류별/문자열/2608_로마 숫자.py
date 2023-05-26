def change_num(s):
    cnt = 0
    i = 0
    while i < len(s):
        if s[i:i+2] in alpha_dict:
            cnt += alpha_dict[s[i:i+2]]
            i += 2
        else:
            cnt += alpha_dict[s[i]]
            i += 1

    return cnt


def change_str(num):
    result = ''
    idx = 0
    alpha_list = list(alpha_dict.keys())
    while num > 0:
        n = num//alpha_dict[alpha_list[idx]]
        num -= n*alpha_dict[alpha_list[idx]]
        result += alpha_list[idx] * n
        idx += 1

    return result


answer = 0
alpha_dict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100,
             'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}

for _ in range(2):
    answer += change_num(input())
print(answer)
print(change_str(answer))