import sys
start,end = int(sys.argv[1]),int(sys.argv[2])
for i in range(start,end + 1):
  print("git add sequences/%03d/*.lzo; git commit sequences/%03d/*.lzo -m 'A%03d000 to A%03d999'" % (i, i, i, i))
  if i % 10 == 0:
    print("git push")
print("git push")
