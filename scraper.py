import asyncio
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from time import sleep
from datetime import date

# Define the URL of the page you want to scrape
url = "https://www.cars45.com/listing"

total_page = 155

def main():
    for page in range(1, total_page, 1):
        print(f"{page} of {total_page} pages")
        # Define the URL of the page to scrape
        url = f"https://www.cars45.com/listing?page={page}"
        page_tree = BeautifulSoup(requests.get(url).content, 'html.parser')
        listing_urls = page_tree.find_all("a", class_="car-feature car-feature--wide-mobile")
        car_urls = ["https://www.cars45.com/" + url["href"] for url in listing_urls]
        scrape_dates = [date.today().strftime("%d/%m-%y") for i in range(len(car_urls))]
        """print(scrape_dates)
        print(car_urls)
        break"""

        for car_url in car_urls:
            # Send a GET request to the URL
            #response = requests.get(car_url)
            driver = webdriver.Chrome()
            driver.get(f"{car_url}")
            sleep(10)
            #driver.find_element(By.CLASS_NAME, 'main-details__info flex').click()
            #driver.execute_script("arguments[0].click();")
            driver.close()
            #inner_page_tree = BeautifulSoup(response.content, 'html.parser')    

            """if response.status_code == 200:
                print(f"page{page}. Request successful")
                #Find all car details on the page
                car_details1 = list (inner_page_tree.find('div', class_ = "main-details__tags flex wrap"))
                #print(car_details1)
                
                #extract the first set of car details
                use_condition = car_details1[0].text.strip()
                transmission_type = car_details1[1].text.strip()
                mileage = car_details1[2].text.strip()
                #print(use_condition, transmission_type, mileage)
            
                #extract second set of car details
                location = inner_page_tree.find("p", class_ = "main-details__region").text.strip()
                price_formatted = inner_page_tree.find("h5", class_ = "main-details__name__price").text.strip()
                price = price_formatted[2:]
                currency_code = price_formatted[0:1]"""
            
                #extract third set of car details
                # Find the button element using BeautifulSoup
                #button = inner_page_tree.find('button', {'class': 'main-details__info flex'})

                # Use Selenium to click the 
            """driver.find_element(By.CLASS_NAME, 'main-details__info flex').click()
                contact = inner_page_tree.find("button", class_ = "main-details__info flex")
                page_source = driver.page_source
                driver.quit()
                contact_page = BeautifulSoup(page_source, 'html.parser')
                print(contact_page)"""

                #print(location, price, currency_code)          
            break
        break

        """# Create a BeautifulSoup object to parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all car listings on the page
            #car_main_page = soup.find(id='container')
            car_names = []
            car_prices = []
            car_use_conditions = []
            car_mileages = []
            car_colors = []
            car_details = soup.find_all("div", class_="car-feature__details")

            for car_detail in car_details:
                name = car_detail.find("p", class_="car-feature__name").text.strip()
                price = car_detail.find("p", class_="car-feature__amount").text.strip()
                extra_details = car_detail.find("div", class_="car-feature__others").find_all("span", class_="car-feature__others__item")
                extra_details = [extra_detail.text.strip() for extra_detail in extra_details]
                if len(extra_details) == 1:
                    use_condition = extra_details[0]
                    mileage = "N/A"
                elif len(extra_details) == 2:
                    use_condition = extra_details[0]
                    mileage = extra_details[1]
                print(name)
                print(price, use_condition, mileage)
                print()

                name = name.split(" ")
                name = name[0:len(name)-1]
                name = " ".join(name)
                car_color = name[len(name)-1]



                car_names.append(name)
                car_prices.append(price)
                car_use_conditions.append(use_condition)
                car_mileages.append(mileage)
                car_colors.append(car_color)
                

            # Create a pandas DataFrame to store the data
            data = {"Car Name": car_names, "Price": car_prices, "Use Condition": car_use_conditions, "Mileage": car_mileages, "URL": urls}
            df = pd.DataFrame(data)

            # Append the DataFrame to the existing CSV file (or create a new file if it doesn't exist)
            df.to_csv("car_data.csv", mode="a", index=False, header=False)

        # Pause the loop for 60 seconds
        sleep(30)"""

def cars45_scrape():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    import pandas as pd
    

    # Set up the Selenium driver (you may need to download a specific driver for your browser)
    driver = webdriver.Chrome()

    # Open the homepage of the website
    homepage_url = 'https://cars45.com'
    first_listing_page = '/listing'
    page = 1    
    current_page = f'{homepage_url}{first_listing_page}'

    PAGE_ONE = 1

    while(True):
        driver.get(current_page)

        if page == PAGE_ONE:
            #Find the limk to the next page
            next_page =  WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//a[@class="pagination__next"]'))).get_attribute('href')
        else:
            #Find the limk to the next page
            next_page =  WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//a[@class="pagination__next nuxt-link-active"]'))).get_attribute('href')

        # Find all the links to the cars on the current listing page
        anchors = WebDriverWait(driver,3).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="car-feature car-feature--wide-mobile"]')))
        ##print(anchors)
        ##return

        # Visit each cars in the current listing page
        car_urls = [anchor.get_attribute('href') for anchor in anchors]
        print(f'page{page}. All car link on the page gotten successfully') 
        print()

        ##return
        for car_url in car_urls:
            #visit the single car page 
            driver.get(car_url)
            try:
                show_contact_button = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//button[@class="main-details__info flex"]')))
                show_contact_button.click()
                #Get the dealer phone number
                dealer_phone_number = show_contact_button.text
            except NoSuchElementException:
                dealer_phone_number = ""

            try:   
                # Get the dealer location
                dealer_location = driver.find_element(By.CLASS_NAME, 'main-details__region').text
            except NoSuchElementException:
                dealer_location = ""

            try:
                #Get the car name
                car_name = driver.find_element(By.CLASS_NAME, 'main-details__name__title').text
                #Get the car color from car name
                car_color = car_name.split(" ")
                car_color = car_color[-1]

            except NoSuchElementException:
                car_name = ""
                car_color = ""

            try:
                #Get the car price
                car_price = driver.find_element(By.CLASS_NAME, 'main-details__name__price').text
                #Get price currency from car price
                currency = car_price[0:1]  
            except NoSuchElementException:
                car_price = ""
                currency = ""   

            try:
                #Get car use condition 
                car_condition = driver.find_element(By.XPATH, '//div[@class="main-details__tags flex wrap"]//span[1]').text
            except NoSuchElementException:
                car_condition = ""

            try:    
                #Get car transmission type
                car_transmission = driver.find_element(By.XPATH, '//div[@class="main-details__tags flex wrap"]//span[2]').text
            except NoSuchElementException:
                car_transmission = ""

            try:    
                #Get car mileage
                car_mileage = driver.find_element(By.XPATH, '//div[@class="main-details__tags flex wrap"]//span[3]').text
            except NoSuchElementException:
                car_mileage = ""
            
            try:
                #Get the car make
                car_make = driver.find_element(By.XPATH, '//div[@class="general-info grid"]//div[1]//p').text
            except NoSuchElementException:
                car_make = ""

            try:    
                #Get the car model
                car_model = driver.find_element(By.XPATH, '//div[@class="general-info grid"]//div[2]//p').text
            except NoSuchElementException:
                car_model = ""

            try:    
                #Get the car year
                car_year = driver.find_element(By.XPATH, '//div[@class="general-info grid"]//div[3]//p').text
            except NoSuchElementException:
                car_year = ""

            try:     
                #Scrape date of the car
                scrape_date = date.today().strftime("%B-%d-%Y")
                ##scrape_date = date.today().strftime("%d-%m-%y") alternative date format
            except NoSuchElementException:
                scrape_date = ""

            #write to csv file row 
            #create a pandas DataFrame to store the data
            data = {
                "car_name":[car_name], "car_color":[car_color], "car_make":[car_make], 
                "car_model":[car_model], "car_year":[car_year], "car_url":[car_url], 
                "dealer_location":[dealer_location], "car_price":[car_price], 
                "currency":[currency],"car_condition":[car_condition], 
                "car_transmission":[car_transmission], "car_mileage":[car_mileage], 
                "dealer_phone_number":[dealer_phone_number], "scrape_date":[scrape_date]
            }

            df = pd.read_csv('cars45_data.csv')

            if len(df["car_url"]) != 0:
                exists = df["car_url"].eq(car_url).any()
            else:
                exists = False

            if exists:
                df.loc[df['car_url'] == car_url, ['last_scrape_date']] = scrape_date       
                df.to_csv("cars45_data.csv", mode='w', index=False, header=True)
                print("car already exists")
            else:
                data["first_scrape_date"] = [scrape_date]
                data["last_scrape_date"] = [scrape_date]
                df = pd.DataFrame(data)
                df.to_csv("cars45_data.csv", mode='a', index=False, header=False)

            print(car_name, car_color, car_make, car_model, car_year, car_url, 
                dealer_location, car_price, currency, car_condition, 
                car_transmission, car_mileage, dealer_phone_number, 
                scrape_date)

            ##print(link, show_contact_button.text)
            print()
            print()
            sleep(3)

        if next_page == "https://www.cars45.com/listing":
            break

        current_page = next_page
        page += 1

    # Perform any actions you need to do on the visited page"""

    # Close the browser
    driver.quit()

def carmart_scrape_pages():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    import pandas as pd
    import re
    
    CSV_FILE = "carmart_data.csv"

    # Create the WebDriver instance with headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Open the homepage of the website
    homepage_url = 'https://www.carmart.ng/cars-for-sale'

    with open('last_page_downloaded.txt', 'r', encoding='utf-8') as file:
        page = int(file.read() ) 

    current_page = f'{homepage_url}?page={page}'

    PAGE_ONE = 1

    while True:
        driver.get(current_page)

        # Download the DOM of the current page
        dom = driver.page_source

        # Save the DOM to a file with the appropriate extension (e.g., .html)
        filename = f'{page}.html'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(dom)
        
        # Increment page number
        page += 1

        with open('last_page_downloaded.txt', 'w', encoding='utf-8') as file:
            file.write(str(page))

        # Find the link to the next page
        try:
            next_page = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//a[@class="page-link"][@aria-label="Next »"]'))).get_attribute('href')
            print(next_page)

            # Set the current page to the next page link
            current_page = next_page

        except NoSuchElementException:
            break

        sleep(3)

    # Close the browser
    driver.quit()

def run_local_server():
    import http.server
    import socketserver

    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

def get_contact(driver):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    import re

    try:
        contact_whataspp_link = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '//a[@data-bs-original-title="Chat with the advertiser on WhatsApp"]'))).get_attribute('href')
        
        #Get the dealer phone number
        dealer_phone_number = re.search(r'(?<=wa\.me/)\d+', contact_whataspp_link).group()
        dealer_phone_number = dealer_phone_number.replace("234", "0")
        
    except NoSuchElementException:
        dealer_phone_number = ""
    
    return dealer_phone_number

def carmart_scrape_cars():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import TimeoutException
    import pandas as pd
    import re

    """Start the local web server in a separate thread
    server_thread = threading.Thread(target=run_local_server)
    server_thread.daemon = True
    server_thread.start()"""
    

    CSV_FILE = "carmart_data.csv"


    # Create the WebDriver instance with headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-web-security")
    driver = webdriver.Chrome(options=chrome_options)

    """This is the part where data is scrapped from each page"""  
    base_file_path = r'C:\Users\abdulqowiyyu\Desktop\web_scraper\\' 

    with open('last_page_scraped.txt', 'r', encoding='utf-8') as file:
        page = int(file.read())
  


    while(True):
        print()
        print(f'page{page}.')

        file_path = base_file_path + f'{page}.html'
        driver.get(file_path)
    
        # Find all the links to the cars on the current listing page
        anchors = WebDriverWait(driver,3).until(EC.presence_of_all_elements_located((By.XPATH, '//h5[@class="add-title"]//a')))
        ##print(anchors)
        ##return

        # Visit each cars in the current listing page
        car_urls = [anchor.get_attribute('href') for anchor in anchors]
        print()
        print(car_urls)
        #return
        print(f'page{page}. All car link on the page gotten successfully') 
        print()

        ##return

        with open('last_car_url.txt', 'r', encoding='utf-8') as file:
            last_car_scraped = int(file.read())

        start_index = last_car_scraped if last_car_scraped > -1 else 0

        for index, car_url in enumerate(car_urls[start_index:]):

            print(car_url)
            #visit the single car page 
            driver.get(car_url)
            redirected_url = driver.current_url

            if redirected_url != car_url:
                print()
                print('Redirect occured')
                with open('last_car_url.txt', 'w', encoding='utf-8') as file:
                    last_index = last_car_scraped+index+1
                    file.write(str(last_index))
                continue

            """# Create a ThreadPoolExecutor with a single thread (can be increased if needed)
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                # Submit the scrape_data function to the executor as a task
                future = executor.submit(get_contact, driver)

                # Wait for the task to complete and get the result
                dealer_phone_number = future.result()"""
            
            try:
                contact_whataspp_link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//a[@data-bs-original-title="Chat with the advertiser on WhatsApp"]'))).get_attribute('href')
                
                #Get the dealer phone number
                dealer_phone_number = re.search(r'(?<=wa\.me/)\d+', contact_whataspp_link).group()
                dealer_phone_number = dealer_phone_number.replace("234", "0")
                
            except NoSuchElementException:
                dealer_phone_number = ""
            
            except TimeoutException:
                dealer_phone_number = ""
            
            
            """print()
            print(dealer_phone_number)
            continue"""

            try:
                dealer_name = driver.find_element(By.XPATH, '//div[@class="cell-content"]//span//a').text
                
            except NoSuchElementException:
                dealer_name = ""


            try:   
                # Get the dealer location
                dealer_location = driver.find_element(By.CLASS_NAME, 'item-location').text
            except NoSuchElementException:
                dealer_location = ""

            try:
                #Get the car name
                car_name = driver.find_element(By.XPATH, '//ol[@class="breadcrumb"]//li[5]//a').text
                #Get the car color from car name
                ##car_color = car_name.split(" ")
                car_color = ""

            except NoSuchElementException:
                car_name = ""
                car_color = ""


            try:
                #Get the car price
                car_price = driver.find_element(By.XPATH, '//div[@class="p-price-tag skin-green"]').text.replace(',', '')
                #Get price currency from car price
                currency = car_price[0:1]  
                car_price = car_price[1:]
            except NoSuchElementException:
                car_price = ""
                currency = ""   

            try:
                #Get car use condition 
                car_condition = driver.find_element(By.XPATH, '//th[text()="Condition"]/following-sibling::td').text
            except NoSuchElementException:
                car_condition = ""

            try:    
                #Get car transmission type
                car_transmission = driver.find_element(By.XPATH, '//th[text()="Transmission"]/following-sibling::td').text
            except NoSuchElementException:
                car_transmission = ""


            try:    
                #Get car mileage
                car_mileage = driver.find_element(By.XPATH, '//th[text()="Mileage"]/following-sibling::td').text
            except NoSuchElementException:
                car_mileage = ""
            
            try:
                #Get the car make
                car_make = driver.find_element(By.XPATH, '//ol[@class="breadcrumb"]//li[4]//a').text
            except NoSuchElementException:
                car_make = ""

            try:    
                #Get the car model
                car_model = driver.find_element(By.XPATH, '//th[text()="Model"]/following-sibling::td').text
            except NoSuchElementException:
                car_model = ""
            

            try:    
                #Get the car year
                car_year = driver.find_element(By.XPATH, '//th[text()="Year"]/following-sibling::td').text
            except NoSuchElementException:
                car_year = ""
            
            
            try:     
                #Scrape date of the car
                scrape_date = date.today().strftime("%B-%d-%Y")
                ##scrape_date = date.today().strftime("%d-%m-%y") alternative date format
            except NoSuchElementException:
                scrape_date = ""

            #write to csv file row 
            #create a pandas DataFrame to store the data
            data = {
                "car_name":[car_name], "car_color":[car_color], "car_make":[car_make], 
                "car_model":[car_model], "car_year":[car_year], "car_url":[car_url], 
                "dealer_location":[dealer_location], "car_price":[car_price], 
                "currency":[currency],"car_condition":[car_condition], 
                "car_transmission":[car_transmission], "car_mileage":[car_mileage], 
                "dealer_name": [dealer_name],"dealer_phone_number":[dealer_phone_number], 
                "scrape_date":[scrape_date],
                
            }

            df = pd.read_csv(CSV_FILE)

            if len(df["car_url"]) != 0:
                exists = df["car_url"].eq(car_url).any()
            else:
                exists = False

            if exists:
                df.loc[df['car_url'] == car_url, ['last_scrape_date']] = scrape_date       
                df.to_csv(CSV_FILE, mode='w', index=False, header=True)
                print("car already exists")

                with open('last_car_url.txt', 'w', encoding='utf-8') as file:
                    last_index = last_car_scraped+index+0
                    file.write(str(last_index))
            else:
                data["first_scrape_date"] = [scrape_date]
                data["last_scrape_date"] = [scrape_date]
                df = pd.DataFrame(data)
                df.to_csv(CSV_FILE, mode='a', index=False, header=False)

                with open('last_car_url.txt', 'w', encoding='utf-8') as file:
                    last_index = last_car_scraped+index+1
                    file.write(str(last_index))

            print(dealer_name, dealer_phone_number, dealer_location, car_name, car_price, currency, car_condition, car_transmission, car_mileage, car_make, car_model, car_year)
            
            print()
            print()
            sleep(3)

        with open('last_car_url.txt', 'w', encoding='utf-8') as file:
                    file.write('-1')
        page += 1

        with open('last_page_scraped.txt', 'w', encoding='utf-8') as file:
                    file.write(str(page))

    # Perform any actions you need to do on the visited page"""

    # Close the browser
    driver.quit()

def jiji_scrape_cars():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import TimeoutException
    import pandas as pd
    import re
    import threading
    import concurrent.futures
    

    CSV_FILE = "jiji_data.csv"


    # Create the WebDriver instance with headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-web-security")
    driver = webdriver.Chrome(options=chrome_options)

    """This is the part where data is scrapped from each page"""  
    base_file_path = r'C:\Users\abdulqowiyyu\Desktop\web_scraper\\' 

    """ with open('last_page_scraped.txt', 'r', encoding='utf-8') as file:
        page = int(file.read())"""

    page = 1

    while(True):
        print()
        print(f'page{page}.')

        file_path = base_file_path + f'{page}.html'
        driver.get(file_path)
    
        # Find all the links to the cars on the current listing page
        anchors = WebDriverWait(driver,3).until(EC.presence_of_all_elements_located((By.XPATH, '//h5[@class="add-title"]//a')))
        ##print(anchors)
        ##return

        # Visit each cars in the current listing page
        car_urls = [anchor.get_attribute('href') for anchor in anchors]
        print()
        print(car_urls)
        #return
        print(f'page{page}. All car link on the page gotten successfully') 
        print()

        ##return

        with open('last_car_url.txt', 'r', encoding='utf-8') as file:
            last_car_scraped = int(file.read())

        start_index = last_car_scraped if last_car_scraped > -1 else 0

        for index, car_url in enumerate(car_urls[start_index:]):

            print(car_url)
            #visit the single car page 
            driver.get(car_url)
            redirected_url = driver.current_url

            if redirected_url != car_url:
                print()
                print('Redirect occured')
                with open('last_car_url.txt', 'w', encoding='utf-8') as file:
                    last_index = last_car_scraped+index+1
                    file.write(str(last_index))
                continue

            """# Create a ThreadPoolExecutor with a single thread (can be increased if needed)
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                # Submit the scrape_data function to the executor as a task
                future = executor.submit(get_contact, driver)

                # Wait for the task to complete and get the result
                dealer_phone_number = future.result()"""
            
            try:
                contact_whataspp_link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//a[@data-bs-original-title="Chat with the advertiser on WhatsApp"]'))).get_attribute('href')
                
                #Get the dealer phone number
                dealer_phone_number = re.search(r'(?<=wa\.me/)\d+', contact_whataspp_link).group()
                dealer_phone_number = dealer_phone_number.replace("234", "0")
                
            except NoSuchElementException:
                dealer_phone_number = ""
            
            except TimeoutException:
                dealer_phone_number = ""
            
            
            """print()
            print(dealer_phone_number)
            continue"""

            try:
                dealer_name = driver.find_element(By.XPATH, '//div[@class="cell-content"]//span//a').text
                
            except NoSuchElementException:
                dealer_name = ""


            try:   
                # Get the dealer location
                dealer_location = driver.find_element(By.CLASS_NAME, 'item-location').text
            except NoSuchElementException:
                dealer_location = ""

            try:
                #Get the car name
                car_name = driver.find_element(By.XPATH, '//ol[@class="breadcrumb"]//li[5]//a').text
                #Get the car color from car name
                ##car_color = car_name.split(" ")
                car_color = ""

            except NoSuchElementException:
                car_name = ""
                car_color = ""


            try:
                #Get the car price
                car_price = driver.find_element(By.XPATH, '//div[@class="p-price-tag skin-green"]').text.replace(',', '')
                #Get price currency from car price
                currency = car_price[0:1]  
                car_price = car_price[1:]
            except NoSuchElementException:
                car_price = ""
                currency = ""   

            try:
                #Get car use condition 
                car_condition = driver.find_element(By.XPATH, '//th[text()="Condition"]/following-sibling::td').text
            except NoSuchElementException:
                car_condition = ""

            try:    
                #Get car transmission type
                car_transmission = driver.find_element(By.XPATH, '//th[text()="Transmission"]/following-sibling::td').text
            except NoSuchElementException:
                car_transmission = ""


            try:    
                #Get car mileage
                car_mileage = driver.find_element(By.XPATH, '//th[text()="Mileage"]/following-sibling::td').text
            except NoSuchElementException:
                car_mileage = ""
            
            try:
                #Get the car make
                car_make = driver.find_element(By.XPATH, '//ol[@class="breadcrumb"]//li[4]//a').text
            except NoSuchElementException:
                car_make = ""

            try:    
                #Get the car model
                car_model = driver.find_element(By.XPATH, '//th[text()="Model"]/following-sibling::td').text
            except NoSuchElementException:
                car_model = ""
            

            try:    
                #Get the car year
                car_year = driver.find_element(By.XPATH, '//th[text()="Year"]/following-sibling::td').text
            except NoSuchElementException:
                car_year = ""
            
            
            try:     
                #Scrape date of the car
                scrape_date = date.today().strftime("%B-%d-%Y")
                ##scrape_date = date.today().strftime("%d-%m-%y") alternative date format
            except NoSuchElementException:
                scrape_date = ""

            #write to csv file row 
            #create a pandas DataFrame to store the data
            data = {
                "car_name":[car_name], "car_color":[car_color], "car_make":[car_make], 
                "car_model":[car_model], "car_year":[car_year], "car_url":[car_url], 
                "dealer_location":[dealer_location], "car_price":[car_price], 
                "currency":[currency],"car_condition":[car_condition], 
                "car_transmission":[car_transmission], "car_mileage":[car_mileage], 
                "dealer_name": [dealer_name],"dealer_phone_number":[dealer_phone_number], 
                "scrape_date":[scrape_date],
                
            }

            df = pd.read_csv(CSV_FILE)

            if len(df["car_url"]) != 0:
                exists = df["car_url"].eq(car_url).any()
            else:
                exists = False

            if exists:
                df.loc[df['car_url'] == car_url, ['last_scrape_date']] = scrape_date       
                df.to_csv(CSV_FILE, mode='w', index=False, header=True)
                print("car already exists")

                with open('last_car_url.txt', 'w', encoding='utf-8') as file:
                    last_index = last_car_scraped+index+0
                    file.write(str(last_index))
            else:
                data["first_scrape_date"] = [scrape_date]
                data["last_scrape_date"] = [scrape_date]
                df = pd.DataFrame(data)
                df.to_csv(CSV_FILE, mode='a', index=False, header=False)

                with open('last_car_url.txt', 'w', encoding='utf-8') as file:
                    last_index = last_car_scraped+index+1
                    file.write(str(last_index))

            print(dealer_name, dealer_phone_number, dealer_location, car_name, car_price, currency, car_condition, car_transmission, car_mileage, car_make, car_model, car_year)
            
            print()
            print()
            sleep(3)

        with open('last_car_url.txt', 'w', encoding='utf-8') as file:
                    file.write('-1')
        page += 1

        with open('last_page_scraped.txt', 'w', encoding='utf-8') as file:
                    file.write(str(page))

    # Perform any actions you need to do on the visited page"""

    # Close the browser
    driver.quit()

def jiji_scrape_pages():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    import pandas as pd
    import re

    # Create the WebDriver instance with headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Open the homepage of the website
    homepage_url = 'https://www.jiji.ng/cars'

    """with open('last_page_downloaded.txt', 'r', encoding='utf-8') as file:
        page = int(file.read() ) """

    current_page = f'{homepage_url}?page={page}'

    PAGE_ONE = 1

    while True:
        driver.get(current_page)

        # Download the DOM of the current page
        dom = driver.page_source

        # Save the DOM to a file with the appropriate extension (e.g., .html)
        filename = f'jiji_{page}.html'
        """with open(filename, 'w', encoding='utf-8') as file:
            file.write(dom)"""
        
        # Increment page number
        page += 1

        """with open('last_page_downloaded.txt', 'w', encoding='utf-8') as file:
            file.write(str(page))"""

        # Find the link to the next page
        try:
            next_page = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//a[@class="page-link"][@aria-label="Next »"]'))).get_attribute('href')
            print(next_page)

            # Set the current page to the next page link
            current_page = next_page

        except NoSuchElementException:
            break

        sleep(3)

    # Close the browser
    driver.quit()

# Function to scroll down and load more content
def scroll_down(driver):
    import time

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust as needed

def sign_in_jiji():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC 

    # Initialize Selenium webdriver
    chrome_driver_path = r"C:\Users\abdulqowiyyu\Desktop\chromedriver.exe"
    chrome_service = Service(executable_path=chrome_driver_path)

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument(r"user-data-dir=C:\Users\abdulqowiyyu\AppData\Local\Google\Chrome\User Data\Default")


    driver = webdriver.Chrome(service=chrome_service, options=options)

    try:
        # Load the webpage
        url = "https://jiji.ng/login.html"
        driver.get(url)
        login_button = driver.find_element(By.XPATH, '//button[@class="h-width-100p h-bold fw-button qa-fw-button fw-button--type-success fw-button--size-large"]')
        login_button.click()

        #my google email 
        email = ""
        #my google password
        password = ""

        #access jiji login email input 
        email_input_box = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//input[@class="fw-input qa-login-field"]'))) 
        email_input_box.clear()
        email_input_box.send_keys(email)

        #access jiji login password input 
        password_input_box = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//input[@class="fw-input qa-password-field"]')))
        password_input_box.clear()
        password_input_box.send_keys(password)

        login_button = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//button[@class="h-width-100p h-bold qa-login-submit fw-button qa-fw-button fw-button--type-success fw-button--size-large"]')))
        login_button.click()

    except KeyboardInterrupt:
        print("Scraping interrupted by user.")

    finally:
        # Close the ChromeDriver
        driver.quit()

def scrape_single_car_page(driver, car_link):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import ElementClickInterceptedException

    driver.get(car_link)

    #try:

    #Click the Show Contact Button
    
    car_info = {}

    try:
        #Get the Dealer Location
        dealer_location = driver.find_element(By.XPATH, '//div[@class="b-advert-info-statistics__inner"]//div[3]').text
        car_info["dealer_location"] = dealer_location

    except NoSuchElementException:
        dealer_location = driver.find_element(By.XPATH, '//div[@class="b-advert-info-statistics__inner"]//div[2]').text
        car_info["dealer_location"] = dealer_location

    state = dealer_location.split(",")[0].strip()
    LGA = dealer_location.split(",")[1].strip()

    
    #Get the Dealer Name
    dealer_name = driver.find_element(By.CLASS_NAME, "b-seller-block__name").text.strip()
    car_info["dealer_name"] = dealer_name

    #Get dealer phone number
    WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//a[@class="qa-show-contact cy-show-contact js-show-contact b-show-contact"]'))).click()
    dealer_phone_number = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//a[@class="qa-show-contact cy-show-contact js-show-contact b-show-contact b-advert-card-wrapper__buttons-item"]'))).get_attribute('href')

    if dealer_phone_number is None:
        WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//a[@class="qa-show-contact cy-show-contact js-show-contact b-show-contact"]'))).click()
        dealer_phone_number = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//a[@class="qa-show-contact cy-show-contact js-show-contact b-show-contact b-advert-card-wrapper__buttons-item"]'))).get_attribute('href')
    
    dealer_phone_number = dealer_phone_number.replace("tel:", "").strip()
    
    car_info["dealer_phone_number"] = dealer_phone_number
    print(dealer_location, state, LGA, dealer_name, dealer_phone_number)
    return {}

    #     page_source = driver.page_source
    #     soup = BeautifulSoup(page_source, "html.parser")

    car_info_items = driver.find_element(By.XPATH, '//div[@class="b-advert-attributes--tiles"]')

    for item in car_info_items:
        value_div = item.find("div", class_="b-advert-attribute__value")
        key_div = item.find("div", class_="b-advert-attribute__key")
        if value_div and key_div:
            key = key_div.get_text(strip=True)
            value = value_div.get_text(strip=True)
            car_info[key] = value

        

    # except ElementClickInterceptedException:
    #     print("ElementClickInterceptedException")
    #     car_info = {}

    # except NoSuchElementException:
    #     print("Refinding Dealer Location")

    #     return car_info

    # finally:
    #     print(car_info)
    #     return car_info


def jiji_scrape_cars():
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from bs4 import BeautifulSoup
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC 
    from selenium.webdriver.common.keys import Keys

    CSV_FILE = "jiji_data.csv"

    # Initialize Selenium webdriver
    chrome_driver_path = r"C:\Users\abdulqowiyyu\Desktop\chromedriver.exe"
    chrome_service = Service(executable_path=chrome_driver_path)

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument(r"user-data-dir=C:\Users\abdulqowiyyu\AppData\Local\Google\Chrome\User Data\Default")


    driver = webdriver.Chrome(service=chrome_service, options=options)

    try:
        # Load the webpage
        url = "https://jiji.ng/cars"  
        driver.get(url)


        while True:
            # Parse the page source with BeautifulSoup
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, "html.parser")


            # Find all car items on the page
            car_items = soup.find_all("div", class_="b-list-advert__gallery__item")

            # Print car information
            for car_item in car_items:
                car_name = car_item.find("div", class_="b-advert-title-inner").get_text(strip=True)
                car_price = car_item.find("div", class_="qa-advert-price").get_text(strip=True)
                #remove the currency and the commas from the car price
                car_price = car_price.replace("₦", "").replace(",", "")
                #stor the currency in a variable
                currency = "₦"

                #get link to the single car page
                car_url= car_item.find("a")["href"]
                #append jiji.ng to the car link
                car_url = "https://jiji.ng" + car_url
                print("Car URL:", car_url)
                #test car url
                #car_url = "https://jiji.ng/gwarinpa/cars/toyota-highlander-limited-v6-fwd-2004-gold-349uc0bWtNznfGPFfZ73e0Ze.html?page=1&pos=7&cur_pos=7&ads_per_page=20&ads_count=95492&lid=YVYoMZcZt5KR4YD2&indexPosition=6"
                car_info = scrape_single_car_page(driver, car_url)

                # Print car information
                if car_info != {}:
                    #print("Model:", car_info.get("Model", "N/A"))
                    car_model = car_info.get("Model", "N/A")
                    #print("Make:", car_info.get("Make", "N/A"))
                    car_make = car_info.get("Make", "N/A")
                    # print("Year of Manufacture:", car_info.get("Year of Manufacture", "N/A"))
                    car_year = car_info.get("Year of Manufacture", "N/A")
                    # print("Dealer Name", car_info.get("dealer_name", "N/A"))
                    dealer_name = car_info.get("dealer_name", "N/A")
                    # print("Dealer Phone Number", car_info.get("dealer_phone_number", "N/A"))
                    dealer_phone_number = car_info.get("dealer_phone_number", "N/A")

                    dealer_location = car_info.get("dealer_location", "N/A")

                    dealer_state = car_info.get("State", "N/A")

                    car_condition = car_info.get("Second Condition", "N/A")
                    if car_condition == "N/A":
                        car_condition = car_info.get("Bought Condition", "N/A")

                    car_transmission = car_info.get("Transmission", "N/A")
                    car_mileage = car_info.get("Mileage", "N/A")

                    car_color = car_info.get("Colour", "N/A")
                    if car_color == "N/A":
                        car_color = car_info.get("Body Colour", "N/A")

                    scrape_date = date.today().strftime("%B-%d-%Y")
                    # print("Car Name:", car_name)
                    # print("Currency:", currency)
                    # print("Car Price:", car_price)
                    # print("=" * 50)
                    #write to csv file row 
                    #create a pandas DataFrame to store the data
                    data = {
                        "car_name":[car_name], "car_color":[car_color], "car_make":[car_make], 
                        "car_model":[car_model], "car_year":[car_year], "car_url":[car_url], 
                        "dealer_location":[dealer_location], "state": [dealer_state], "car_price":[car_price], 
                        "currency":[currency],"car_condition":[car_condition], 
                        "car_transmission":[car_transmission], "car_mileage":[car_mileage], 
                        "dealer_name": [dealer_name],"dealer_phone_number":[dealer_phone_number], 
                        "scrape_date":[scrape_date],
                        
                    }

                    df = pd.read_csv(CSV_FILE)

                    if len(df["car_url"]) != 0:
                        exists = df["car_url"].eq(car_url).any()
                    else:
                        exists = False

                    if exists:
                        df.loc[df['car_url'] == car_url, ['last_scrape_date']] = scrape_date       
                        df.to_csv(CSV_FILE, mode='w', index=False, header=True)
                        print("car already exists")

                    else:
                        data["first_scrape_date"] = [scrape_date]
                        data["last_scrape_date"] = [scrape_date]
                        df = pd.DataFrame(data)
                        df.to_csv(CSV_FILE, mode='a', index=False, header=False)

            #wait for 5 seconds
            time.sleep(5)

            # Scroll down to load more content
            scroll_down(driver)

    except KeyboardInterrupt:
        print("Scraping interrupted by user.")

    finally:
        # Close the ChromeDriver
        driver.quit()

if __name__ == "__main__":
    #carmart_scrape_pages()
    #carmart_scrape_cars()
    #jiji_scrape_pages()
    jiji_scrape_cars()
    #cars45_scrape()
