curso-python

Permissions

```sh
sudo chown -R khristopher ~/plt-test-code
```

Instalación
```sh
sudo apt update
sudo apt -y upgrade
```

Verificar Instalación de python
```sh
python3 -V
```

nstalación de gestor de paquetes de dependencias
```sh
sudo apt install -y python3-pip
```

Verificar Instalación del gestor
```sh
pip3 -V
```

Dependencias en entorno profesional
```sh
apt install -y build-essential libssl-dev libffi-dev python3-dev
```

extensiones vscode
```sh
wsl & python
```

generar ungit ignore
[git ignore](https://www.toptal.com/developers/gitignore)

# Game Project

to run the game u should follow the instructions

```sh
cd game
python3 main.py
```

# Practice

where is locate python and pip on linux
these commands get the ubication 
of python and pip directory on linux

```sh
which python3
which pip3
```

# virtual envirouments

install virtual env

```sh
apt install -y python3-venv
```

create a virtual enviroument

```sh
python3 -m venv <name enviroument>
```

for example

```sh
python3 -m venv env
```

start virtual enviroument

```sh
source env/bin/activate
```

close virtual enviroument

```sh
deactivate
```

create a requeriments file/ file dependency

```sh
pip freeze > requeriments.txt
```

install all dependencies of requeriments file
```sh
pip install -r requeriments.txt
```
