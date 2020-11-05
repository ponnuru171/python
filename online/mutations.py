old_string="abdd"
string_list = list(old_string)
string_list[2] = "c"
new_string = "".join(string_list)
print(new_string)