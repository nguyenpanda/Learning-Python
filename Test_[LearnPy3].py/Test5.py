def power():
    base_num = float(input("Enter your base number: "))
    power = int(input("Enter your power number: "))
    result = float(1)

    for i in range(power):
        result = result * base_num
    return result
    # print(round(result, 55))


def replace_string(phrase, phrase_contain, replace_by):
    result = ""

    for index_letter in phrase:
        if index_letter.lower() in phrase_contain:
            if index_letter.islower():
                result = result + replace_by.lower()
            else:
                result = result + replace_by.upper()
        else:
            result = result + index_letter
    return result


print(
    replace_string(input("Enter your phrase below:\n"),
                   "ueoai",
                   "a")
)
