from math import ceil,log2
def getmid(ss,se):
    return ss+(se-ss)//2

def getsumutil(st,ss,se,qs,qe,si):
    if(qs<=ss and qe>=se):
        return st[si]
    if(qe<ss or qs>se):
        return 0
    mid=getmid(ss,se)
    return getsumutil(st,ss,mid,qs,qe,2*si+1)+getsumutil(st,mid+1,se,qs,qe,2*si+2)

def getsum(st,n,qs,qe):
    if(qs<0 or qe>n-1 or qs>qe):
        print("Invalid query")
        return -1
    return getsumutil(st,0,n-1,qs,qe,0)

def constructSTutil(arr,ss,se,st,si):
    if(ss==se):
        st[si]=arr[ss]
        return arr[ss]
    mid=getmid(ss,se)
    st[si]=constructSTutil(arr,ss,mid,st,2*si+1)+constructSTutil(arr,mid+1,se,st,2*si+2)
    return st[si]

def updatevalueUtil(st,ss,se,index,diff,si):
    if(index<ss or index>se):
        return
    st[si]=st[si]+diff
    if(se!=ss):
        mid=getmid(ss,se)
        updatevalueUtil(st,ss,mid,index,diff,2*si+1)
        updatevalueUtil(st,mid+1,se,index,diff,2*si+2)


def updatevalue(arr,n,st,i,data):
    if(i<0 or i>n-1):
        print("Invalid Index")
        return -1
    diff=data-arr[i]
    arr[i]=data
    updatevalueUtil(st,0,n-1,i,diff,0)


def constructST(arr,n):
    height=(int)(ceil(log2(n)))
    length=2*(int)(2**height)-1
    st=[0]*length
    constructSTutil(arr,0,n-1,st,0)
    return st



print("Enter size of array")
n=int(input())
print("Enter each element of array")
arr=list(map(int,input().split()))
segment_tree=constructST(arr,n) #ST -> Segment Tree
while True:
    option=int(input())
    if(option==0):
        break
    elif(option==1):
        data,index=map(int,input().split())
        updatevalue(arr,n,segment_tree,index,data)
    elif(option==2):
        L,R=map(int,input().split())
        ans=getsum(segment_tree,n,L,R)
        print(ans)
    else:
        print("Wrong option")
        break
