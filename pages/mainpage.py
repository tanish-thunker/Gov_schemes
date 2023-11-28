import Orange
import pickle
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from pages import helpline_page

st.set_page_config(initial_sidebar_state="collapsed", page_title="Home Page")
def generate_scheme_info_link(scheme_name, scheme_id):
    return f"[{scheme_name}](/scheme_info?scheme_id={scheme_id})"

# Loading models


model_widow = pickle.load(open("models/widowpension.pkcls", "rb"))
model_disability = pickle.load(open("models/disabilitypension.pkcls", "rb"))
model_pmuy = pickle.load(open("models/pmuy.pkcls", "rb"))
model_oldage = pickle.load(open("models/oldage.pkcls", "rb"))
model_suraksha = pickle.load(open("models/surakshabima.pkcls", "rb"))
model_kisansamman = pickle.load(open("models/kisaansamman.pkcls", "rb"))
model_krishisinch = pickle.load(open("models/krishisinch.pkcls", "rb"))
model_kisancreditcard = pickle.load(open("models/kisaancreditcard.pkcls", "rb"))
model_financialassistance = pickle.load(open("models/financialassistance.pkcls", "rb"))
model_agriclinic = pickle.load(open("models/agriclinic.pkcls", "rb"))
model_brambedkar = pickle.load(open("models/brambedkar.pkcls", "rb"))
model_deendayal = pickle.load(open("models/deendayal.pkcls", "rb"))
model_pmkvy = pickle.load(open("models/pmkvy.pkcls", "rb"))
model_agnipath = pickle.load(open("models/agnipath.pkcls", "rb"))
model_pmayg = pickle.load(open("models/pmayg.pkcls", "rb"))


def preprocess_gender(gender):
    if gender == 'Male':
        return 1
    elif gender == 'Female':
        return 2
    else:
        return 0


def preprocess_disability(disability):
    if disability == 'Yes':
        return 1
    elif disability == 'No':
        return 2
    else:
        return 0


def preprocess_student(student):
    if student == 'Yes':
        return 1
    elif student == 'No':
        return 2
    else:
        return 0


def preprocess_employment(employment):
    if employment == 'Government Employed':
        return 1
    elif employment == 'Self Employed':
        return 2
    elif employment == 'Unemployed':
        return 3
    else:
        return 0


def preprocess_farmer(farmer):
    if farmer == 'Yes':
        return 1
    elif farmer == 'No':
        return 2
    else:
        return 0


def preprocess_bpl(bpl):
    if bpl == 'Yes':
        return 1
    elif bpl == 'No':
        return 2
    else:
        return 0


def preprocess_area(area):
    if area == 'Urban':
        return 1
    elif area == 'Rural':
        return 2
    else:
        return 0


def preprocess_marriage_status(marriage_status):
    if marriage_status == 'Married':
        return 1
    elif marriage_status == 'Un-Married':
        return 2
    elif marriage_status == 'Divorced':
        return 3
    else:
        return 0


def show_main():
    
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
    
    
    # Custom title
    st.title('Government Scheme Eligibility Prediction')
    st.write('Enter the user details to predict the eligibility for government schemes.')

    gender = st.selectbox('Gender', ['Male', 'Female'])
    age = st.number_input('Age', min_value=1)
    disability = st.radio('Are You Disabled?', ['Yes', 'No'])
    student = st.radio('Are You A Student?', ['Yes', 'No'])
    employment = st.selectbox('Employment status', ['Governmnent Employed', 'Self Employed', 'Unemployed'])
    farmer = st.radio('Are You A Farmer?', ['Yes', 'No'])
    bpl = st.radio('Does Your Family Have a BPL Card?', ['Yes', 'No'])
    familyincome = st.number_input('Your Family Income (Annual)', min_value=0)
    disability_percentage = st.number_input('Enter Your Disability Percentage (If not disabled, just enter 0)', min_value=0)
    area = st.selectbox('Which Area Do You Live In?', ['Urban', 'Rural'])
    marriage_status = st.selectbox('Your Marital Status', ['Married', 'Un-Married', 'Divorced'])

    if st.button('Predict Eligibility'):
        # Preprocess user inputs
        gender = preprocess_gender(gender)
        disability = preprocess_disability(disability)
        student = preprocess_student(student)
        employment = preprocess_employment(employment)
        farmer = preprocess_farmer(farmer)
        bpl = preprocess_bpl(bpl)
        area = preprocess_area(area)
        marriage_status = preprocess_marriage_status(marriage_status)

        # Prepare the input data
        input_data = np.array([[gender, age, disability, student, employment, farmer, bpl, familyincome, disability_percentage, area, marriage_status]])


        #Probabilities prediction
        probabilities_widow = model_widow.predict_proba(input_data)[:, 1]
        probabilities_disability = model_disability.predict_proba(input_data)[:, 1]
        probabilities_pmuy = model_pmuy.predict_proba(input_data)[:, 1]
        probabilities_suraksha = model_suraksha.predict_proba(input_data)[:, 1]
        probabilities_oldage = model_oldage.predict_proba(input_data)[:, 1]
        probabilities_kisansamman = model_kisansamman.predict_proba(input_data)[:, 1]
        probabilities_krishisinch = model_krishisinch.predict_proba(input_data)[:, 1]
        probabilities_kisancard = model_kisancreditcard.predict_proba(input_data)[:, 1]
        probabilities_agriclinic = model_agriclinic.predict_proba(input_data)[:, 1]
        probabilities_brambedkar = model_brambedkar.predict_proba(input_data)[:, 1]
        probabilities_deendayal = model_deendayal.predict_proba(input_data)[:, 1]
        probabilities_financial = model_financialassistance.predict_proba(input_data)[:, 1]
        probabilities_pmkvy = model_pmkvy.predict_proba(input_data)[:, 1]
        probabilities_agnipath = model_agnipath.predict_proba(input_data)[:, 1]
        probabilities_pmayg = model_pmayg.predict_proba(input_data)[:, 1]

        # Make predictions using the trained models
        predictions_widow = model_widow.predict(input_data)
        predictions_disability = model_disability.predict(input_data)
        pred_pmuy = model_pmuy.predict(input_data)
        pred_suraksha = model_suraksha.predict(input_data)
        pred_oldage = model_oldage.predict(input_data)
        pred_kisansamman = model_kisansamman.predict(input_data)
        pred_krishisinch = model_krishisinch.predict(input_data)
        pred_kisancard = model_kisancreditcard.predict(input_data)
        pred_agriclinic = model_agriclinic.predict(input_data)
        pred_brambedkar = model_brambedkar.predict(input_data)
        pred_deendayal = model_deendayal.predict(input_data)
        pred_financial = model_financialassistance.predict(input_data)
        pred_pmkvy = model_pmkvy.predict(input_data)
        pred_agnipath = model_agnipath.predict(input_data)
        pred_pmayg = model_pmayg.predict(input_data)

        # Display the predicted schemes
        st.subheader('You may be eligible for:')
        eligible_schemes = []

        if predictions_widow[0] == 1:
            eligible_schemes.append(('Widow Women Pension Scheme (Haryana)', 'widow_pension', probabilities_widow[0]))
        
        if predictions_disability[0] == 1:
            eligible_schemes.append(('Disability Pension Scheme (Haryana)', 'disabilitypension', probabilities_disability[0]))

        if pred_pmuy[0] == 1:
            eligible_schemes.append(('Pradhan Mantri Ujjwala Yojana (PMUY) (Central)', 'pmuy', probabilities_pmuy[0]))

        if pred_oldage[0] == 1:
            eligible_schemes.append(('OLD AGE SAMMAN ALLOWANCE SCHEME (Haryana)', 'oldage', probabilities_oldage[0]))

        if pred_suraksha[0] == 1:
            eligible_schemes.append(('Pradhan Mantri Suraksha Bima Yojana (Central)', 'surakshabima', probabilities_suraksha[0]))

        if pred_kisansamman[0] == 1:
            eligible_schemes.append(('Pradhan Mantri Kisan Samman Nidhi (Central)', 'kisansamman', probabilities_kisansamman[0]))


        if pred_krishisinch[0] == 1:
            eligible_schemes.append(('Pradhan Mantri Krishi Sinchayee Yojana: Per Drop More Crop (Central)', 'kisansinch', probabilities_krishisinch[0]))

        if pred_kisancard[0] == 1:
            eligible_schemes.append(('Kisan Credit Card (Central)', 'kisancard', probabilities_kisancard[0]))

        if pred_agriclinic[0] == 1:
            eligible_schemes.append(('Agri-Clinics And Agri-Business Centres Scheme (Central)', 'agriclinic', probabilities_agriclinic[0]))

        if pred_deendayal[0] == 1:
            eligible_schemes.append(('Deen Dayal Upadhyay Grameen Kaushalya Yojana (Central)', 'deendayal', probabilities_deendayal[0]))

        if pred_brambedkar[0] == 1:
            eligible_schemes.append(('Dr. B.R. Ambedkar Awas Navinikarn Yojana (Haryana)', 'brambedkar', probabilities_brambedkar[0]))

        if pred_financial[0] == 1:
            eligible_schemes.append(('Financial Assistance Scheme For Higher Competitive/ Entrance Examination To Scheduled Castes/ Backward Classes Students (Haryana)','financialsc', probabilities_financial[0]))

        if pred_pmkvy[0] == 1:
            eligible_schemes.append(('Pradhan Mantri Kaushal Vikas Yojana (Central)', 'pmkvy', probabilities_pmkvy[0]))

        if pred_pmayg[0] == 1:
            eligible_schemes.append(('Pradhan Mantri Awaas Yojana Gramin (PMAYG) (Central)', 'pmayg', probabilities_pmayg[0]))

        if pred_agnipath[0] == 1:
            eligible_schemes.append(('Agnipath Yojana (Central)', 'agnipath', probabilities_agnipath[0]))
    

        # Repeat this for other schemes

        if len(eligible_schemes) > 0:
            st.write(f'You are eligible for {len(eligible_schemes)} schemes.')

            for scheme_name, scheme_id, probability in eligible_schemes:
                st.markdown(f'[{scheme_name}](/scheme_info?scheme_id={scheme_id}) - Probability: {probability * 100:.2f}%')
    

    st.write("Need Assistance?")

        # Button to navigate to the call helpline numbers page
    if st.button("Call Helpline Numbers"):
            helpline_page_link = "[Helpline Numbers Page](/helpline_page)"
            st.markdown(f"Click the link below to view helpline numbers: {helpline_page_link}")
            # You can add the redirection logic or any other actions here

        # Button to redirect to another website (chatbot)
    if st.button("Chat with Chatbot"):
            st.write("Please click on this link to start: (https://sites.google.com/view/testgovapp/home)")

if __name__ == '__main__':
    show_main()

