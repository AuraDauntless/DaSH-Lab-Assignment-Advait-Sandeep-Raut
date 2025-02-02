# Adding libraries
import google.generativeai as genai
import json
import time
# Input Part
inputfilepath=input("Specify text file location")
outputfilepath=input("Specify json file location")
# API Call Part and reading the input file
genai.configure(api_key="AIzaSyBilD2uRwotu_MuUhkW1N1VfyqZfLpad4o")
model = genai.GenerativeModel("gemini-1.5-flash")
#Defining the output list
output_list=[]
# Opening Part and specifying the information in the form of a variable
with open(inputfilepath,'r') as inputfile:
    for line in inputfile:
        file_prompt=line.strip()
        # Getting the time before the call
        Timesent=int(time.time())   
        response = model.generate_content(file_prompt)
        # Getting the time after the call
        Timerecvd=int(time.time()) 
        # Making the python dictionary in the given format
        formatted_output={
        "Prompt": file_prompt,
        "Message":response.text,
        "TimeSent":Timesent,
        "TimeRecvd":Timerecvd,
        "Source":"Gemini 1.5"
            }
        output_list.append(formatted_output)
#converting the python dictionary to a json formatted string
jsonoutput= json.dumps(output_list,indent=4)
# Publishing the file
with open(outputfilepath,'a') as file:
    file.write(jsonoutput)