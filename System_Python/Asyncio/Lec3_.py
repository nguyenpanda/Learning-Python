import asyncio

async def userInput():
    name = str(input('Enter your name: '))
    return name

async def phoneProcessing():
    print('App is being built')
    for i in range(101):
        print(f'{i}%')
        await asyncio.sleep(0.1)
        
async def main():
    task1 = asyncio.create_task(userInput())
    task2 = asyncio.create_task(phoneProcessing())
    
    userName = await task1
    
    await task2  # Wait for phoneProcessing task to complete
    
    print('Finished!')
    print(f'User name is {userName}')
    
asyncio.run(main())
