## 1. Making a File ##

/home/dq$ touch test.txt

## 2. Understanding Standard Streams ##

/home/dq$ echo "All bears should juggle"

## 3. Redirecting Standard Streams ##

/home/dq$ echo "All bears should juggle">test.txt

## 5. Overview of File Permissions ##

/home/dq$ ls -l

## 6. Octal Notation for File Permissions ##

/home/dq$ stat test.txt

## 7. Modifying File Permissions ##

/home/dq$ chmod 0760 test.txt

## 8. Moving Files ##

/home/dq$ mv test.txt test

## 9. Copying Files ##

/home/dq$ cp test/test.txt test/test2.txt

## 11. Deleting a File ##

/home/dq/test$ rm /home/dq/test/test2.txt

## 12. Bypassing Permissions as the Root User ##

/home/dq/test$ sudo ls