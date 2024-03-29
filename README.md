# QCM-python-app

## Configuration

### Prérequis

- [Python 3.8](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [Git](https://git-scm.com/downloads)
- [Tkinter](https://docs.python.org/fr/3/library/tkinter.html)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)

### Installation

1. Cloner le projet
2. Crée un environnement virtuel avec la commande `python3 -m venv venv`
3. Activer l'environnement virtuel avec la commande `source venv/bin/activate`
4. Installer les dépendances avec la commande `pip install -r requirements.txt`
5. Configurer Tkinter avec la commande `sudo apt-get install python3-tk`

### Lancement

1. Activer l'environnement virtuel avec la commande `source env/bin/activate`
2. Lancer le programme avec la commande `python main.py [json file]`

### Informations

- Le fichier `main.py` est le fichier principal du programme
- Le fichier `qcm.json` contient les questions et les réponses du QCM
- Le fichier `requirements.txt` contient les dépendances du projet

#### Structure du fichier `qcm.json`

```json
{
    [
        {
            "titre": "Question 1",
            "question": "Exemple de question 1",
            "answers": [
                "Réponse 1",
                "Réponse 2",
                "Réponse 3",
                "Réponse 4"
            ], 
            "correct": [
                2,
                3
            ], 
            "nb_points" : 2,
            "type": 1
        }
    ]
}
```

- `titre` : Titre de la question
- `question` : Question
- `answers` : Réponses possibles
- `correct` : Réponses correctes
- `nb_points` : Nombre de points de la question
- `type` : Type de la question (1 = QCM, 2 = Matching)

### Auteurs

- [Denis Gremaud](mailto:denis.gremaud@gmail.com)

### License

Ce projet est sous licence ``GNU GPL v3`` - voir le fichier [LICENSE.md](LICENSE) pour plus d'informations
