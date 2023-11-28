# helpline_page.py
import streamlit as st

def show_helpline_page():
    # Add styling for better appearance
    st.set_page_config(initial_sidebar_state="collapsed")
    hide_streamlit_style = """
        <style>
            #MainMenu {visibility: hidden;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)
    
    st.title("Helpline Numbers")

    st.write("In case you need official help, please contact the relevant helpline numbers:")

    # Display sample helpline numbers
    st.write("- Police: 100")
    st.write("- Fire: 101")
    st.write("- Medical Emergency: 102")
    st.write("- National Emergency: 112")

if __name__ == "__main__":
    show_helpline_page()
