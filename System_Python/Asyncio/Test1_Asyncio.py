import asyncio
import time

async def task1():
    await asyncio.sleep(4)
    print("Task 1 done")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 done")

async def main():
    await asyncio.gather(task1(), task2())

start = time.time()
asyncio.run(main())
end = time.time()
print(f'Completed in {end - start} second')
