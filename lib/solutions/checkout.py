

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):

    sum_ = 0
    a = 0
    b = 0
    e = 0
    for item in skus:

        if item == "A" and a != 2:
            sum_ += 50
            a += 1
        elif item == "B" and b != 1:
            sum_ += 30
            b += 1
        elif item == "C":
            sum_ += 20
        elif item == "D":
            sum_ += 15
        elif item == "E" and e != 1:
            sum_ += 40
            e += 1
        elif item == "A" and a == 2:
            sum_ += 30
            a = 0
        elif item == "B" and b == 1:
            sum_ += 15
            b = 0
        elif item == "E" and e == 1:
            sum_ -= 30
            e = 0
        else:
            return -1
    return int(sum_)
