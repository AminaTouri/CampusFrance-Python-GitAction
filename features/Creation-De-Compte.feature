Feature: Création de compte sur CampusFrance

  Scenario Outline: Création de compte pour un utilisateur
    Given l'utilisateur est sur la page de création
    When l'utilisateur renseigne l'email "<AdresseEmail>", le mot de passe "<MotDePasse>", la civilité "<Civilite>", le nom "<Nom>", le prénom "<Prenom>", le pays de résidence "<PaysDeResidence>", la nationalité "<PaysDeNationalite>", le code postal "<CodePostal>", la ville "<Ville>", le téléphone "<Telephone>", le statut "<VousEtes>", le domaine "<DomaineEtudes>" et le niveau "<NiveauEtude>"
    Then les champs sont bien remplis

  Examples:
    | AdresseEmail        | MotDePasse | Civilite | Nom   | Prenom | PaysDeResidence | PaysDeNationalite | CodePostal | Ville | Telephone  | VousEtes   | DomaineEtudes | NiveauEtude |
    | etudiant1@test.com  | Test1234   | Mr       | Doe   | John   | Maroc           | France            | 75000      | Paris | 0601020304 | Étudiants  | Informatique  | Licence     |
    | chercheur1@test.com | Pass5678   | Mme      | Smith | Alice  | France          | Canada            | 69000      | Lyon  | 0611121314 | Chercheurs | Biologie      | Doctorat    |
