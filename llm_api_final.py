#This program is used to predict the temperature of any place for the next two days at differnent times. The place which is chosen specifically by me is Panjim.

import requests
import json
API_URL = "https://api.open-meteo.com/v1/forecast"

def call_api(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m"
    }
    
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed with status code {response.status_code}"}

def process_input_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        inputs = infile.readlines()

    results = {}
    for line in inputs:
        cleaned_line = line.strip()
        if cleaned_line:
            try:
                # Code expects latitude and longitude separated by a comma
                lat, lon = map(float, cleaned_line.split(','))
                response = call_api(lat, lon)
                results[cleaned_line] = response
            except ValueError:
                results[cleaned_line] = {"error": "Invalid input format. Expected 'latitude,longitude'."}

    with open(output_file, 'w') as outfile:
        json.dump(results, outfile, indent=4)

if __name__ == "__main__":
    input_file = "C:\Python\input.txt"  
    output_file = "C:\Python\output.json"  

    process_input_file(input_file, output_file)
    print(f"Responses saved to {output_file}")