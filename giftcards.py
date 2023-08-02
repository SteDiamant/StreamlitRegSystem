import streamlit as st
import pandas as pd
import numpy as np
from database import GitfCards

def new_giftcard_ppayment():
    with st.form(key='GiftCard'):
        st.title('New Gift Card')
        descrtption=st.text_area("Description")
        source=st.text_input("Source")
        amount=st.number_input("Amount")
        if st.form_submit_button(label='Submit'):
            GitfCards.insert_data(descrtption,source,amount)
            st.success('Gift Card Created!')
def update_giftcard_payments():
    """
    Filter the card payments by date.
    Then Import the data to the placeholders of a form 
    In submit button update the data in the database
    """
    df = pd.DataFrame(GitfCards.get_all_data(),columns=('Description','Source','Amount','Date'))
    st.title('Update Card Payments')
    day_choice = st.selectbox('Select Date', df['Date'].unique())
    
    # Filter data by selected date
    filtered_df = df[df['Date'] == day_choice]
    
    with st.form(key='Update GiftCard Info'):
        st.subheader('Gift Card Information')
        # Get the unique gift card descriptions for the selected date
        descriptions = filtered_df['Description'].unique()
        source = filtered_df['Source'].unique()
        selected_description = st.selectbox('Select Source', source)
        
        # Get the relevant row for the selected gift card description
        selected_row = filtered_df[filtered_df['Source'] == selected_description].iloc[0]
        
        # Create input fields for updating the data
        updated_description = st.text_area("Description", value=selected_row['Description'])
        updated_source = st.text_input("Source", value=selected_row['Source'])
        updated_amount = st.number_input("Amount",min_value =0, value=selected_row['Amount'])
        
        if st.form_submit_button(label='Update'):
            GitfCards.update_data(selected_description, updated_description, updated_source, updated_amount)
            st.success('Data updated successfully!')

       
    