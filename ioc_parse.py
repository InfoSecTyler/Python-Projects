'''
Tool that takes a file as an argument and then uses regular expressions
to match common patterns for indicators of compromise (IP, hash, FQDN, etc.)
'''
# import required packages
import docx
import re

#Regex for IPs
ip4Regex = re.compile(r'((?:\d{1,3}\.){3}\d{1,3})')
ip6Regex = re.compile(r'((?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4})')

#Regex for hashes
md5Regex = re.compile(r'[a-fA-F0-9]{32}')
sha1Regex = re.compile(r'[a-fA-F0-9]{40}')
sha256Regex = re.compile(r'[a-fA-F0-9]{64}')
sha512Regex = re.compile(r'[a-fA-F0-9]{128}')

#Regex for Emails
emailRegex = re.compile(r'/^([a-z0-9_\.-]+)@([\da-z\.-]\.([a-z\.]{2,6})$/')

# take a file as an argument and open it
def getText(filename):
    doc = docx.Document(filename)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)



# pass the text/ data contained in the file and run Regex against it

# Create new file with only IoCs
