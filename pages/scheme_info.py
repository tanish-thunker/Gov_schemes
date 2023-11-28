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
                color: #FFFFFF;
                font-size: 24px;
                font-weight: bold;
                padding-bottom: 10px;
                border-bottom: 2px solid #FFFFFF;
                margin-bottom: 20px;
            }
            .section-header {
                color: #FFFFFF;
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
    elif scheme_id == 'pmuy':
        show_pmuy_info()    
    elif scheme_id == 'oldage':
        show_oldage_info()    
    elif scheme_id == 'surakshabima':
        show_suraksha_info()    
    elif scheme_id == 'pmkvy':
        show_pmkvy_info()   
    elif scheme_id == 'kisansamman':
        show_kisansamman_info()    
    elif scheme_id == 'kisansinch':
        show_krishisinch_info()    
    elif scheme_id == 'pmayg':
        show_pmayg_info()    
    elif scheme_id == 'kisancard':
        show_kisancard_info()    
    elif scheme_id == 'agriclinic':
        show_agriclinic_info()    
    elif scheme_id == 'financialsc':
        show_financial_info()    
    elif scheme_id == 'deendayal':
        show_deendayal_info()    
    elif scheme_id == 'brambedkar':
        show_brambedkar_info()  
    elif scheme_id == 'agnipath':
        show_agnipath_info()         
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
def show_suraksha_info():
    st.markdown("<h2 class='section-header'>Pradhan Mantri Suraksha Bima Yojana (Central)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("The Pradhan Mantri Suraksha Bima Yojana is a government-backed accident insurance scheme that covers accidental death, permanent disability, and partial disablement. Individuals between 18 years and 70 years are eligible to apply for this scheme.")
    st.write("### Eligibility Criteria:")
    st.write("- The minimum age requirement is 18 years.")
    st.write("- The maximum age requirement is 70 years.")
    st.write("- Those having a savings bank account and falling under the age group of 18 - 70 years are eligible to subscribe to the policy.")
    st.write("- The bank account must be linked with the Aadhaar card.")
    st.write("- If the bank account is not linked with the Aadhaar card, then the Aadhaar card copy must be attached with the application form.")
    st.write("- If the individual has more than one savings account, he or she is only eligible to join the scheme through a single bank account.")
    st.write("- Premium to be paid is Rs.12 yearly.")
    st.write("- The premium amount is auto debited from the insured's bank account.")
    st.write("- The scheme is valid for a year and it can be renewed at the end of the year.")
    st.write("- The primary KYC document required is the applicant's Aadhaar card.")


    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("Pradhan Mantri Suraksha Bima Yojana Registration:")
    st.write("1. The customers can approach either one of the participating banks or health insurance companies to opt for PMSBY.")
    st.write("2. Most of the reputed banks allow the subscribers to take the policy through internet banking.")
    st.write("3. The subscriber will have to log in to the Internet banking account and enroll for the scheme.")
    st.write("4. Subscriber can also send a message through their registered mobile number to the toll free numbers of the banks and the insurance companies.")
     # Add more steps as needed
def show_pmkvy_info():
    st.markdown("<h2 class='section-header'>Pradhan Mantri Kaushal Vikas Yojana (Central)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("Pradhan Mantri Kaushal Vikas Yojana (PMKVY) is the flagship scheme of the Ministry of Skill Development and Entrepreneurship (MSDE) implemented by National Skill Development Corporation (NSDC). The objective of this Skill Certification scheme is to enable Indian youth to take up industry relevant skill training that will help them in securing a better livelihood. SHORT TERM TRAINING: STT component imparted at PMKVY Training Centres (TC) is expected to benefit candidates of Indian nationality who are either school/college dropouts or unemployed. Apart from providing training according to the National Skills Qualification Framework (NSQF), TCs also impart training in soft skills, entrepreneurship, financial and digital literacy. Upon successful completion of assessment, candidates are provided placement assistance by Training Providers. RECOGNITION OF PRIOR LEARNING: Individuals with prior learning experience or skills are assessed and certified under the RPL component of the scheme. Project Implementing Agencies (PIAs) such as Sector Skill Councils (SSCs) or any other agencies designated by MSDE/NSDC are being incentivised to implement RPL projects in any of the three models (RPL camps, RPL at employer's premise and RPL centres). To address knowledge gaps, PIAs offer bridge courses to RPL candidates along with training on soft skills, job role related safety and hygiene practices. SPECIAL PROJECTS: The Special Projects component of PMKVY envisages creation of a platform that will facilitate trainings in special areas and/or premises of Government bodies, corporate or industry bodies, and training in special job roles not defined under the available Qualification Packs (QPs)/National Occupational Standards (NOS). Special Projects require some deviation from the short- term training guidelines under PMKVY for any stakeholder. A proposing stakeholder can be institutions of Central or State Government(s) autonomous body/statutory body or any other equivalent body or corporate who desires to provide training to candidates.")
    st.write("### Eligibility Criteria:")
    st.write("- An Indian unemployed youth, college/school dropout.")
    st.write("- Be at least 18 years of age.")
    st.write("- Have a valid identity proof such as a Voter's ID, Aadhaar Card, or a Bank account.")


    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("To avail the Pradhan Mantri Kaushal Vikas Yojana scheme's benefits, the eligible candidates have to first register online.")
    st.write("The process:")
    st.write("1. Visit the official website of PMKVY to apply online to obtain the training. Link: https://pmkvyofficial.org")
    st.write("2. When the webpage opens, enter your basic information such as your name, email id, education, address, and other required details.")
    st.write("3. Select the course you desire to pursue under the PMKVY scheme. You can pick any one of the courses from 40 options that include food and processing, constructions, electronics, furniture, gems and jewellery, and many more.")
    st.write("4. Find a Training Centre near you by entering the requisite details on the website, and get yourself enrolled in the course you desire to pursue.")
     # Add more steps as needed
def show_kisansamman_info():
    st.markdown("<h2 class='section-header'>Pradhan Mantri Kisan Samman Nidhi (Central)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("The scheme aims to supplement the financial needs of all landholding farmers’ families in procuring various inputs to ensure proper crop health and appropriate yields, commensurate with the anticipated farm income as well as for domestic needs. Under the Scheme an amount of Rs.6000/- per year is released by the Central Government online directly into the bank accounts of the eligible farmers under Direct Benefit Transfer mode, subject to certain exclusions.")
    st.write("### Eligibility Criteria:")
    st.write("All landholding farmers' families, which have cultivable land holding in their names are eligible to get benefit under the scheme except these following categories of beneficiaries belonging to the higher economic status which will not be eligible to obtain the benefits under the scheme:")
    st.write("- Every institutional landholder.")
    st.write("Farmer families belonging to one or more of the below categories:")
    st.write("- Present and past holders of constitutional posts.")
    st.write("- Present and former Ministers, State Ministers, Chairpersons of District Panchayats, 5. Mayors of Municipal Corporations, Members of Lok Sabha or Rajya Sabha or State Legislative Assemblies or State Legislative Councils.")
    st.write("- Every retired and serving employee and officer of Central or State Government Ministries or Offices or Departments and its field units or Central/State PSEs and attached offices or autonomous institutions under government and employees of the local bodies. (Excluding Class IV/Multi Tasking Staff/Group D employees).")
    st.write("- Every superannuated or retired pensioner with a monthly pension of Rs.10,000 and above (Excluding Class IV/Multi Tasking Staff/Group D employees)")
    st.write("- Every person who paid Income Tax in the last assessment year.")
    st.write("- Professionals like Engineers, Doctors, Chartered Accountants, Lawyers, and Architects registered with Professional bodies and carry out the profession by undertaking practices.")
    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("The farmers can apply for this scheme in the following ways:")
    st.write("Offline:")
    st.write("1. The eligible farmers can apply for this scheme with the revenue officials, village Patwaris or other designated officers or agencies by submitting the required details to them.")
    st.write("2. or they can visit their nearest Common Service Centres (CSCs) for registration under the scheme upon payment of fees.")
    st.write("Online:")
    st.write("1. Go to https://pmkisan.gov.in/")
    st.write("2. Click on New farmer registration.")
    st.write("3. Fill out the form and submit.")
    # Add more steps as needed
def show_krishisinch_info():
    st.markdown("<h2 class='section-header'>Pradhan Mantri Krishi Sinchayee Yojana: Per Drop More Crop (Central)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("The scheme mainly focuses on enhancing water use efficiency at the farm level through Micro Irrigation (Drip and Sprinkler Irrigation System). Besides, it also supports micro-level water storage, and water conservation/management activities (Other Interventions) to supplement source creation for Micro Irrigation. It provides financial assistance to farmers for the installation of irrigation components under Micro Irrigation (all assets/ water sources for this must be mandatorily linked with a Micro Irrigation system to achieve water use efficiency) and Installation of drip or sprinkler irrigation in the farmers' field for selected crops.")
    st.write("### Eligibility Criteria:")
    st.write("- The applicant should be a citizen of India.")
    st.write("- All the farmers of the State & Union Territory are eligible to take the benefits of this scheme.")
    st.write("- The subsidy payable to the beneficiary will be limited to an overall ceiling of 5 hectares per beneficiary.")
    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("Offline registration process:")
    st.write("1. The farmers, based on the requirement of their field & region, may contact their Block/District Agriculture Office through their respective Gram Panchayat. Further, the farmer may also contact the Agriculture Officer of their Block/District or call Kisan Call Centre (Toll-Free No. 1800-180-1551).")
    st.write("2. The farmers may approach the concerned authority and request/collect an application form for the scheme.")
    st.write("3. In the application form, fill in all the mandatory fields, paste the passport-sized photograph (signed across), and attach all the (self-attested) mandatory documents.")
    st.write("4. Submit the duly filled and signed application form along with the documents to the designated receiving authority.")
    st.write("5. Acquire the receipt/acknowledgment of the successful submission of the application form from the receiving authority.")
    # Add more steps as needed
def show_pmayg_info():
    st.markdown("<h2 class='section-header'>Pradhan Mantri Awaas Yojana Gramin (PMAYG) (Central)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("Pradhan Mantri Awaas Yojana Gramin (PMAY-G) is centre's flagship mission by the Ministry of Rural Development (MoRD), implemented by the Ministry of Housing and Urban Affairs (MoHUA). PMAY-G aims at providing a pucca house, with basic amenities, to all houseless households and those households living in kutcha and dilapidated house. PMAY-G addresses the rural housing shortage and bridges the housing deficit in rural areas of India, contributing significantly to the mission of Housing for All.")
    st.write("### Eligibility Criteria:")
    st.write("- Houseless families.")
    st.write("- Families with houses having zero, one, or two rooms with a kutcha wall and kutcha roof.")
    st.write("- Households without a literate adult above 25 years of age.")
    st.write("- Households without an adult male member aged between 16 and 59 years of age.")
    st.write("- Households without any adult member between 16 and 59 years of age.")
    st.write("- Households without any able-bodied members and with a disabled member.")
    st.write("- Landless households who derive income from casual labour.")
    st.write("- Scheduled Caste, Scheduled Tribe, Others, and Minorities.")

    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("1. Log in to the official website of the PMAY-G.")
    st.write("2. All the personal details columns have to be filled in, which consists of gender, Aadhaar number, mobile number, and other details.")
    st.write("3. A consent letter for using the Aadhaar data has to be uploaded in its entirety.")
    st.write("4. A search button will now appear. Clicking on it will divulge details on a beneficiary and if the case has priority.")
    st.write("5. Next, click on Register.")
    st.write("6. Automatically, the beneficiary's details will appear. Ensure that the information provided is accurate and updated.")
    st.write("7.The remaining fields including Aadhaar details, details of nomination, bank account, etc. have to be filled.")
    st.write("8. With the completion of this data entry process, if a beneficiary wishes to avail of a loan under this scheme, he or she can click on Yes and fill in an amount required as a loan.")
    st.write("9. Finally, SBM and MGNREGS details have to be uploaded.")
    st.write("With the completion of these steps, the assigned authority will process the request to add a beneficiary.")


    
    # Add more steps as needed
def show_kisancard_info():
    st.markdown("<h2 class='section-header'>Kisan Credit Card (Central)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("The KCC Scheme was introduced with the objective of providing adequate and timely credit to the farmers for their agricultural operations. The Government of India provides interest subvention of 2% and Prompt Repayment Incentive of 3% to the farmers, thus making the credit available at a very subsidized rate of 4% per annum. The scheme aims at providing adequate and timely credit support from the banking system under a single window with the flexible and simplified procedures to the farmers for their cultivation and other needs as indicated below : To meet the short term credit requirements for the cultivation of crops, Post-harvest expenses, Produce marketing loan, Consumption requirements of farmer household, Working capital for maintenance of farm assets and activities allied to agriculture, Investment credit requirement for agriculture and allied activities.")
    st.write("### Eligibility Criteria:")
    st.write("- Farmers - individual/joint borrowers who are owner cultivators.")
    st.write("- Tenant farmers, oral lessees & share croppers.")
    st.write("- Self Help Groups (SHGs) or Joint Liability Groups (JLGs) of farmers including tenant farmers, share croppers etc.")


    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("You can apply for Kisan Credit Card in two ways:")
    st.write("Online Process:")
    st.write("1. Visit the website of the bank you wish to apply for the kisan credit card scheme.")
    st.write("2. From the list of options, choose the Kisan Credit Card.")
    st.write("3. On clicking the option of Apply, the website will redirect you to the application page.")
    st.write("4. Fill the form with the required details and click on Submit.")
    st.write("5. On doing so, an application reference number will be sent. If you are eligible, the bank will get back to you for the further process within 3-4 working days.")
    st.write("Offline Process:")
    st.write("Offline applications can be done by visiting the branch of the bank of your choice or by downloading the application form from the website of the bank as well. The applicant can visit the branch and begin the application process with the help of the bank representative.")

     # Add more steps as needed
def show_agriclinic_info():
    st.markdown("<h2 class='section-header'>Agri-Clinics And Agri-Business Centres Scheme (Central)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("This welfare scheme by the Ministry of Agriculture and Farmers' Welfare aims at agricultural development by supplementing the efforts of public extension by providing extension and other services to farmers either on a payment basis or free of cost as per the business model of agri-preneur, local needs, and affordability of the target group of farmers. AC&ABC creates gainful self-employment opportunities for unemployed agricultural graduates, agricultural diploma holders, intermediate in agriculture, and biological science graduates with PG in agri-related courses.")
    st.write("### Eligibility Criteria:")
    st.write("- The age of the applicant must be between 18 and 60 years.")
    st.write("- The applicant must qualify as one of the following - a. Graduates in agriculture and allied subjects from SAUs/ Central Agricultural Universities/ Universities recognized by ICAR/ UGC. Degree in Agriculture and allied subjects offered by other agencies are also considered subject to the approval of the Department of Agriculture & Cooperation, Government of India on the recommendation of the State Government. b. Diploma (with at least 50% marks)/ Post Graduate Diploma holders in Agriculture and allied subjects from State Agricultural Universities, State Agriculture and Allied Departments, and State Department of Technical Education. c. Diplomas in Agriculture and allied subjects offered by other agencies are also considered subject to the approval of the Department of Agriculture & Cooperation, Government of India on the recommendation of the State Government. d. Biological Science Graduates with Post Graduation in Agriculture & allied subjects. Degree courses recognized by UGC have more than 60 percent of the course content in Agriculture and allied subjects. e. Diploma/Post-graduate Diploma courses with more than 60 percent of course content in Agriculture and allied subjects, after B.Sc. with Biological Sciences, from recognized colleges and universities. f. Agriculture-related courses at intermediate (i.e. plus two) level, with at least 55% marks.")
    st.write("Exclusions:")
    st.write("Retired Employees Getting Pensionary Benefits Are Not Eligible For Subsidy. However, They Can Undergo Training And Establish Self Financed Projects.")
    st.write("- Self Help Groups (SHGs) or Joint Liability Groups (JLGs) of farmers including tenant farmers, share croppers etc.")


    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("Please visit this official link and follow all the guidelines to apply according to your needs. Link: https://www.agriclinics.net/OnlineApplication26052020.pdf")
def show_financial_info():
    st.markdown("<h2 class='section-header'>Financial Assistance Scheme For Higher Competitive/ Entrance Examination To Scheduled Castes/ Backward Classes Students (Haryana)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("The scheme “Financial Assistance Scheme for Higher Competitive/ Entrance Examination to Scheduled Castes/ Backward Classes Students” was launched by the Department of Welfare of Scheduled Castes & Backward Classes, Government of Haryana. Under the scheme, the state government will provide financial assistance to the Scheduled Caste and Backward Classes boys/girls who are unable to avail of the coaching facilities for IAS and other higher services competitive examinations because of their weak financial position. Under the scheme, a committee headed by the Secretary, Welfare of Scheduled Castes & Backward Classes has been constituted which will determine the duration of coaching and quantum of fees for different examinations keeping in view the market rates. Under the scheme, earlier the financial assistance up to ₹10,000/- was being given. The income ceiling under the scheme has also been enhanced from ₹1.00 lacs per annum to ₹2.50 lakhs per annum now.")
    st.write("### Eligibility Criteria:")
    st.write("- The student should be a domicile of Haryana & must belong to a Scheduled caste/Backward Class.")
    st.write("- The annual Income of the parents/guardians Should not exceed ₹2.50 lacs.")
    st.write("- The candidate should possess all the requisite qualifications required for the examination.")
    st.write("- The candidate will not be permitted to avail of more than two chances for a particular competitive examination.")
    st.write("Note 01: The selected candidates shall have to attend all classes. In the event of any student remaining absent for more than 5 days at a time maximum of 15 days during the entire course without any valid reason, benefits of free coaching to him/her shall be discontinued and another candidate shall be taken in his/her place.")
    st.write("Note 02: Depending on the budget allocation, the total number of students should be fixed in advance and distributed among the agencies; it should not be left open-ended.")
    st.write("Note 03: This scheme will be applicable and available for only those courses which are not covered by any other Scheme for Scheduled Castes and Backward Classes run by other departments.")
    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("1.Have application from DWO/TWO or download it from department website.")
    st.write("2. Duly filled the application and submit as prescribed in Advertisement whenever issued.")
def show_deendayal_info():
    st.markdown("<h2 class='section-header'>Deen Dayal Upadhyay Grameen Kaushalya Yojana (Central)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("Deen Dayal Upadhyaya Grameen Kaushalya Yojana (DDU-GKY), the skill training and placement program of the Ministry of Rural Development (MoRD), occupies a unique position amongst other skill training programs, due to its focus on the rural poor youth and its emphasis on sustainable employment through the prominence and incentives are given to post-placement tracking, retention, and career progression.")
    st.write("### Eligibility Criteria:")
    st.write("- Rural youth from poor families in the age group of 15 to 35 years")
    st.write("- Ownership of/ inclusion in BPL Cards or Ownership of/ inclusion in BPL PDS Cards (In some states its called Antyodaya Anna Yojana) or Ownership of/ inclusion in RSBY Card (Rashtriya Swasthya Bima Yojana)")
    st.write("- Family members of SHG members of a registered SHG in the village")
    st.write("- Family members of paid workers under the MGNREGS with a minimum of 15 days of work in the last 12 months.")
    st.write("Note: DDU-GKY insists on mandatory coverage of socially disadvantaged groups (SC/ST 50%, Minority 15%, Women 33%) and 3 percent for Persons with Different Abilities (PwDs) through reservations/ earmarked funds in every project.")
    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("1. A candidate should first enroll himself/herself with Gram Rozgar Sewak or the Gram Panchayat. From there, they get a recommendation for the nearest training center.")
    st.write("2. After contacting the nearby training center, a candidate should collect all the information regarding the trade and the training center that provides the training.")
    st.write("3. Lastly, the applicant should visit the Kaushal Panjee official website https://kaushalpanjee.nic.in/ and fill in all the details for registration.")
def show_brambedkar_info():
    st.markdown("<h2 class='section-header'>Dr. B.R. Ambedkar Awas Navinikarn Yojana (Haryana)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("The Haryana government launched the BR Ambedkar Awas Navinikaran Yojana to assist the backward classes of the State by providing funds for home repairs. Under this scheme, the government will sanction up to Rs 80,000 to the beneficiaries to repair their old houses. However, the scheme is only applicable for the Scheduled Castes (SCs), De-notified Tribes, and Tapriwas Caste.")
    st.write("### Eligibility Criteria:")
    st.write("- The applicant should be been person amongst Scheduled Castes.")
    st.write("- The applicant should have a plot of 50 sq.yard in rural areas and 35 sq.yard in urban areas.")
    st.write("- The applicants should be a permanent resident of Haryana.")
    st.write("- The applicants should be included under the Below Poverty Line (BPL) family list.")
    st.write("- The applicant must have a bank account to receive the money.")
    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("You can apply for this scheme online only:")
    st.write("Online Process:")
    st.write("1. Visit the link: https://saralharyana.gov.in/viewServiceApplicationForm.do?serviceId=9540023&tempId=2808&templStatus=243&state=6&backButtonUrl=")
    st.write("2. Fill the form")
    st.write("3. Submit the form online.")
def show_agnipath_info():
    st.markdown("<h2 class='section-header'>Agnipath Yojana (Central)</h2>", unsafe_allow_html=True)
    
    st.write("### Description:")
    st.write("A welfare scheme by the Department of Military Affairs, MoD under which rigorous military training will be imparted at the youth aged between 17.5 to 23 years and meeting other educational, physical and medical criteria, who are aspirational to be a part of the armed forces. The selected candidates will be enrolled as Agniveers for a period of four years, on completion of which 25 percent of Agniveers shall be enrolled in the Armed Forces as a regular cadre. The scheme aims at improving battle preparedness through transformative evolution with energetic, fitter, diverse, more trainable & resilient youth, suited to the changing dynamics. The scheme will empower, discipline & skill youth with a military ethos. 46,000 Agniveers are planned to be recruited in 2022.")
    st.write("### Eligibility Criteria:")
    st.write("- The applicant must be a citizen of India.")
    st.write("- For the 2022 intake, the age of the applicant must be between 17.5 and 23 years. For the subsequent intakes, the age of the applicant must be between 17.5 and 21 years.")
    st.write("Educational Qualification (Indian Navy):")
    st.write("- For Agniveer SSR, the applicant should be qualified in 10+2 examination with Mathematics, Physics and at least one of these subjects: Chemistry/Biology/Computer Science from an educational board recognized by Ministry of Education, Govt. of India.")
    st.write("- For Agniveer MR, the applicant should have passed Matriculation Examination from the Boards of School Education recognized by Ministry of Education, Govt. of India.")
    # Add more eligibility criteria as needed

    st.write("### Registration Process:")
    st.write("Under the Agnipath Scheme 2023 started by the Ministry of Defense, the recruitment of Agniveer will be done in the same way as the recruitment of soldiers in the defense forces in normal condition.")
    st.write("1. First of all notification will be issued by the Indian Armed Forces for the recruitment of Agniveer. Interested young citizens have to apply according to this notification.")
    st.write("2. After that the young candidates will have to appear in the written test. If the written test is passed by the young candidates then their physical test, literacy etc. will be done.")
    st.write("3. Merit list will be prepared on the basis of written test, physical test, literacy etc given by the candidates through which Agniveer will be appointed in Defense Forces.")




if __name__ == '__main__':
    # Get the scheme_id from the URL
    scheme_id = st.experimental_get_query_params().get('scheme_id', [''])[0]
    show_scheme_info(scheme_id)
