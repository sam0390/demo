def TOH(n,s,d,a):
    if n==1:
        print ("Move disk 1 from Source",s,"to Destination",d)
        return
    TOH(n-1, s, a, d)
    print ("Move disk",n,"from Source",s,"to Destination",d)
    TOH(n-1, a, d, s)  
n=int(input("Enter no. of Disks :- "))
TOH(n,'S','D','A')
