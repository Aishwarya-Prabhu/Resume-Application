"""Skills page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Skills :hammer_and_wrench:")
    st.markdown(
            """## Languages
### Programming Languages
- Java
- C#
- SQL 
- Python

### Web Technologies
- HTML5
- CSS3
- JavaScript

## Frameworks
- Angular
- Express.js
- Selenium
- Spring

## Cloud Technologies
- Microsoft Azure/TFS

## Development/Deployment Tools
- Git
- TravisCI
- Jenkins

## Databases
- MongoDB
- MySQL

## Tools
- Postman
- JIRA
- Axure RP
- WordPress

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
