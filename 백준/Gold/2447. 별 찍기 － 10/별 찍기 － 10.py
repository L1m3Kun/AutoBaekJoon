def stars(n):
    if n == 1:
        # if input number is 1, returns just 1 star
        return ['*']
    # multi of 3 makes stars list
    num = n // 3
    # save func activation before as s
    s = stars(num)

    # makes new list for result
    star =[]
    # first line
    # saved stars * 3 append in star list
    for i in s:
        star.append(i*3)
    # second line
    # it takes blank in middle so append blanks as divided 3 instead of star lists
    for i in s:
        star.append(i + " " * num + i)

    # las line is equals first line
    for i in s:
        star.append(i*3)

    # return star list made of star lists
    return star

# input
N = int(input())

# for removing list symbol([])
s = stars(N)
for i in s:
    print(i)