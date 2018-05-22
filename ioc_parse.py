'''
Tool that takes a file as an argument and then uses regular expressions
to match common patterns for indicators of compromise (IP, hash, FQDN, etc.)
'''
# import required packages
import docx
import re

#Regex for IPs
ip4Regex = re.compile('((?:\d{1,3}\.){3}\d{1,3})')
ip6Regex = re.compile(r'((?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4})')

#Regex for hashes
md5Regex = re.compile('[a-fA-F0-9]{32}')
sha1Regex = re.compile(r'[a-fA-F0-9]{40}')
sha256Regex = re.compile(r'[a-fA-F0-9]{64}')
sha512Regex = re.compile(r'[a-fA-F0-9]{128}')

#list and string converter to handle the input text
ioc_list = []
ioc_str = ''.join(ioc_list)

#Regex for Emails
emailRegex = re.compile(r'/^([a-z0-9_\.-]+)@([\da-z\.-]\.([a-z\.]{2,6})$/')

inputfile = open('./test.txt')

# pass the text/ data contained in the file and run Regex against it
def reParse():
    for x in inputfile:
        ioc_list.append(x)
        print(ioc_list)

# take a file as an argument and open it
def getText():
    m = ip4Regex.search(ioc_str)
    for x in ioc_list:
        if m:
            print('Match Found: ', m.group())
        else:
            print('No Match')


# Create new file with only IoCs
# def newDoc():

# Run the functions
reParse()

getText()

# newDoc()

inputfile.close()
