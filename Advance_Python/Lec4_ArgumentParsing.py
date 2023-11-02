import sys
import getopt  # allow us to use '-o', '-p' command
''' -o:
Được sử dụng để chỉ định một tệp đầu ra (output file).
Nếu bạn muốn ghi kết quả của một lệnh vào một tệp,
bạn có thể sử dụng -o để chỉ định tên của tệp đó'''
''' -p:
Được sử dụng để chỉ định một cổng (port).
Điều này thường được sử dụng trong ngữ cảnh liên quan đến mạng
hoặc kết nối tới các dịch vụ mạng cụ thể trên máy chủ hoặc máy tính.
'''

def Lec4_argv():
    """
    -argv: argument vector -> return a list containing command
    -command: python3 Lec4_ArgumentParsing.py Test
              sys.argv[0] -> Lec4_ArgumentParsing.py
              sys.argv[0] -> Test
    """
    print(sys.argv[0])
    print(sys.argv[1])

def write_text_to_file():
    """
    Write text to a file using this command:
    """
    filename = sys.argv[1]
    message = str(sys.argv[2])

    with open(filename, 'w+') as file:
        file.write(message)
        
# write_text_to_file()

def take_command_option():
    opts, args = getopt.getopt(sys.argv[1:], 'f:m:', ['filename', 'message'])
    """
    @getopt.getopt(sys.argv[1:], 'f:m:', ['filename', 'message']) -> tuple[list[tuple[str, str]], list[str]]
            after colon, expect something after that
    @Argument:
        - Index 0: sys.argv[1:] -> Take the second command to the last command
        - Index 1: 'f:m:' -> command 'f' and 'm'
        - Index 2: ['filename', 'message'] ->
    @Example:
    - python3 Lec4_ArgumentParsing.py -f TestLec4.txt "Hello World"
        -> Options: [('-f', 'TestLec4.txt')]
        -> Arguments: ['Hello World']
    - python3 Lec4_ArgumentParsing.py -f TestLec4.txt -m "Hello World"
        -> Options: [('-f', 'TestLec4.txt'), ('-m', 'Hello World')]
        -> Arguments: []
    - python3 Lec4_ArgumentParsing.py -f  TestLec4.txt -m "Hello World" HaTuongNguyen
        -> Options: [('-f', 'TestLec4.txt'), ('-m', 'Hello World')]
        -> Arguments: ['HaTuongNguyen']
    """
    print(f'Options: {opts}')
    print(f'Arguments: {args}')
    return opts, args

take_command_option()

def main():
    filename = 'Lec4_defaultOutput.txt'
    message = 'Empty message'
    
    # python3 Lec4_ArgumentParsing.py -f  Lec4_Test.txt -m "Hello World! My name is Nguyen"
    opts, args = getopt.getopt(sys.argv[1:], 'f:m:', ['filename', 'message'])

    for opt, arg in opts:
        if opt == '-f':
            filename = arg
        elif opt == '-m':
            message = arg
        else:
            raise TypeError('Some thing is wrong')
        
    with open(filename, 'w+') as file:
        file.write(message)

main()
