import asyncio # Asynchronous

# Synchronous: đồng bộ ~ normal program
# Asynchronous: không đồng bộ 

async def main_test():
    print('Wait 2 seconds')
    # To execute this function, we need await command 
    await sub_func() # await need to be inside the async function
    print('Finished')

async def sub_func():
    print('Sub-function is executed')
    await asyncio.sleep(2)

print(main_test) # This function is an object

asyncio.run(main_test()) # -> create an event loop

async def main():
    print('Program start to run!')
    print('Program wait to')
    
    
    
    