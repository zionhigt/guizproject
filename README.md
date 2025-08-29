## Gestionaire de n° de série

### Installation
 - [python] = Dépend de l'OS. Commande python de la CLI
 - WORKDIR: /guizproject/
 ```bash
 # [optionnel] Monter un environement virtuel python
 [python] -m venv env
 # Lancer l'environement, Ex (windows) `\env\Script\activate.bat`
 \env\Script\activate.bat
 # Installer les dépendances
 [python] -m pip install -r requirements.txt

 # Créer le dosier de mémoire
 mkdir /app/data/ # windows: mkdir \app\data\
 # Lancer l'application
 [python] -m app

 ```