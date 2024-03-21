#1
import re
s='abb dfab'
reg = re.compile('ab*')
result = reg.findall(s)
print(result)

#2
import re
s='abb dfabbb abbbbb'
reg = re.compile('ab{2,3}')
result = reg.findall(s)
print(result)

#3
import re

s='akskdjf alskdfj lks d d  hello_world'
reg = re.compile('[a-z]+_[a-z]+')
result = reg.findall(s)
print(result)

#4
import re
s='akskdjf Alskdfj lKs d d  hello_world'
reg = re.compile('[A-Z]+[a-z]+')
result = reg.findall(s)
print(result)

#5
import re
s='akskdjfb alskdbfj lKs d d  hello_world'
reg = re.compile('a.*b')
result = reg.findall(s)
print(result)

#6
import re
s='akskdjfb alskdbfj lKs. d d  hello_world'
modified_text = re.sub(r'[ ,.]', ':', s)
print("Modified text:", modified_text)

#7
def snake_to_camel(text):
    return ''.join(word.title() for word in text.split('_'))

snake_string = "geeksforgeeks_is_best_for_geeks"
print("Original string:", snake_string)
print("Camel case string:", snake_to_camel(snake_string))

#8
import re
s = "HelloHowAreYou Good good"
reg = re.compile('[A-Z][^A-Z]*')
result = reg.findall(s)
print(result)

#9
import re
s = "HelloHowAreYou Good good"

reg = re.sub(r"(?<=\w)([A-Z])", r" \1",s)
print(reg)

#10
import re

def camel_to_snake(s: str):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s).lower()

print(camel_to_snake("HelloHowAreYou"))