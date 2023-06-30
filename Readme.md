# Pyculator

A simple calculator.<br>
Provide basics operations like :

- `addition`
- `substraction`
- `division`
- `multiplication`

  [](https://github.com/PavelDelhomme/Pyculator/blob/master/img/calculatrice_graphhique_01.png?raw=true)

## Comment exécuter le programme

### Prérequis

Avant d'executer Pyculator, assurez-vous d'avoir les éléments suivant d'installés sur votre système :

- Python (>= 3.6)
- Les bibliothèques requises : Tkinter

### Instructions d'installation

1. Clonez ce référentiel vers votre machine locale :
   <br /><code>git
   clone [https://github.com/PavelDelhomme/Pyculator.git](https://github.com/PavelDelhomme/Pyculator.git)</code>
   <br />
   <br />
2. Accédez au répertoire du projet :
   <br />`cd Pyculator`
   <br />
   <br />
3. Installez les dépendances requises :
   <br />
   `pip install -r requirements.txt`
   <br />
   <br />

### Exécution du programme

Pour exécuter Pyculator, exécutez la commande suivante depuis le répertoire du projet :
<br />
`python main.py`
<br />
<br />
Le programme de la calculatrice devrait s'ouvrir et être prêt à être utilisé.

### Création d'un exécutable

Vous pouvez créer des exécutables pour différentes plateformes à l'aide de bibliothèques telles quee `pyinstaller` ou `py2exe`. Voici comment créer des exécutables pour Windows, Arch Linux et Debian :

#### Windows / ArchLinux / Debian

1. Installez `pyinstaller` en utilisant la commande suivante :
<br /><code>pip install pyinstaller</code>
<br />
<br />
2. Générez l'exécutable :
<br /><code>py installer --onefile main.py</code>
<br />
<br />
Cela créera un exécutable autonome dans le répertoire `'dist/'`.
