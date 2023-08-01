import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    df = pd.read_csv(r'data/SamSamMayProducts.csv')#This data are for a single week
    return df
def main():
    df=read_data()
    st.title('Product Comparison based on Revenue')
    selected_products = st.multiselect('Select products', df['product_name'])
    # Filter the DataFrame based on the selected products
    filtered_df = df[df['product_name'].isin(selected_products)]

    # Create a bar chart visualization
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.bar(filtered_df['product_name'], filtered_df['revenue'])
    ax.set_xlabel('Product Name')
    ax.set_ylabel('Revenue')
    ax.set_title('Revenue per Product')
    ax.set_xticklabels(filtered_df['product_name'], rotation=45)
    st.pyplot(fig)
    
if __name__ == "__main__":
    main()