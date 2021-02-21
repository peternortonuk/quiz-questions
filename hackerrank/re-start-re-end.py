import re

string = 'jjhv'
text = 'z'
expected = (-1, -1)

string = 'aaadaa'
text = 'aa'

text_length = len(text)

# use a zero-length search with a look-ahead search
# to solve requirement for all overlapping results
# also note combination of f strings and r strings
pattern = fr'(?=({text}))'
results = re.finditer(pattern, string)

# butchery for required results
results = [result.span() for result in results]
if results:
    results = [(result[0], result[0] + text_length - 1) for result in results]
else:
    results = [(-1, -1)]

for result in results:
    print(result)


