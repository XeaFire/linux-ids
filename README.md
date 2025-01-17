# TP IDS

(groupe : Tristan Diard, Brendan Visine)

## Utilisation

- Sur un environnement linux, cloner le repository.
- Déplacer ids.timer et .service à l'endroit ```/etc/systemd/system/```.
- Pour lancer votre timer et rendre votre verification automatique, utiliser la commande : ```sudo systemctl enable ids.timer``` et  ```sudo systemctl start ids.timer```.
- Pour changer le moment de verif, vous pouvez modifier la valeur ```OnCalendar``` du fichier ids.timer (de base : chaque minute).
- Pour vérifier que votre timer est rappelé (en fonction de la valeur "OnCalendar"), utiliser la commande : ```systemctl list-timers```
- Pour verifier que votre service est bien exécuté, utiliser la commande : ```journalctl -u ids.service```
- Si le service renvoie ```State : Ok``` tout va bien, sinon, s'il renvoi ```State : Divergente``` cela indique que le fichier a été modifier

Si vous voulez tester manuellement le programme, déplacer vous dans le dossier linux-ids qui contient le fichier ids.py (```cd linux-ids```). Ensuite lancé la commande ```python ids.py check```.

## Usage

Ce projet IDS nous permet d'etre informé de la modification d'un fichier. Cette pratique est très utilisé pour avertir d'une intrusion non désiré. Dans le cas ou un fichier a été modifié, on peut s'avoir lequel a été changé afin de le remettre a jour. De plus il est possible de connaitre l'IP de la personne malveillante afin de le bannir.

## Configuration