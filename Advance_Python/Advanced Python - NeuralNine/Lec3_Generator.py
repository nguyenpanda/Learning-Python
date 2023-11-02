"""
Trong Python, yield là một từ khóa được sử dụng trong việc định nghĩa một hàm generator. Hàm generator là một loại đặc biệt của hàm có khả năng tạm dừng và tiếp tục từ nơi chúng dừng lại. Khi một hàm generator được gọi, nó trả về một đối tượng generator mà bạn có thể sử dụng để lấy giá trị một cách tuần tự từ hàm mà không cần phải tải toàn bộ dữ liệu vào bộ nhớ, điều này giúp tiết kiệm tài nguyên.

Từ khóa yield được sử dụng để trả về giá trị từ hàm generator và tạm dừng việc thực thi của hàm. Khi hàm generator được gọi lần đầu tiên hoặc sau mỗi lần gọi hàm next() trên generator, hàm sẽ chạy cho đến khi gặp lệnh yield, sau đó trả về giá trị được yield và tạm dừng. Khi hàm generator được gọi lần nữa, nó sẽ tiếp tục thực thi từ chỗ dừng trước đó cho đến khi gặp lệnh yield tiếp theo hoặc kết thúc hàm.
"""
import sys

def Cube_generator(n):
    for n in range(n):
        yield n**3
def Linear_numbers(n):
    i = 0
    while i < n:
        yield i
        i += 1
def Hello(name):
    print(f'Hello {name}')
    
Cube = Cube_generator(10)

print(next(Cube))
print(next(Cube))
for x in Cube:
    print(x)

Linear_count = Linear_numbers(100000)

print(f'The size of the normal function: {sys.getsizeof(Hello)}')
print(f'The size of the Cube_generator: {sys.getsizeof(Cube)}')
print(f'The size of the Linear_numbers: {sys.getsizeof(Linear_count)}')

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
    
fibonacci_num = fibonacci_generator()

for _ in range(10):
    print(next(fibonacci_num))
