import streamlit as st
import json
import os

# Assuming you have the 'rows' list containing the extracted data
output_file_pathJSON = 'output.json'

# Load the JSON data from the file
with open(output_file_pathJSON, 'r') as json_file:
    json_data = json.load(json_file)

# Display the JSON data in a table using Streamlit
st.table(json_data)
