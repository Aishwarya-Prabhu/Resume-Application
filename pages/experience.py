"""Experience page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Work Experience :female-technologist:")
    st.markdown(
            """### Philips Healthcare
**Software Development in Test Co-op | January 2020 - June 2020 | Boston, MA**\n
- Developed automated deployment of networked systems that help in testing the Patient monitoring product in order to reduce manual efforts and save time 
- Automated Behavioral Driven Development (BDD) test scenarios on Single Patient Monitoring System using Specflow that wires gherkin syntax into the .NET code 
- Increased Code coverage from 2% to 16% by designing unit test cases in the Web Automation Framework using Moq 
 

### Rachana Infotech Pvt Ltd
**Software Engineer | June 2017 - May 2018 | Belgaum, India**\n
**1. Internal project**
- Designed web pages for company’s internal web application based on the MVC architecture using PHP(CodeIgniter) for generating templates to collect developer inputs for project designs, updates and reviews
- Developed an internal database using MySQL to store data requirements \n
**2. Client project**
- Developed a web application for a cruise company that supported aspects like billing, housekeeping, room service and maintenance
- Designed web pages using AngularJS for client side, Node.js for the backend and MongoDB for data storage
- Used HTML5 features to make the web application interactive
- Implemented CSS3 features like buttons, icons, logos, pseudo classes for styling across the application
- Worked with Express for developing REST API and tested the API using Postman

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()

