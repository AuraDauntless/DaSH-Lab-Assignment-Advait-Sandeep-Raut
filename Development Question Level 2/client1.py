#Importing Libraries
import socket
import time
import json

#Creating the socket on the client end
client_socket=socket.socket()

#Taking the inputs for input and output file locations
inputfilepath=input(("Specify text file location"))
outputfilepath=input("Specify json file location")

#Defining the output list
output_list=[]

#Connecting to the previously made server
client_socket.connect(('localhost',9999))

#Reading the file in client mode
with open(inputfilepath,'r') as inputfile:
    for line in inputfile:
        if not line:
            client_socket.close()
        file_prompt=line.strip()
    
# Getting the time before the call
        Timesent=int(time.time())   

#Sending the information in the form of bytes to the connected server
        client_socket.send(bytes(inputfilepath,'utf-8'))

#Recieving The response to the input sent by the server 
        response=client_socket.recv(102444).decode()

# Getting the time after the call
        Timerecvd=int(time.time()) 
# Making the python dictionary in the given format
        formatted_output={
        "Prompt": file_prompt,
        "Message":response,
        "TimeSent":Timesent,
        "TimeRecvd":Timerecvd,
        "Source":"Gemini 1.5"
            }
        output_list.append(formatted_output)
client_socket.detach()

#converting the python dictionary to a json formatted string
jsonoutput= json.dumps(output_list,indent=4)

# Publishing the file
with open(outputfilepath,'a') as file:
    file.write(jsonoutput)

