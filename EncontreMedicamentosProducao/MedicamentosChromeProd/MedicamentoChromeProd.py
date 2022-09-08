# minhas importacoes
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from win10toast import ToastNotifier
from faker import Faker
fake = Faker('pt_BR')



class Test_medicamentos():
    def setup_method(self):
        self.driver = webdriver.Chrome(
            executable_path=
            "C:\\Users\\Juliana.bueno\\Desktop\\EncontreMedicamentos\\drivers\\chromedriver.exe")


    def teardown_method(self):
        self.driver.quit()

    def test_pessoal(self):
        self.driver.get("https://cluder.clude.com.br/Login/Index2?ReturnUrl=%2f")
        self.driver.maximize_window()

        # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("@uorak.com")
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("xxx")
        self.driver.find_element(By.XPATH, "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        self.driver.implicitly_wait(10)

        # iniciando
        self.driver.find_element(By.XPATH, "(//a[@href='/Saude'])[1]")
        self.driver.find_element(By.XPATH, "(//a[@href='/Saude'])[1]").click()
        self.driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/a[1]/div[1]").click()
        self.driver.find_element(By.XPATH, "//a[contains(@class,'btn btn-success botao_busca')]")
        self.driver.find_element(By.XPATH, "//a[contains(@class,'btn btn-success botao_busca')]").click()
        self.driver.find_element(By.ID, "txtEndereco").send_keys("06033070")
        self.driver.find_element(By.ID, "txtEndereco").send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)


        # massa de teste: incruir medicamentos a serem pesquisados
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='clude-tab ajuste_tab'][contains(.,'Medicamentos')]"))).click()
        self.driver.find_element(By.ID, "txtMedicamento").send_keys("Dipirona")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//div[contains(.,'Dipirona - Comando do Exército')]"))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Buscar farmácias')])[1]"))).click()
        print("Remédios encontrados")

        # Fim do programa
        self.driver.close()
