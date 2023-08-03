import streamlit as st
import pandas as pd
import numpy as np
from database import Card
import matplotlib.pyplot as plt


def new_card_ppayment():
    with st.form(key='Card Payments'):
        st.title('New Card Payments')
        c1,c2,c3,c4=st.columns(4)
        with c1:
            visa_count = st.number_input(label='Visa',min_value=0,step=1)
        with c2:
            mastercard_count = st.number_input(label='Mastercard',min_value=0,step=1)
        with c3:
            maestro_count = st.number_input(label='Maestro',min_value=0,step=1)
        with c4:
            vpay_count = st.number_input(label='Vpay',min_value=0,step=1)
        total=visa_count+mastercard_count+maestro_count+vpay_count
        st.write('Total:',str(total))
        if st.form_submit_button(label='Submit'):
            Card.create_db()
            Card.insert_data(visa_count,mastercard_count,maestro_count,vpay_count)

def update_card_payments():
    """
    Filter the card payments by date.
    Then Import the data to the placeholders of a form 
    In submit button update the data in the database
    """
    df=pd.DataFrame(Card.get_all_data(),columns=('Visa','Mastercard','Maestro','Vpay','Total','Date'))
    st.title('Update Card Payments')
    day_choice=st.selectbox('Select Date',df['Date'].unique())
    with st.form(key='Update Card Payments'):
        
        c1,c2,c3,c4=st.columns(4)
        # Define placeholders for all four inputs
        visa_placeholder = str(int(df[df['Date'] == day_choice]['Visa']))
        mastercard_placeholder = str(int(df[df['Date'] == day_choice]['Mastercard']))
        maestro_placeholder = str(int(df[df['Date'] == day_choice]['Maestro']))
        vpay_placeholder = str(int(df[df['Date'] == day_choice]['Vpay']))

        # Collect user inputs with st.text_input and validate the input
        with c1:
            visa_input = st.text_input(label='Visa', placeholder=visa_placeholder)
            try:
                visa_count = int(visa_input)
            except ValueError:

                visa_count = int(visa_placeholder)

        with c2:
            mastercard_input = st.text_input(label='Mastercard', placeholder=mastercard_placeholder)
            try:
                mastercard_count = int(mastercard_input)
            except ValueError:
                mastercard_count = int(mastercard_placeholder)

        with c3:
            maestro_input = st.text_input(label='Maestro', placeholder=maestro_placeholder)
            try:
                maestro_count = int(maestro_input)
            except ValueError:
                maestro_count = int(maestro_placeholder)

        with c4:
            vpay_input = st.text_input(label='Vpay', placeholder=vpay_placeholder)
            try:
                vpay_count = int(vpay_input)
            except ValueError:
                vpay_count = int(vpay_placeholder)

                total=visa_count+mastercard_count+maestro_count+vpay_count
                st.write('Total:',str(total))
        total=visa_count+mastercard_count+maestro_count+vpay_count
        if st.form_submit_button(label='Update Information'):
            Card.update_data(visa_count,mastercard_count,maestro_count,vpay_count,day_choice)
            st.experimental_rerun()
    st.write(df)


class CardPaymentsVisualisation:
    def __init__(self) -> None:
        df = pd.DataFrame(Card.get_all_data(), columns=('Visa', 'Mastercard', 'Maestro', 'Vpay', 'Total', 'Date'))
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
        df.sort_values(by='Date', inplace=True)
        self.df = df
        
    def visualize_card_payments_over_time(self):
        choices=st.multiselect('Select Card Type', self.df.columns[0:4])
        fig,axis=plt.subplots()
        fig=plt.figure(figsize=(8, 3))
        for i in choices:
            plt.plot(self.df['Date'], self.df[i], label=i)
            plt.legend()
        plt.xlabel('Date')
        plt.xticks(rotation=45)
        plt.ylabel('Payment Amount')
        plt.title('Card Payments Over Time')
        return fig
    
    def visualize_bar_totals(self):
        fig,axis=plt.subplots()
        fig=plt.figure(figsize=(8, 6))
        plt.bar(self.df['Date'],self.df['Total'])
        plt.xlabel('Date')
        plt.ylabel(':euro:')
        plt.title('Total Payments Over Time')
        return fig
    def visualize_total_per_card(self):
        """
            Bar Plot that show the total amount for each column bui the last one
        """
        fig,axis=plt.subplots()
        fig=plt.figure(figsize=(10, 6))
        plt.bar(self.df.columns[0:4],self.df.iloc[:,0:4].sum())
        plt.xlabel('Card Type')
        plt.ylabel(':euro:')
        plt.title('Total Payments Per Card')
        return fig

    def main():
        visualization = CardPaymentsVisualisation()
        print(visualization.df)
        st.title('Card Payments')
        c1,c2=st.columns(2)
        with c1:
            st.pyplot(visualization.visualize_total_per_card())
        with c2:
            st.pyplot(visualization.visualize_bar_totals())
        st.pyplot(visualization.visualize_card_payments_over_time())

