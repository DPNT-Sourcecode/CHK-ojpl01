

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):

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

    sum_ = 0
    single_b = 0
    print(my_dict)
    for k, v in my_dict.items():
        print("k: ", k)
        print("sum: ", sum_)
        if k == "A":
            print("HEre")
            if my_dict[k] >= 5:
                fivers = my_dict[k] // 5
                sum_ += fivers * 200

            if (my_dict[k] - (my_dict[k] // 5)) >= 3:
                sum_ += (my_dict[k] // 3) * 130

            print(((my_dict[k] // 5) * 5) - ((my_dict[k] // 3) * 3))
            sum_ += (my_dict[k] - ((my_dict[k] // 5) * 5) - ((my_dict[k] // 3) * 3)) * 50
            print(sum_)
        if k == "B":
            if my_dict[k] >= 2:
                twos = my_dict[k] // 2
                sum_ += twos * 45
                single_b = my_dict[k] - (twos * 2)

            sum_ += (my_dict[k] - ((my_dict[k] // 2) * 2)) * 30

        if k == "C":
            sum_ += my_dict[k] * 20

        if k == "D":
            sum_ += my_dict[k] * 15

        if k == "E":
            sum_ = my_dict[k] * 40
            two_e = my_dict[k] // 2
            if single_b >= 1 and two_e:
                if single_b > two_e:
                    sum_ -= two_e * 30
                elif single_b <= two_e:
                    sum_ -= single_b * 30

    print("sum: ", sum_)
    return int(sum_)


checkout("AAA")
