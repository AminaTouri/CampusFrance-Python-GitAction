from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class RegistrationPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get("https://www.campusfrance.org/fr/user/register")

    def fermer_banniere_cookies(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tarteaucitronPersonalize2")))
            bouton = self.driver.find_element(By.CSS_SELECTOR, "#tarteaucitronPersonalize2")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#tarteaucitronPersonalize2")))
            self.driver.execute_script("arguments[0].click();", bouton)
            print("✅ Bannière de cookies fermée.")
        except Exception as e:
            print("⚠️ Aucune bannière de cookies détectée ou elle n’a pas pu être fermée.")
            print(f"🔍 Détail technique : {e}")

    def remplir_formulaire(self, user):
        try:
            print(f" Remplissage du formulaire pour : {user['AdresseEmail']}")

            self.driver.find_element(By.XPATH, "//input[@placeholder='monadresse@domaine.com']").send_keys(user["AdresseEmail"])
            self.driver.find_element(By.ID, "edit-pass-pass1").send_keys(user["MotDePasse"])
            self.driver.find_element(By.ID, "edit-pass-pass2").send_keys(user["MotDePasse"])

            civilite_id = "edit-field-civilite-mr" if user["Civilite"].lower() == "mr" else "edit-field-civilite-mme"
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.ID, civilite_id))

            self.driver.find_element(By.ID, "edit-field-nom-0-value").send_keys(user["Nom"])
            self.driver.find_element(By.ID, "edit-field-prenom-0-value").send_keys(user["Prenom"])

            self._remplir_selectize_custom("edit-field-pays-concernes", user["PaysDeResidence"])
            self.driver.find_element(By.ID, "edit-field-nationalite-0-target-id").send_keys(user["PaysDeNationalite"])

            self.driver.find_element(By.ID, "edit-field-code-postal-0-value").send_keys(user["CodePostal"])
            self.driver.find_element(By.ID, "edit-field-ville-0-value").send_keys(user["Ville"])
            self.driver.find_element(By.ID, "edit-field-telephone-0-value").send_keys(user["Telephone"])

            statut = user["VousEtes"]
            if statut == "Étudiants":
                statut_id = "edit-field-publics-cibles-2"
            elif statut == "Chercheurs":
                statut_id = "edit-field-publics-cibles-3"
            else:
                raise ValueError(f"Statut non supporté: {statut}")
            radio = self.driver.find_element(By.ID, statut_id)
            self.driver.execute_script("arguments[0].click();", radio)

            assert radio.is_selected(), f" Le statut '{statut}' n'a pas été sélectionné"

            self._remplir_selectize_custom("edit-field-domaine-etudes", user["DomaineEtudes"])
            self._remplir_selectize_custom("edit-field-niveaux-etude", user["NiveauEtude"])

            print(f"✅ Formulaire terminé pour : {user['AdresseEmail']}")
        except Exception as e:
            print(f"❌ Erreur lors du remplissage du formulaire : {e}")
            input("Appuyez sur Entrée pour garder la fenêtre ouverte...")
            raise

    def _remplir_selectize_custom(self, base_id, valeur):
        try:
            container = self.wait.until(EC.presence_of_element_located((By.ID, base_id)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", container)
            input_field = container.find_element(By.XPATH, ".//following::input[@type='text'][1]")

            self.driver.execute_script("arguments[0].click();", input_field)
            ActionChains(self.driver)\
                .move_to_element(input_field)\
                .click()\
                .send_keys(Keys.CONTROL + "a")\
                .send_keys(Keys.BACKSPACE)\
                .perform()
            input_field.send_keys(valeur)
            time.sleep(0.3)
            input_field.send_keys(Keys.ENTER)

            print(f" Champ '{base_id}' rempli avec : {valeur}")
        except Exception as e:
            print(f"❌ Erreur champ selectize '{base_id}' : {e}")
            raise
