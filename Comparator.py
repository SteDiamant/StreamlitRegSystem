import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    """
    Read data from the CSV file.

    Returns:
        pd.DataFrame: The DataFrame containing the data.
    """
    df = pd.read_csv(r'data\roducts.csv')  # This data is for a single week
    return df

def importLists():
    unknow=['Theeglas heet water ','IJskoffie','Mazda Lunch','Kinderijsje','Slagroom','Daghap medew.','Cadeau bon','met Mayonaise','Stokbrood vooraf!','Tafel mee - keuken','Satesaus met prijs', 'Kids Frikadelletjes', 'Met Ketchup', 'Met Curry', 'Met Mayonaise', 'met spek', 'Haver i.p.v.', 'Spa blauw', 'Spa blauw GRO 0.75', 'Spa rood', 'Spa rood GRO 0.75', 'Wit Montcalm', 'Rose Montcalm', 'Charles Tyrand Eclip', 'Domaine Charles Tyra', 'Pinot grigio fles wi', 'Laphroaigh', 'Courvoisier', 'Armagnac', 'Verse Muntthee', 'Extra slagroom', 'Boterham/bol vlokken', 'Gin Tonic', 'Limoncello Spritz', 'Gin Tonic 0%', 'Peuterfrites', 'Kids Beefburgr doorb', 'Kids krokante kip', 'Kids Pannenkoek', 'Kids Beefburgr mediu', 'Kids Knakworst diner', 'Broodje Knakwrst lun', 'Snack Bitterballetje', 'Snack poffertjes', 'Kids Fish en chips', 'Speciaalmenu', 'Lunch Speciaal', 'Mazda Lunch']
    food=['Varkenssate','Falafer & Hummus','Kaasloempiaatjes',"Nacho's groot VEGA",'Oude Kaas','Falafel & Hummus','Salade Krokante kip','Borrel box','Borrel box vega','Brownie','Kaas en worst','Breekbrood',"Nacho's klein vega","Nacho's klein",'Kiphaasjes','Twente','Bitterballen','Garnalenkroketjes','Warm Plukbrood','Geroosterde groenten','Frites','Frisse salade',"Cafe steak","Nacho's groot",'Nachos groot VEGA ',"Nacho's groot",'Eendenborst','Gele curry vegan','Sticky Lemon Chicken','Zalmfilet', 'Gravad Lax Voor','Carpaccio voor','Gyoza', 'Salade Krokante kip ', 'Tosti Ham', 'Yog. bosvruchtenijs','Glutenvrij Broodje', 'Grolsch session IPA', 'Loaded fries Rendang', 'Tosti kaas', 'Tosti ham kaas', 'Tosti ham kaas anana', 'Club Sandwich', 'Broodje Gravad Lax', 'Twentse Ham', 'Broodje Carpaccio', 'Pistolet Kaas', 'Waldkorn kaas', 'Waldkorn Ham', 'Pistolet Filet Ameri', 'Waldkorn Filet Ameri', 'Pistolet tonijnsalad', 'Waldkorn Tonijnsalad', 'Sam Sam Koffie', 'Uitsmijter', 'Een kroket+brood', 'Twee kroket+brood', 'Tuna melt', 'Broodje kaas', 'Broodje beenham', 'Br Tonijnsalade AVE', 'Sam Sammertje', 'Appeltaart', 'Cheesecake rood frui', 'Worteltaart', 'Brownie', 'Arretjescake', 'Red Velvet Cake', 'Vegan Banana cake', 'Dadeltaart', 'Parfait', 'Limoncello Cheesecak', 'Sweetbox', 'Broodje warm vlees', 'Banh Mi Seitan', 'Banh Mi Kip', '12 uurtje', 'Flammkuchen', 'Mosterdsoep', 'Ramen buikspek', 'Ramen tofu', 'Bouillabaisse', 'Soep Sam Sam', 'Soep Sam Sam GRO', 'Salade Thaise Biefst', 'Salade Tabouleh', 'Big Burger + friet', 'Falafelburger+friet', 'Rode curry', 'Kabeljauw', 'Kophaas', 'Jack Fruit Rendang', 'Pancake', "Chik'n Nuggets", 'Zoete aard. frites', 'Big Burger Concordia', 'Quinoa Burger Concor', 'Kipsate Concordia', 'Jack Fruit Conc', 'Halve p Bitterballen', 'Halve p Garnalenkr', 'Big Burger AVE', 'Falafelburger AVE', 'Frites AVE', 'Zomerdeal Borrelbox']
    drinks=['Johnnie Walker Black','Wisseltap','Limoncello Spritz','Koninck','Speciaal drankje L','Bacardi Cola','Baileys','Grand Marnier','Aperol Spritz','Grimbergen Tripel','Grimbergen Blanche','Grimbergen Blond','Grimbergen Dubbel','Cointreau','Amaretto','Sangiovese delle Mar','Berenburg','Bio Gember/sinas','Wodka','Jasmijnthee','Limoncello shot','Rode Port','Latte met siroop','Koffie', 'Ceylanthee', 'Cappuccino', 'Koffie verkeerd', 'Espresso', 'Dubbele koffie', 'Dubbele Cappuccino', 'Dubbele Espresso', 'Decaf Koffie', 'Decafe Cappucino', 'Irish coffee', 'Espresso Macchiato', 'Spanish Coffee', 'Verse gemberthee', 'Radler 0.0', 'Jardin Bluethee', 'Rooibosthee', 'Liefmans Fruitesse', 'Grolsch Radler', 'Kamille thee', 'Pils', 'Fluitje', 'Halve liter', 'Grolsch 0%', 'Duvel', 'Chai Tea Latte', 'Filmclub koffie', 'Weizen Klein', 'Gunnen Vert thee', 'Earl Greythee', 'Weizen Groot', 'Decaf Latte Macchiat', 'Latte Macchiato', 'Cola', 'Tonic', 'Ginger Ale', 'Bitter lemon', 'Ginger Beer', 'Appel/Spa', 'Fanta', 'Rivella', 'Sprite', 'Cola Zero', 'Cassis', 'Beugel', 'Chocomel warm', 'Chocomel koud', 'Fristi', 'Ranja', 'Karnemelk', 'Liefmans 0.0', '0.50 Karaf Water', '1.00 karaf Water', 'Glas Water', 'Chocomel Slagroom', 'Sauvignon Blanc glas', 'Grolsch Weizen 0.0', 'Pinot Grigio', 'Hugo', 'Bio Vlierbes', 'Bio Citroen', 'Fles Prosecco', 'Prosecco', 'Sauvignon fles wit', 'Fles Rose', 'Italian coffee', 'Cappu Ned', 'Flat White', 'Classic Ice Tea', 'Glas Rose', 'Green Ice Tea', 'Glas Merlot', 'Glas Wit Zoet', 'Jus', 'Ap. Pe. Fram.', 'Appelsap']
    return unknow,food,drinks

def append_category_to_dataset(dataset):
    # Create a new column 'category' in the dataset

    dataset['category'] = ''
    unknown,food,drinks=importLists()
    # Iterate over each row in the dataset
    for index, row in dataset.iterrows():
        product_name = row['product_name'].strip()
        
        # Check if the product_name is in the 'food' list
        if product_name in food:
            dataset.at[index, 'category'] = 'food'

        # Check if the product_name is in the 'drinks' list
        elif product_name in drinks:
            dataset.at[index, 'category'] = 'drinks'

        # Check if the product_name is in the 'unknown' list
        elif product_name in unknown:
            dataset.at[index, 'category'] = 'unknown'
        # Put the variiable ansunged to the rest
        else :
            dataset.at[index, 'category'] = 'unasigned'

    return dataset

def visualize_revenue_by_product(df, selected_products, identifier):
    """
    Visualize revenue for selected products in a bar chart.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        selected_products (list): List of selected product names.
        identifier (str): Column name for the selected identifier.
    """
    filtered_df = df[df['product_name'].isin(selected_products)]

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.bar(filtered_df['product_name'], filtered_df[identifier])
    ax.set_xlabel('Product Name')
    ax.set_ylabel(f'{identifier.capitalize()}')
    ax.set_title(f'{identifier.capitalize()}')
    ax.set_xticklabels(filtered_df['product_name'], rotation=45, ha='right')
    st.pyplot(fig)


def filter_by_category(df, category):
    """
    Filter the DataFrame by category.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        category (str): The category to filter by.
    """
    return df[df['category'] == category]

def visualize_top_10_products(df, identifier):
    """
    Visualize the top 10 products by revenue in a bar chart.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        identifier (str): Column name for the selected identifier.
    """
    # Group the DataFrame by product_name and sum the identifier
    grouped_df = df.groupby('product_name').sum()[identifier].sort_values(ascending=False)

    # Select the top 10 products
    top_10_products = grouped_df.head(10)

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.bar(top_10_products.index, top_10_products)
    ax.set_xlabel('Product Name')
    ax.set_ylabel(f'{identifier.capitalize()}')
    ax.set_title(f'Top 10 Products by {identifier.capitalize()}')
    ax.set_xticklabels(top_10_products.index, rotation=90, ha='right')
    return fig
def main():
    """
    Main function to run the Streamlit app.
    """
    df = read_data()
    df = append_category_to_dataset(df)
    st.title('Product Comparison based on Revenue')

    selected_products = st.multiselect('Select products', df['product_name'])
    identifier = st.radio('Select identifier', ['amount', 'revenue'],horizontal=True)
    # Filter and visualize the DataFrame based on the selected products
    if selected_products:
        visualize_revenue_by_product(df, selected_products,identifier)
        identifier1 = st.radio('Select identifier', ['food', 'drinks','unknown','unasigned'],horizontal=True)
        st.slider
        st.pyplot(visualize_top_10_products(filter_by_category(df, identifier1),identifier))
if __name__ == "__main__":
    main()