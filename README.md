![Screenshot_2023-05-02_18-37-36](https://user-images.githubusercontent.com/94005355/235803121-e06ca2cc-d4f0-42a7-87af-84c82550ce8c.png)
# FTP Brute Force Tool

This is a command-line tool for performing brute force attacks against FTP servers. It accepts a list of server addresses, usernames, and passwords and attempts to log in to each server with each combination of credentials.

# Installation

```
git clone https://github.com/DrW3b/ftp_brute.git
cd ftp_brute
pip3 install -r requirements.txt
```

# Usage

```
python ftp_brute.py [-h] (-s SINGLE_SERVER | -f SERVER_FILE) -u USERNAME_FILE -p PASSWORD_FILE
```
# Arguments

- -h, --help: Show a help message and exit.
- -s SINGLE_SERVER: A single server to target.
- -f SERVER_FILE: A file containing server addresses, one per line.
- -u USERNAME_FILE: A file containing usernames, one per line.
- -p PASSWORD_FILE: A file containing passwords, one per line.

# Example

To attempt to log in to a single server with a list of usernames and passwords, run:

```
python ftp_brute.py -s ftp.example.com -u usernames.txt -p passwords.txt
```

To attempt to log in to multiple servers with the same list of usernames and passwords, create a file `servers.txt` containing a list of server addresses, one per line, and run:

```
python ftp_brute.py -f servers.txt -u usernames.txt -p passwords.txt
```
# Legal Disclaimer: 
This script is intended for educational and/or testing purposes only. The creator of this script does not condone or support the use of this script for any illegal or unethical activities, including but not limited to attacking targets without their permission. The use of this script for any such activities is strictly prohibited and may result in legal consequences. By using this script, you agree that you will not use it for any illegal or unethical purposes, and that you will use it only for educational and/or testing purposes, with the permission of the target. The creator of this script is not responsible for any misuse or illegal use of the script.
