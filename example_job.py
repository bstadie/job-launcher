import json
import time
import argparse

import sys



def parse_job_from_json_config_dict():
    parse = argparse.Argumentarser ()
    parse.add_argument('-d', '--my-dict', type-json.loads)
    args = parse.parse_args()
    #data=json. loads (argv (1])
    mydict = args.my_dict # wilt return a dictionary
    #print (mydict)
    print ("Going to sleep")
    time.sleep (3.0)
    print ("slept 3 seconds. Sleeping again") 
    time.sleep (6.0)
    print ('ran fancy launcher') 
    print (mydict)


def parse_job_from_argparse_string():
    parser = argparse.ArgumentParser()
    # Parse the arguments
    #args, unknown_args = parse._parse_known_args()

    # Create a dictionary to store the parsed arguments
    #arg_dict = vars(args)

    #args = parser.parse_args()
    #print(' '.join(f'{k}={v}' for k, v in vars(args).items()))
    #print("FFF")
    #args = parser.parse_args()
    #print(args)
    #print("FFFFF")

    print(sys.argv[1:])




    # Print the dictionary
    #print(arg_dict)

    # Print any unknown arguments
    #print(unknown_args)

    #print (mydict)
    print ("Going to sleep")
    time.sleep (3.0)
    print ("slept 3 seconds. Sleeping again") 
    time.sleep (6.0)
    print('ran fancy launcher') 


if __name__ == "__main__":
    parse_job_from_argparse_string()