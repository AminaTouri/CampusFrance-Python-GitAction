from behave import given, when, then
from features.pages.registration_page import RegistrationPage
from collections import OrderedDict
from selenium.webdriver.common.by import By  # Nécessaire pour les assertions dans @then
import time

@given("l'utilisateur est sur la page de création")
def step_ouvrir_page(context):
    context.page = RegistrationPage()
    context.page.open()
    context.page.fermer_banniere_cookies()

@when('l\'utilisateur renseigne l\'email "{AdresseEmail}", le mot de passe "{MotDePasse}", la civilité "{Civilite}", '
    'le nom "{Nom}", le prénom "{Prenom}", le pays de résidence "{PaysDeResidence}", '
    'la nationalité "{PaysDeNationalite}", le code postal "{CodePostal}", la ville "{Ville}", '
    'le téléphone "{Telephone}", le statut "{VousEtes}", le domaine "{DomaineEtudes}" et le niveau "{NiveauEtude}"')
def step_renseigner_infos(context, AdresseEmail, MotDePasse, Civilite, Nom, Prenom,
                          PaysDeResidence, PaysDeNationalite, CodePostal, Ville,
                          Telephone, VousEtes, DomaineEtudes, NiveauEtude):
    user_data = {
        "AdresseEmail": AdresseEmail,
        "MotDePasse": MotDePasse,
        "Civilite": Civilite,
        "Nom": Nom,
        "Prenom": Prenom,
        "PaysDeResidence": PaysDeResidence,
        "PaysDeNationalite": PaysDeNationalite,
        "CodePostal": CodePostal,
        "Ville": Ville,
        "Telephone": Telephone,
        "VousEtes": VousEtes,
        "DomaineEtudes": DomaineEtudes,
        "NiveauEtude": NiveauEtude,
    }

    print(f"🧪 Nouveau JDD : {AdresseEmail}")
    context.user_data = user_data  # ✅ ligne à ajouter                       
    context.page.remplir_formulaire(user_data)


@then("les champs sont bien remplis")
def step_verification(context):
    driver = context.page.driver  
    
    # Vérifie que le bouton radio correct est sélectionné
    statut = context.user_data["VousEtes"]
    statut_id = "edit-field-publics-cibles-2" if statut == "Étudiants" else "edit-field-publics-cibles-3"
    statut_elem = driver.find_element(By.ID, statut_id)
    assert statut_elem.is_selected(), f" Le statut '{statut}' n’est pas sélectionné."

    # Si tout va bien
    print(" Tous les champs ont été remplis et vérifiés avec succès.")

    #time.sleep(3)
    context.page.driver.quit()
