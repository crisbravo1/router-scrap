import requests
import sys
from bs4 import  BeautifulSoup
from selenium import webdriver

def connect(username,password):


    url="http://192.168.1.1"
    response = requests.get(url, auth = (username,password))
    # print(response.text)
    #print(response.status_code)


if __name__=="__main__":

    parameters=len(sys.argv)

    if parameters !=3:

        print ("You must give only 2 parameters . Username and password ")
        sys.exit(1)

    else:

        username=str(sys.argv[1])
        print(username)

        password=str(sys.argv[2])

    try:
        connect(username,password)

    except:

        print("You made a mistake")



# Mejoras para el codigo. En este caso ya me conecto a la pagina
#Lo que debo hacer ahora es pulir con los errores de conexion de status.
#Por otra parte debo continuar con el parser de la pagina con beautiful soup
# Debo verificar si es posible que con el request yo pueda navegar atraves de subpaginas
# O si necesariamente debo utilizar selenium
# Del resto debo hacer el parse para reiniciar el router



# # Selecciono el driver que quiero utilizar
# browser = webdriver.Firefox()
# browser.get('http://192.168.1.1')

# # WebDriverWait(browser, 10)

# for handle in browser.window_handles:

#     print(handle)

# browser.switch_to_window(browser.window_handles[1])
# browser.close()

# # alert = browser.switch_to_alert()
# # alert.send_keys('')
# # alert.send_keys(Keys.TAB)
# # alert.send_keys('nanny1steph')
# # alert.accept()
# # print(alert.text)
# # name_prompt = Alert(browser).name_prompt.send_keys("Willian Shakesphere")
# # Alert(browser).accept()
# # print(name_prompt)
# # name_prompt.accept()
# # browser.switch_to.alert.authenticate(' ', 'nanny1steph')

# # def login(username, password):

# #         link='192.168.1.1'
# #         browser = webdriver.Firefox()
# #         URL = "http://" +link
# #         browser.get(URL)
# #         browser.switchTo().alert();
# #         broser.findElement(By.id("userID")).sendKeys("userName");
# #         browser.findElement(By.id("password")).sendKeys("myPassword");
# #         browser.switchTo().alert().accept();



# # if __name__ =='__main__':

# #     login('','nannysteph1')
#
#

# # r = requests.get('http://192.168.1.1')
# r= requests.post("'http://192.168.1.1'", data = {"username":"", "password":"nanny1steph"})
# print(r.text)
#



