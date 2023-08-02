import streamlit as st
import pandas as pd
import numpy as np
from database import Invoice

def new_invoice():
    with st.form(key="New Invoice"):
        st.title('New Invoice')
        name=st.text_input(label='Debiteur',key='name')
        email=st.text_input(label='Debiteur Email',key='email')
        amount=st.number_input("amount",key='amount')
        description=st.text_area("Description",key='description')
        if st.form_submit_button(label='Submit'):
            Invoice.insert_data(name,email,description,amount)
            st.success('Invoice Created!')

def update_invoice():
    df = pd.DataFrame(Invoice.get_all_data(), columns=('name', 'email', 'description', 'amount', 'date'))
    st.title('Update Invoice')
    day_choice = st.selectbox('Select Date', df['date'].unique())
    filtered_df = df[df['date'] == day_choice]
    
    with st.form(key='Update Invoice Info'):
        st.subheader('Invoice Information')

        # Retrieve the first row from the filtered DataFrame as a Series
        selected_row = filtered_df.iloc[0]

        # Use the Series to fill in the form fields with the existing data
        updated_name = st.text_input("Name", value=selected_row['name'], key='invoice_name')
        updated_email = st.text_input("Email", value=selected_row['email'], key='invoice_email')
        updated_description = st.text_area("Description", value=selected_row['description'])
        updated_amount = st.number_input("Amount", key='invoice_amount')
        

        if st.form_submit_button(label='Update_invoice'):
            # Assuming you have a method called Invoice.update_data() to update the data
            Invoice.update_data(
                updated_name,
                updated_email,
                updated_amount,
                day_choice
            )
            st.success('Data updated successfully!')


