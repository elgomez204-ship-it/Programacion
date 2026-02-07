# Descargamos la instalacion de ollama

sudo apt install curl (si no tenemos curl)

curl -fsSL https://ollama.com/install.sh | sh

# Comprobar la version instalada

ollama --version  ## ollama version is 0.13.0

# Alternativa con snap:

sudo snap install ollama

# Quiero saber los modelos que tengo instalado

ollama list
