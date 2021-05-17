"""Edu page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Education :books:")
    st.markdown(
            """### Northeastern University
**Master of Science in Information Systems | December 2020** | [**NEU**](https://www.northeastern.edu/)\n

**Courses ** \n
- Application Engineering and Development \n
- Database Management and Database Design \n
- Web Development Tools and Methods \n
- Web Design and User Experience Engineering \n
- User Experience Design and Testing \n
- Software Quality Control and Management \n
- Program Structures and Algorithms \n
- Software Engineering \n



### Visvesvaraya Technological University
**Bachelors of Engineering in Computer Science | June 2017** | [**VTU**](https://vtu.ac.in/)\n

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
