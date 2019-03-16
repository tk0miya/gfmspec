import re


def replace(match):
    prefix, num = match.groups()
    num = int(num)
    if num >= 605:
        num += 27
    elif num >= 584:
        num += 26
    elif num >= 459:
        num += 15
    elif num >= 392:
        num += 13
    elif num >= 275:
        num += 12
    elif num >= 264:
        num += 10
    elif num >= 191:
        num += 8

    return '%s%s' % (prefix, num)


content = open('index.html').read()
content = re.sub(r'(example-|Example )(\d+)', replace, content)
open('index.html', 'w').write(content)
