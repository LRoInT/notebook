import re

get_word=re.compile("[a-zA-Z]")
print(get_word.match("Asfsdfsf4234324").group())