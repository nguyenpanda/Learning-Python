def find_string_2():
    main_string = input("Enter your string: ")
    key_string = input("Enter the string you want to find: ")
    contain = []

    if (key_string in main_string) == True:
        first = main_string.find(key_string)
        contain.append(first)

        for i in range(len(main_string)):
            first = main_string.find(key_string, first + 1)
            contain.append(first)

            if first == -1:
                contain.pop()
                break

        print(f'Có {len(contain)} ký tự \"{key_string}\" \nVị trị của \"{key_string}\" bắt đầu từ 0 được sắp xếp trong list như sau:')
        print("->", contain)

    else:
        print('Ko có thấy má ơi')

find_string_2()


