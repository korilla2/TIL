'''
6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)

1.7 MB
'''

h, b, c, s = map(int, input().split())

result = (h * b * c * s) / 8 / 1024 / 1024

print(f'{result:.1f} MB')
