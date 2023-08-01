import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def read_data():
    df = pd.read_csv(r'data\SamSamMayProducts.csv')#This data are for a single week
    df1 = pd.read_csv(r'data\SamSamMayCashFlow.csv')#This data are for a single week
    return df,df1

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

def process_products(products) :
     products = append_category_to_dataset(products)
     return products

def process_cash(cash) :
    cash['DATE'] = pd.to_datetime(cash['DATE'], format='%m/%d/%Y')
    cash.set_index('DATE', inplace=True)
    cash['DAY'] = cash['DAY'].str.strip()
    return cash

import seaborn as sns
import matplotlib.pyplot as plt

def plot_sales(df):
    # Set the style of the plot
    day_palette = {'Maandag': 'blue', 'Dinsdag': 'green', 'Woensdag': 'orange',
                   'Donderdag': 'red', 'Vrijdag': 'purple', 'Zaterdag': 'brown',
                   'Zondag': 'gray'}
    sns.set_style("darkgrid")
    
    # Create the plot using seaborn
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.lineplot(data=df, x=df.index, y='SALES', marker='o', markersize=5, color='blue')
    ax.set_xticklabels(df.index.strftime('%d'))
    # Set the x-axis ticks and labels
    

    # Set the plot title and axis labels
    plt.title('Sales Over Time')
    plt.xlabel('Dates')
    plt.ylabel('Sales')
    
    # Show the plot
    plt.show()
    return fig


def spliit_weeks(df):
    days = []
    n = len(df)
    for i in range(0, n, 7):
        subset = df[i:i+7]
        days.append(subset)
    return days

def main():

    products,cash=read_data()
    products=process_products(products)
    cash=process_cash(cash)
    st.title('May Sales')
    st.pyplot(plot_sales(cash))
    weeks=(spliit_weeks(cash))
    
    c1,c2,c3,c4=st.columns(4)
    with c1:
        st.title('Week 1')
        st.pyplot(plot_sales(weeks[0]))
        st.write("Weekly Revenue: ",str(round(weeks[0]['SALES'].sum())))
    with c2:
        st.title('Week 2')
        st.pyplot(plot_sales(weeks[1]))
        st.write("Weekly Revenue: ",str(round(weeks[1]['SALES'].sum())))
    with c3:
        st.title('Week 3')
        st.pyplot(plot_sales(weeks[2]))
        st.write("Weekly Revenue: ",str(round(weeks[2]['SALES'].sum())))
    with c4:
        st.title('Week 4')
        st.pyplot(plot_sales(weeks[3]))
        st.write("Weekly Revenue: ",str(round(weeks[3]['SALES'].sum())))
        
if __name__ == "__main__":
    main()