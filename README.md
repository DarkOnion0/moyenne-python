# Moyenne

[![moyenne satus](https://gitlab.com/DarkOnion0/moyenne-python/badges/master/pipeline.svg "Gitlab pipeline")](https://gitlab.com/DarkOnion0/moyenne-python/-/pipelines/latest)

Un script qui calcule la moyenne de classe,

## Utilisation :rocket:
* Installer [pip](https://pypi.org/project/pip/) et installer le module `rich` --> `pip install rich`
* Télécharger la dernière version stable et executer `python moyenne-console.py`
* Commencer par créer un nouveaux fichier en choisissant le choix 1 lors du démarage et laissez vous guider  
* Vous pouvez modifier votre moyenne a partir du fichier data.json ou en créer un avec la syntax suivante
  
  ```json
  {
      "Votre_Matière": {
          "note": [
              10.0,
              20.0
          ],
          "coef": [
              1.0,
              2.0
          ],
          "last": [
              20.0,
              2.0
          ],
          "moyenne": 16.67
      }
  }
  ```

  * l'option `note` et `coef` requiert au moins une valeur chacune
  * l'option `moyenne` sera automatiquement calculée et mise a jour 
  * l'option `last` est seulement mise a jour quand vous utiliser le programme pour indenté des notes
* Un fichier data.txt est créer lors de la création d'un fichier (Voir le To-Do)

## Problèmes connus :rocket:

## Contributions

* We need your help 😀

## To-Do

- [x] Sauvegarde de la moyenne
  - [x] Sauvegarde de la moyenne
  - [x] Réutilisation de la moyenne sauvegardée
- [x] Utilisation du donnée data.txt a toute les étapes
- [ ] GUI
