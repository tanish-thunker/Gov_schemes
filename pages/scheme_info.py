import streamlit as st

def show_scheme_info(scheme_id):
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
    
    # Add styling for better appearance
    st.markdown(
        """
        <style>
            body {
                color: #1E1E1E;
                background-color: #F5F5F5;
            }
            .header {
                color: #004080;
                font-size: 24px;
                font-weight: bold;
                padding-bottom: 10px;
                border-bottom: 2px solid #004080;
                margin-bottom: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
            body {
                color: #1E1E1E;
                background-color: #F5F5F5;
            }
            .header {
                color: #004080;
                font-size: 24px;
                font-weight: bold;
                padding-bottom: 10px;
                border-bottom: 2px solid #004080;
                margin-bottom: 20px;
            }
            .section-header {
                color: #004080;
                font-size: 20px;
                font-weight: bold;
                margin-top: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add a custom header
    st.markdown("<h1 class='header'>Scheme Information</h1>", unsafe_allow_html=True)

    # Scheme-specific information
    if scheme_id == 'widow_pension':
        show_widow_pension_info()
    elif scheme_id == 'disabilitypension':
        show_disability_info()    
    # Add information for other schemes as needed

def show_widow_pension_info():
    st.markdown("<h2 class='section-header'>Widow Women Pension Scheme (Haryana)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("This is a State scheme under which destitute or deserted women and widow of 18 years of age or above are given pension as per eligibility criteria laid down in the rules of the scheme. Rate of Allowance: Rupees 2750 per month")
    
    st.write("### Eligibility Criteria:")
    st.write("Eligibility Criteria for Widow Women Pension Scheme: Any women of age 18 years and above is eligible for grant of pension under the scheme if she is domicile of Haryana and has been residing in Haryana State for the last 15 year at the time of submission of application and her own income from all sources is below Rupees 2,00,000 per annum and further any one of the three conditions are fulfilled:")
    st.write("- She is a widow; or")
    st.write("- She is destitute without husband, parents and son(s): or")
    st.write("- She is destitute due to desertion or physical/mental incapacity of, a) Husband in case of married women; or b) Parents in case of other women.")
    st.write("Please note that, a woman employed by any Government or by any Local/Statutory Body or any organization substantially financed by any Government or Local/Statutory Body or who is drawing pension or family pension there from will not be eligible under this Scheme.")
    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("Online Process:")
    st.write("1. Visit the link: https://saralharyana.gov.in/viewServiceApplicationForm.do?serviceId=7390017&tempId=2240&templStatus=243&state=6&backButtonUrl=&OWASP_CSRFTOKEN=0UAB-PCES-SPD8-N9C1-LFGP-C1TU-F8II-OIOP")
    st.write("2. Fill the form.")
    st.write("3. Submit the form online.")
    st.write("Offline Process:")
    st.write("1. Go To Official Website:  https://socialjusticehry.gov.in/form/application-form-for-widow-and-destitute-women-pension/")
    st.write("2. Download the application form for the scheme in PDF format.")
    st.write("3. Enter the essential details in the application form and submit the same to the Social Welfare Officer of the respective district along with the required documents. That concludes the application procedure. The beneficiaries will receive their pension amounts soon after the process of verification.")
    # Add more steps as needed
def show_disability_info():
    st.markdown("<h2 class='section-header'>Disability Pension Scheme (Haryana)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("This is a State scheme under which any disabled person of Haryana domicile with a minimum 60 percent disability and are 18 years of age and above, are given pension as per eligibility criteria laid down in the rules of the scheme. Rate of Allowance: Rupees 2750 per month.")
    st.write("### Eligibility Criteria:")
    st.write("Full Eligibility Criteria For Disability Pension Scheme:")
    st.write("- Age 18 years and above.")
    st.write("- Domicile of Haryana & residing in Haryana State.")
    st.write("- Self income from all sources should not exceed the minimum wages of unskilled labour as notified by the Labour Department.")
    st.write("- Disability ranging from 60-100% -> a) Total absence of sight. b) Visual acquity not exceeding 3/60 to 10/200 (snellen) in the better eye with correcting lenses. c) A lose of sense of hearing to the extent that it is non-functional for the ordinary purposes of life. d) Orthopaedic disabled with a permanent disability of 60 percent and above. e) Mental Retardation with I.Q. not exceeding 50.")
    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("You can apply for Disability Pension Scheme (Haryana) in two ways:")
    st.write("Online Process:")
    st.write("1. Visit the link: https://saralharyana.gov.in/viewServiceApplicationForm.do?serviceId=7320009&tempId=2226&templStatus=243&state=6&backButtonUrl=&OWASP_CSRFTOKEN=XPWB-MVUV-D76H-C3VB-PQIM-6GY0-WW3K-TJDM")
    st.write("2. Fill the form.")
    st.write("3. Submit the form online.")
    st.write("Offline Process:")
    st.write("1. Go To Official Website:  https://socialjusticehry.gov.in/form/application-form-for-disability-pension/")
    st.write("2. Download the application form for “Haryana Disability Pension Scheme” in PDF format.")
    st.write("3. Enter the essential details in the application form and submit the same to the Social Welfare Officer of the respective district along with the required documents. That concludes the application procedure. The beneficiaries will receive their pension amounts soon after the process of verification.")
    # Add more steps as needed
def show_pmuy_info():
    st.markdown("<h2 class='section-header'>Pradhan Mantri Ujjwala Yojana (PMUY) (Central)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("In May 2016, Ministry of Petroleum and Natural Gas (MOPNG), introduced the 'Pradhan Mantri Ujjwala Yojana' (PMUY) as a flagship scheme with an objective to make clean cooking fuel such as LPG available to the rural and deprived households which were otherwise using traditional cooking fuels such as firewood, coal, cow-dung cakes etc. Usage of traditional cooking fuels had detrimental impacts on the health of rural women as well as on the environment.")
    st.write("### Eligibility Criteria:")
    st.write("- The applicant must be a woman above the age of 18.")
    st.write("- The applicant must have the BPL card and must be a rural resident.")
    st.write("- The applicant must have a savings bank account in any of the nationalised banks to receive the subsidy amount.")
    st.write("- The applicant's household must not already own an LPG connection.")
    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("You can apply for Pradhan Mantri Ujjwala Yojana 2.0 in two ways:")
    st.write("Online Process:")
    st.write("1. Visit the link: https://www.pmuy.gov.in/ujjwala2.html")
    st.write("2. Read all the details and visit the online portal from there according to distributor of your choice.")
    st.write("3. Fill out the form on the portal and click on submit.")
    st.write("Offline Process:")
    st.write("You can apply to any distributor(Eg. Indane) of your choice by submitting application at the distributor's office nearest to you.")
    # Add more steps as needed
def show_oldage_info():
    st.markdown("<h2 class='section-header'>OLD AGE SAMMAN ALLOWANCE SCHEME (Haryana)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("This is a State scheme under which senior citizens of Haryana domicile in the age group of 60 years and above are given Old Age Samman Allowance as per eligibility criteria laid down in the rules of the scheme. Rate of Allowance:  Rupees 2750 per month.")
    st.write("### Eligibility Criteria:")
    st.write("- The person is of age 60 years or more")
    st.write("- The person is domicile and resident of Haryana State")
    st.write("- Their income from all sources together with that of his/her spouse does not exceed Rupees 3,00,000 per annum.")
    st.write("Please note that, any person receiving pension from any Government or Local/ Statutory Body or any organization substantially financed by any Government or Local/ Statutory Body will not be eligible to receive allowance under the scheme.")
    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("You can apply for Old Age Samman Pension Scheme (Haryana) in two ways:")
    st.write("Online Process:")
    st.write("1. Visit the link: https://saralharyana.gov.in/viewServiceApplicationForm.do?serviceId=7360013&tempId=2239&templStatus=243&state=6&backButtonUrl=&OWASP_CSRFTOKEN=QU1X-K8L0-GG37-WTW3-44O2-2X78-5XAM-XPY9")
    st.write("2. Fill the form ")
    st.write("3. Submit the form online.")
    st.write("Offline Process:")
    st.write("Applying for Old Age Samman Allowance through Atal Seva Kender or E-Disha centre:")
    st.write("1.Fill out the application form with all the mandatory details.") 
    st.write("2.Affix a recent passport-size photograph on the application.")
    st.write("3.Submit the application along with all required documents to the concerned Social Justice Department in Haryana.")
    st.write("4.Wait for the application to be approved by the concerned authority. ")
    st.write("5.Once the application is approved, the applicant will be provided with a beneficiary ID.") 
    st.write("6.The eligible beneficiaries will start receiving the allowance or pension amount directly credited to their bank account.")
    # Add more steps as needed


if __name__ == '__main__':
    # Get the scheme_id from the URL
    scheme_id = st.experimental_get_query_params().get('scheme_id', [''])[0]
    show_scheme_info(scheme_id)
