import asyncio
import mcsrvstat
import argparse

servers_to_check = [
    'htc11221.mcskill.net',
    'htc11222.mcskill.net',
    'htc11223.mcskill.net',
    'htc11224.mcskill.net',
    'htc11225.mcskill.net',
    'htc11226.mcskill.net',
    'htc11227.mcskill.net',
    'htc11228.mcskill.net'
]

async def check_servers(server_index=None):
    if server_index is not None:
        if server_index < 1 or server_index > len(servers_to_check):
            print("Invalid server index")
            return

        index = server_index - 1
        address = servers_to_check[index]
        servers_to_check_filtered = [address]
    else:
        servers_to_check_filtered = servers_to_check
    
    print('$${')
    for index, address in enumerate(servers_to_check_filtered):
        server = mcsrvstat.Server(address=address)
        if await server.is_online:
            players = await server.get_players()
            for player in players:
                formatted_message = f'/m {player.name} Привет, как у тебя дела?'
                print(f'echo({formatted_message});')
        else:
            print(f"Server [{index + 1}] {address} not found online.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a message for Minecraft players on a specific server.")
    parser.add_argument("server_index", type=int, nargs='?', default=None, help="Index of the server to check (1-8)")

    args = parser.parse_args()
    asyncio.run(check_servers(args.server_index))
    print('}$$')
