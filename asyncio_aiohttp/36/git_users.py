import asyncio
from aiohttp import ClientSession


async def get_repos(user):
    async with ClientSession() as session:
        url = f"https://api.github.com/users/{user}/repos"
        async with session.get(url=url) as response:
            data_json = await response.json()
            result = []
            for element in data_json:
                result.append(element['full_name'])
            print(f'{user}: {result}')
        

async def main(users_):
    tasks = []
    for user in users_:
        tasks.append(asyncio.create_task(get_repos(user)))

    for task in tasks:
        await task


users = ["Arantir1", "EgorTimofeychik", "maximax15", "letov2110", "denirix", "Noowkies", "NikDychek", "marinamonit",
         "PolonskyIllya", "temabuchka88", "LuydmilaKot", "katherinepcholka", "telenchenkosergey"]


asyncio.run(main(users))




















