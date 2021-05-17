### Main page for streamlit resume
import streamlit as st
import pages.about
import pages.skills
import pages.projects
import pages.edu
import pages.experience

import resources.ast as ast

PAGES = {
    "About": pages.about,
    "Education" : pages.edu,
    "Skills": pages.skills,
    "Work Experience": pages.experience,
    "Projects": pages.projects
}

def main():
    """Main function of App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("Hire Me")
    st.sidebar.info(
        """
        If you are looking to hire a Software Engineer with experience in web application development and automation testing domain 
        [email me](mailto:prabhuaishwarya05@gmail.com) or reach out 
        to me on [LinkedIn](https://www.linkedin.com/in/aishwarya-prabhu/)
""")

if __name__ == "__main__":
    main()
