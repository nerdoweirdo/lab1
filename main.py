import re

with open('input.txt', 'r') as data:
    for s in data:
        s = data.readline()
        if re.match(r'^(((\+7|8)(([\- ]?(\(?\d{3}\)?)[\- ]?)))|(((\(?9\d{2}\)?)[\- ]?)))(\d{3}[\- ]?\d{2}[\- ]?\d{2})$', s):
            with open('output.txt', 'a') as result:
                result.write(s)
