"""Projects page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Projects :female-technologist: ")
    st.markdown(
            """

## Featured Projects [(GitHub)](https://github.com/aishwarya-prabhu/)

**Chat Application [Angular2, HTML, CSS3, JavaScript]**
- Developed a real-time one on one online chat application using Angular framework
- Designed web pages with signup, login, chat windows and edit profile functionality
- Implemented all the functionalities in MVC architecture using HTML, CSS and JavaScript

**Online Bookstore [MySQL, Java, Spring]**
- Developed an application for online purchase of books in Spring MVC and hibernate
- Built a database for storing the buyer, seller and book details using MySQL
- Implemented PDF view functionality to view the billing receipt after an online purchase

**Web Application Prototype and Testing	[Java, Axure, Selenium]**
- Created wireframes and prototype for a fitness website to track individual’s health using Axure 
- Designed prototype for features like fitness tips, healthy recipes, online store and locating restaurants 
- Performed automated testing of the website using Selenium in Java 

**Digit Recognition using Neural Networks [Java]**
- Built a Multi-Layer Neural Network for digit recognition using Java
- Implemented Feed-Forward and Back-Propagation to perform XOR function with 89% accuracy
- Designed and executed unit tests to validate the results

**Bank Database  [MySQL, SQL]**
- Designed a database for a bank using MySQL that stored customer, employee and transaction details
- Formulated an entity-relationship diagram for the database application using MySQL Workbench
- Implemented database functions, triggers, stored procedures, database joins and views

**Testing REST API using Test Driven Development [Python, TravisCI, Postman]**
- Performed Unit testing, System testing, integration testing a REST API using Python
- Implemented Continuous integration using Travis CI
- Verified system tests using Postman

**Automated Testing using Selenium [Java, Selenium, TestNG] **
- Performed automated testing for the end-to-end shopping experience on the amazon website using Java
- Developed individual test cases for user authentication errors
- Generated test result report using TestNG

**Test plan for E-care clinical system [Microsoft Word, Excel] **
- Documented a test plan for a clinical system that stores patient’s admission and diagnosis records
- Designed traceability matrix, test scenarios, test cases and test conditions based on patient’s health insurance details

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()



