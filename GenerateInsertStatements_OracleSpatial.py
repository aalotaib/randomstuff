_author__ = "Ali Alotaibi"

''' here we read from the building table, Polygon shape'''

file = open('filepath', 'r') #first table data file path
newfile = open("D:\\testnewfile.txt", "w") # path and name of the generated file
newfile.write("")    # To Make Sure the file is empty before inserting
for x in file:
  #  print x
    line = x.split(",")
    idd= line[0]
    name=line[1]
    frst=line[3]
    secnd=line[4]
    count=0
    s=""
   # print line
    for n in line:
      #  print n
        if count>2:
            if count==3:
                s= n
            else:
                s=s + "," + n
                print s
        count+=1
        print count
    s=s+","+frst+","+secnd
    insert="INSERT INTO TABLE_NAME VALUES('%s','%s', SDO_GEOMETRY( 2003,NULL,NULL,SDO_ELEM_INFO_ARRAY(1,1003,1), SDO_ORDINATE_ARRAY(%s)));" %(idd, name,s)
    #insert.format(idd,name,s,4)
    newfile.write(insert+"\n")

''' here we read from the firehydrant table, point shape'''

file = open('filepath', 'r') #second table data file path

newfile = open("filepath", "w")# path and name of the generated file
newfile.write("") # To Make Sure the file is empty before inserting
for x in file:
  #  print x
    line = x.split(",")
    idd= line[0]
    p1=line[1]
    p2=line[2]
    
    ''' to ways to insert points? '''
    
    s=s+","+frst+","+secnd
    insert="INSERT INTO TABLE_NAME VALUES('%s', SDO_GEOMETRY( 2001,NULL,  SDO_POINT_TYPE(%s, %s, NULL),NULL, NULL));" %(idd, p1,p2)
    #insert.format(idd,name,s,4)
    newfile.write(insert+"\n")




newfile.close()
file.close()
