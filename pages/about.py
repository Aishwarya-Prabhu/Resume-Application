"""About page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the about page in the app.py file"""
    st.title("Know more about me! :thinking_face:")
    st.markdown(
            """## Who Am I?

I'm a Software Engineer with an experience developing web applications for various clients over a year.
Also, I have experience working as an SDET at a medical device company.
I graduated from Northeastern University with a Master's degree in Information Systems and I'm currently looking for a full-time position.
 
**Aishwarya Prabhu**\n
**Software Engineer | Web Developer | QA/Automation Engineer **

[**LinkedIn**](https://www.linkedin.com/in/aishwarya-prabhu/) | [**Email**](mailto:prabhuaishwarya05@gmail.com)

## The Project
Check out my [**GitHub**](https://github.com/aishwarya-prabhu/) for the implementation.


""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
