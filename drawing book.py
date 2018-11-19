"""

https://hackerrank-challenge-pdfs.s3.amazonaws.com/22564-drawing-book-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1542635823&Signature=n51gi7h0dMPuezgZAILUoVo6e4k%3D&response-content-disposition=inline%3B%20filename%3Ddrawing-book-English.pdf&response-content-type=application%2Fpdf

"""

import sys

n = int(input())
p = int(input())
half_book = p//2
pages_between = (n//2) - (p//2)
print(min(half_book, pages_between))