def swapFile(a,b):
   data1=open(a,"r")
   data2=open(b,"r")
   data1.write(data2.readlines())
   data2.write(data1.readlines())
   print("your file has been swapped")
   print(a,":", data1)
   print(b,":",data2)
file1=input("Enter a file")
file2=input("Enter another file")
swapFile(file1,file2)
   
   
