# Importing Libraries
# Socket is for server connection end and genai is for api call
import google.generativeai as genai
import socket
#Server socket making, binding to port number, and ready for connections
server_socket=socket.socket()
print("Socket Created Successfully!")
server_socket.bind(('localhost',9999))
server_socket.listen()
print("Waiting for connections...")
n=0
#Making the loop for keeping the server running
while True:
    client_socket,addr=server_socket.accept()#Accepting the connection with the client
    print("Connected with",addr)#Confirmation text from the server
    inputfilepath=client_socket.recv(102444).decode()#Taking the input from the client and converting the bytes format to string
    #API Call
    genai.configure(api_key="AIzaSyBilD2uRwotu_MuUhkW1N1VfyqZfLpad4o")
    model=genai.GenerativeModel("gemini-1.5-flash")
    #Opening the file
    with open(inputfilepath,'r') as inputs:
        for line in inputs:
            file_prompt=line.strip()
            response=model.generate_content(file_prompt)
         #Sending back the response
            client_socket.send(bytes(response.text,'utf-8'))
         #Closing the connection
    client_socket.close() 
    print("Disconnected with",addr)
    n+=1
    if(n==3):
        break
print("Server is now closed.")
