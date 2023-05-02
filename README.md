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

#### This script is provided as-is, without warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of the script is with you. Should the script prove defective, you assume the cost of all necessary servicing, repair or correction.

#### In no event, unless required by applicable law or agreed to in writing, shall the author be liable to you for damages, including any general, special, incidental or consequential damages arising out of the use or inability to use the script (including but not limited to loss of data or data being rendered inaccurate or losses sustained by you or third parties or a failure of the script to operate with any other programs), even if the author has been advised of the possibility of such damages.

#### By using this script, you agree to the terms of this disclaimer.
