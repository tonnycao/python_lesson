# trim()函数实现
def left_trim(before_trim):
    for i, j in enumerate(before_trim):
        if j != " ":
            break
        i = i + 1
    return(before_trim[i:])


def right_trim(before_trim):
    reverse = left_trim(before_trim[::-1])
    return(reverse[::-1])


def trim_function(before_trim):
    return(right_trim(left_trim(before_trim)))

before_trim = " 6789 dsjfjdskl     "
print(trim_function(before_trim))


