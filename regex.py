import re
phone_num_pattern_object = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_object.search("My number is 123-456-7891")
print(match_obj.group())