a = int(input())

len = 1
st = 1
cou = 9
while a > len * cou:
    a -= len * cou
    len += 1
    st *= 10
    cou *= 10
number = st + (a - 1) // len
digit_index = (a - 1) % len
print(str(number)[digit_index])