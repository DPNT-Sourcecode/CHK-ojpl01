

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):

    sum_ = 0
    my_dict = {}

    for item in skus:
        if item == "A":
            my_dict.update({item: mydict[item]+1})
        elif item == "B":
            my_dict.update({item: mydict[item]+1})
        elif item == "C":
            my_dict.update({item: mydict[item]+1})
        elif item == "D":
            my_dict.update({item: mydict[item]+1})
        elif item == "E":
            my_dict.update({item: mydict[item]+1})
        elif item == "A" and a == 2:
            my_dict.update({item: mydict[item]+1})
        elif item == "B" and b == 1:
            my_dict.update({item: mydict[item]+1})
        elif item == "E" and e == 1:
            my_dict.update({item: mydict[item]+1})
        else:
            return -1

    offers = 0
    for k, v in my_dict:
        if k == "A":
            fivers = my_dict[k] % 5
            sum_ += fivers * 200
            threes = fivers % 3
            sum_ += threes * 130
            sum_ += (my_dict[k] - (threes * 3) - (fivers * 5)) * 50
        if k == "B":
            twos = my_dict[k] % 2
            sum_ += twos * 45
            single_b = my_dict[k] - (twos * 2)
            sum_ += (my_dict[k] - (twos * 2)) * 30
        if k == "C":
            sum_ += my_dict[k] * 20
        if k == "D":
            sum_ += my_dict[k] * 15
        if k == "E":
            sum_ = my_dict[k] * 40
            two_e = my_dict[k] % 2
            sum_ -= single_b * 30

    return int(sum_)
