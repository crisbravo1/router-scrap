import requests
import sys
from bs4 import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




def connect(username,password):


    url1="http://192.168.1.1/Status_Router.asp"
    response = requests.get(url1, auth = (username,password))

    if response.status_code == requests.codes.ok:
        # print("Everything is fine")
        return(response.content)

    else:

        print("You made a mistake")
        return(-1)

# NO UTILLIZADO  (util para guardar y usar sesiones de la libreria requests )
def probando_session(username,password):


    url0="http://192.168.1.1"
    url1="http://192.168.1.1/Status_Router.asp"

    s = requests.Session()

    s.post(url1)

    c = s.cookies
    i = c.items()

    print(i)
    #return(s) # Aqui devuelvo la session completa





def selenium_driver(session=None):


    url1=("http://"+username+":"+password+"@192.168.1.1/Status_Router.asp")
    driver=webdriver.PhantomJS()
    wait = WebDriverWait(driver, 100)
    driver.get(url1) # agregue ahorita

    # Espero hasta que el boton se encuentre completamente cargado
    wait.until(EC.element_to_be_clickable( (By.XPATH, "//input[@type='button'and @name='dhcp_release']")))

    # Busco el boton de liberar ip
    button=driver.find_element_by_xpath("//input[@type='button'and @name='dhcp_release']")
    button.click()


    # ########################################################### For debugging
    #y=driver.execute_script(" return document.getElementsByTagName('input').length;")
    #print(y)
    # ##############################################################



def write_result(text,text2):

    f=open("ip.txt","w")
    s="Mi ip actual es: " + text + "\n" "La nueva ip es: " + text2 + "\n" + "Gracias por usar el programa"
    f.write(str(s))
    f.close()


def parsing(response):


    soup = BeautifulSoup(response, 'html5lib')

    ip=soup.find_all_next("td" ,class_="FUNFIELD")[7]  # Esto me costo que jode xD !!!!
    result=ip.select("b")

    text=result[0].text

    return(str(text))

def check_requests(user,password):

    try:
        response=connect(user,password)


    except requests.exceptions.Timeout:

        print( "El request tomo demasiado tiempo en completarse")

    except requests.exceptions.ConnectionError:

        print ("Hubo un error en la conexion intentalo nuevamente")

    except requests.exceptions.RequestException:

        print("Error desconocido al procesar el requerimiento")

    else:

        print(" La conexion fue exitosa")


    return(response)



if __name__=="__main__":

    parameters=len(sys.argv)

    if parameters !=3:

        print ("You must give only 2 parameters . Username and password ")
        sys.exit(1)

    else:

        username=str(sys.argv[1])
        password=str(sys.argv[2])


    response=check_requests(username,password)      #me conecto al router
    ip=parsing(response)                            #hago el parsing
    selenium_driver()                               #presiono el boton  del router
    response2=check_requests(username,password)     # me conecto nuevamente al router
    ip2=parsing(response2)                          #obtengo la nueva ip (en este caso 0.0.0.0)
    write_result(ip,ip2)                             # escribo el resultado en un archivo




## Notas del codigo
## Agregar manejo de errores para la funcion parsing() y para la funcion de selenium_driver()






