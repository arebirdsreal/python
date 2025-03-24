# to return string from function, use formatted return : return f"{paramter1}, {parameter2}""

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name}, {formated_l_name}"
print(format_name('nilay', 'adkonkar'))