import re
p = re.compile('ca.e')

# . : 하나의 문자를 의미
# ^ : 문자열의 시작 ^de  de로 시작함
# & : 문자열의 끝 se&  se로 끝남


def print_match(m):
    if m:
        print(m.group())
        print(m.string)
        print(m.start())
        print(m.end())
        print(m.span())
    else:
        print('매칭되지 않음')


# m = p.match('casdfse')
# print_match(m)

# m = p.search('good care')
# print_match(m)

m = p.findall('good care cafe')
print(m)
