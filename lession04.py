# trim()函数实现
print("trim()函数实现")
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

# datetime计算时间差
print("-------------------------------------------------------------------------")
print("datetime计算时间差")
from datetime import datetime


def friend_datetime(timestamp):
    current_time = datetime.now()
    print(datetime.strftime(current_time, "Current time: %Y-%m-%d at %H:%M %p"))
    print(datetime.strftime(timestamp, "Input time: %Y-%m-%d at %H:%M %p"))
    time_in_seconds = (current_time - timestamp).total_seconds()
    mins = int(time_in_seconds//60)
    hours = int(time_in_seconds//3600)
    days = (current_time - timestamp).days
    if days > 1:
        print(datetime.strftime(timestamp, str(days) + " days ago at %H:%M %p"))
    elif days < 1 and hours > 12:
        print(datetime.strftime(timestamp, " Today at %H:%M %p"))
    elif days < 1 and hours > 1 and hours < 12:
        print(datetime.strftime(timestamp, str(hours) + " hours ago at %H:%M %p"))
    elif days < 1 and hours < 1:
        print(datetime.strftime(timestamp, str(mins) + " minutes ago at %H:%M %p"))


timestamp = datetime(2020, 7, 1, 15, 19, 12)
friend_datetime(timestamp)
print("\n")
timestamp = datetime(2020, 8, 1, 1, 19, 12)
friend_datetime(timestamp)
print("\n")
timestamp = datetime(2020, 8, 1, 10, 19, 12)
friend_datetime(timestamp)
print("\n")
timestamp = datetime(2020, 8, 1, 15, 19, 12)
friend_datetime(timestamp)

print("-------------------------------------------------------------------------")
print("杨辉三角 生成器实现")
def generator():
    N = [1]
    while True:
        yield N
        S = N[:]
        S.append(0)
        N = [S[i-1] + S[i] for i in range(len(S))]


T = generator()
for i in range(10):
    print(next(T))
    i = i + 1

