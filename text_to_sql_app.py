
# importing the necessary libraries
import streamlit as st
import google.generativeai as genai

# setting web app page name and selecting wide layout(optional)
st.set_page_config(page_title='Text-To-SQL APP',page_icon=None)#,layout="wide") # option-1 without wide layout
# st.set_page_config(page_title='Text-To-SQL APP',page_icon=None,layout="wide") # option-2 with wide layout


# setting column size 
col1, col2 = st.columns((0.3,1.7))    # without wide layout ( option-1)
# col1, col2 = st.columns((0.15,1.7)) # with wide layout

col1.image('text_to_sql_logo.jpeg')
col2.markdown("# :rainbow[ SQL QUERY AI ASSISTANT APP]")
st.write( "#### :blue[ This is SQL Query Generator Web App Using Google Gemini! ]")

query_input =st.text_area('Please enter your prompt using simple English ')
submit=st.button("Generate SQL")

# defining the api key and loading the gemini pro
genai.configure(api_key="API_KEY") 
model=genai.GenerativeModel('gemini-pro')

## these supportive contexts helps the generative model to be more accurate 
supportive_info1 = ["""Based on the  prompt text, create a SQL query, and make sure to exclude ''' in the beginning and end."""]
supportive_info2 = ["""Based on the SQL query code, create an example input dataframe before the SQL query code is applied and the output dataframe after the SQL query is applied. """]
supportive_info3 = [""" Explain the SQL query in detail without any example output."""]

# Use the model to generate content based on the supportive information and query input provided
response=model.generate_content([supportive_info1[0], query_input])
response2=model.generate_content([supportive_info2[0], response.text])
response3=model.generate_content([supportive_info3[0], response.text])

# if submit is clicked
if submit:
    #creating the columns side by side 
    # col1, col2, col3 = st.columns((0.7,1.0,1.0)) # with wide layout ,
    with st.spinner("Generating.."):

        st.write("##### 1. The Generated SQL Query Code :")
        response=model.generate_content([supportive_info1[0], query_input])
        st.code(response.text)

        st.write("##### 2. A Sample Of Expected Ouput :")
        response2=model.generate_content([supportive_info2[0], response.text])
        st.write(response2.text)

        st.write("##### 3. Explanation of the SQL Query code generated :")
        response3=model.generate_content([supportive_info3[0], response.text])
        st.write(response3.text)






