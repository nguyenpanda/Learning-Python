import asyncio

async def some_async_function():
    await asyncio.sleep(1)
    return "Done"

async def main():
    task = asyncio.create_task(some_async_function())
    # Thực hiện các công việc khác trong khi task đang chạy không đồng bộ
    print("Task is running in the background")
    result = await task # Wait until the task finishes before executing the following command, which is `print("Task result:", result)`
    print("Task result:", result) # if the command is executed, the main() function will end

# Chạy hàm main
asyncio.run(main())
