"""

https://hackerrank-challenge-pdfs.s3.amazonaws.com/22936-counting-valleys-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1542637679&Signature=3fOgG6opECf6ZhC%2FhNbwcfCiL7Y%3D&response-content-disposition=inline%3B%20filename%3Dcounting-valleys-English.pdf&response-content-type=application%2Fpdf

"""

n = int(input())
s = input().lower()
L, V = 0, 0
for i in s:
    if i == 'u':
        L += 1
        if L == 0:
            V += 1
    else:
        L -= 1
print(V)

