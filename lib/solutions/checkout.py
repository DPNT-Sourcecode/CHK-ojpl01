

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):

    sum_ = 0
    my_dict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

    for item in skus:
        if item == "A":
            my_dict.update({item: my_dict[item] + 1})
        elif item == "B":
            my_dict.update({item: my_dict[item] + 1})
        elif item == "C":
            my_dict.update({item: my_dict[item] + 1})
        elif item == "D":
            my_dict.update({item: my_dict[item] + 1})
        elif item == "E":
            my_dict.update({item: my_dict[item] + 1})
        elif item == "A":
            my_dict.update({item: my_dict[item] + 1})
        elif item == "B":
            my_dict.update({item: my_dict[item] + 1})
        elif item == "E":
            my_dict.update({item: my_dict[item] + 1})
        else:
            return -1

    for k, v in my_dict.items():
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
            if single_b >= 1 and two_e:
                if single_b > two_e:
                    sum_ -= two_e * 30
                elif single_b <= two_e:
                    sum_ -= single_b * 30

    return int(sum_)
