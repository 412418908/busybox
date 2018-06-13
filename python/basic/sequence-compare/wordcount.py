#word counter using regex
import re
while True:
    string =raw_input("Enter the string: ")
    count = len(re.findall("[a-zA-Z_]+", string))
    if line == "Done": #command to terminate the loop
        break
    print (count)
print ("Terminated")

[a-zA-Z_][a-zA-Z_0-9]+

> line = line.split('//')[0]
>>> result = re.sub(r'[a-zA-Z_][a-zA-Z_0-9]+', 'A', line)
>>> result
'A (i=0; i<10;i++){ A A '
>>> result2 = re.sub(r'\s+', 'A', result)
>>> result2
'AA(i=0;Ai<10;i++){AAAAA'
