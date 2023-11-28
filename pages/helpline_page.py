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
    st.write("- Widow Women Pension Scheme (Haryana): 0172-3968400")
    st.write("- Disability Pension Scheme (Haryana): 0172-3968400")
    st.write("- OLD AGE SAMMAN ALLOWANCE SCHEME (Haryana): General: 0172-2715090 | Portal: 1800-2000-023")
    st.write("- Pradhan Mantri Ujjwala Yojana (PMUY): 1800-266-6696")
    st.write("- Pradhan Mantri Suraksha Bima Yojana (Central):  1800-180-1111 | 1800-110-001")
    st.write("- Pradhan Mantri Kaushal Vikas Yojana (Central): 088000-55555")
    st.write("- Pradhan Mantri Kisan Samman Nidhi (Central): 011-24300606")
    st.write("- Pradhan Mantri Krishi Sinchayee Yojana: Per Drop More Crop (Central): 1800-180-1551")
    st.write("- Pradhan Mantri Awaas Yojana Gramin (PMAYG) (Central): 1800-11-3377")
    st.write("- Kisan Credit Card (Central): 1800115526 | 011-24300606")
    st.write("- Agri-Clinics And Agri-Business Centres Scheme (Central): 1800 425 1556")
    st.write("- Financial Assistance Scheme For Higher Competitive/ Entrance Examination To Scheduled Castes/ Backward Classes Students (Haryana): 01722704006")
    st.write("- Deen Dayal Upadhyay Grameen Kaushalya Yojana (Central): 040-24001205")
    st.write("- Dr. B.R. Ambedkar Awas Navinikarn Yojana (Haryana): 0172-2564006 | 0172-2567009")
    st.write("- Agnipath Yojana (Central): 011-26173215")


if __name__ == "__main__":
    show_helpline_page()
