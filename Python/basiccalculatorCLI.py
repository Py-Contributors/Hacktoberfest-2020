import argparse
import numpy as np

def checktohex(myArgs):
    return True if len(myArgs) == 1 else False

def handleSum(myArgs):
    print(sum(myArgs))

def handleMul(myArgs):
    print(np.prod(myArgs))

def handleSub(myArgs):
    print(myArgs[0] - myArgs[1])

def handleDiv(myArgs):
    print(myArgs[0] / myArgs[1])

def dectohex(myArgs):
    d2h_table = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    decnum = myArgs[0]
    if checktohex(myArgs):
        cont_div  = True
        hexa = ''
        while cont_div:
            divis = int(decnum / 16)
            rem = decnum % 16
            if divis != 0:
                hexa = d2h_table[rem] + hexa
                decnum = divis
            elif divis == 0:
                hexa = d2h_table[rem] + hexa
                break
        print(f'0x{hexa}')
    else:
        print(f'Please provide only 1 decimal to convert to hex. Not mulitple deicmals.')

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='action', action='store_const',
                    const=handleSum, 
                    help='sum the integers (default: find the max)')

parser.add_argument('--mul', dest='action', action='store_const',
                    const=handleMul, 
                    help='multiply the integers (default: find the max)')

parser.add_argument('--div', dest='action', action='store_const',
                    const=handleDiv, 
                    help='divide the integers (default: find the max)')

parser.add_argument('--sub', dest='action', action='store_const',
                    const=handleSub, 
                    help='subtract the integers (default: find the max)')

parser.add_argument('--tohex', dest='action', action='store_const',
                    const=dectohex, 
                    help='change decimals to integer (default: find the max)')


args = parser.parse_args()

if args.action is None:
    parser.parse_args(['-h'])
args.action(args.integers)