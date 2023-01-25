from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL DE LOS DATOS DE WIKIPEDIA SOBRE LAS ESTRELLAS.
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Controlador web.
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scarped_data = []


# Definir el método para la extracicón de datos.
def scrape():
               
        # Objeto BeautifulSoup.     
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # MUY IMPORTANTE: la clase "wikitable" y los datos <tr> son válidos al momento de la creación de este código. 
        # Esto puede actualizarse en el futuro, ya que la página es mantenida por Wikipedia. 
        # Comprende la estructura de la página como se discutió en la clase y realiza ‘Web Scraping’ desde cero.

        # Encontrar <table>.
        bright_star_table = soup.find("table", attrs={"class", "wikitable"})
        
        # Encontrar <tbody>.
        table_body = bright_star_table.find('tbody')

        # Encontrar <tr>.
        table_rows = table_body.find_all('tr')

        # Obtener datos de <td>.
        for row in table_rows:
            table_cols = row.find_all('td')
            # print(table_cols)
            
            temp_list = []

            for col_data in table_cols:
                # Imprimir solo columnas de texto usando la propiedad ".text".
                # print(col_data.text)

                # Eliminar los espacios en blanco adicionales usando el método strip().
                data = col_data.text.strip()
                # print(data)

                temp_list.append(data)

            # Agregar los datos a la lista star_data.
            scarped_data.append(temp_list)


       
# Llamar al método.    
scrape()

################################################################

# Importar datos a un CSV.

stars_data = []


for i in range(0,len(scarped_data)):
    
    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

print(stars_data)


# Definir el encabezado.
headers = ['Star_name','Distance','Mass','Radius','Luminosity']  

# Definir el DataFrame  de pandas.   
star_df_1 = pd.DataFrame(stars_data, columns=headers)

#Convertir a CSV.
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")

    


