import httpx
import time
import asyncio
import glob

import os
os.chdir('..')

async def runpost(image):
    async with httpx.AsyncClient() as client:
        results = await client.post(
            'http://localhost:8000/image', 
            files={'file': open(image, 'rb')}, timeout=None
        )
            
    return results.json()

async def get_all(images):
    requests = []
    for image in images:
        requests.append(runpost(image))
        
    results = await asyncio.gather(*requests)
    return results

if __name__ == "__main__":
    start_time = time.time()
    images = glob.glob('data/test/**/*.jpg', recursive=True)
    asyncio.run(get_all(images))
    end_time = time.time() - start_time

    print('Took: {} for: {} images'.format(round(end_time, 4), len(images)))