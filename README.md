# 🎵 LensCore
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
### Receba recomendações de músicas a partir de imagens.

[README in english](README_en.md)

## 📝 Descrição

O **LensCore** é uma aplicação que utiliza a **Azure Vision API** para analisar imagens enviadas pelo usuário, extrair tags contextuais e, com base nelas, recomendar músicas utilizando a **API do Deezer**.



https://github.com/user-attachments/assets/236c292b-88c5-49ab-8428-50831304d808



---

## 🚀 Como começar

### Pré-requisitos

* **Python 3.11+** (recomendado)
* **Assinatura Azure:** É necessário possuir uma chave da Azure Vision API (há uma camada gratuita disponível para testes).

## 🛠️ Instalação

1. **Configuração na Azure:**
* [Crie uma conta na Azure](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
* [Crie um recurso de Computer Vision](https://portal.azure.com/#create/Microsoft.CognitiveServicesComputerVision) e copie sua **API Key**.


2. **Clonar o projeto:**
* Abra o terminal, navegue até a pasta desejada e execute:


```bash
git clone https://github.com/nemesis-noctis/LensCore.git

```


* *Alternativamente, baixe o projeto como ZIP e descompacte-o.*


3. **Configuração de Ambiente:**
* No diretório raiz, crie um arquivo `.env` e adicione suas credenciais:


```env
VISION_KEY=SUA_API_KEY
```


4. **Ambiente Virtual e Dependências:**
* Crie o ambiente virtual:
```bash
python -m venv .venv

```


* Ative o ambiente:
* **Windows:** `.venv\Scripts\activate`
* **Linux/Mac:** `source .venv/bin/activate`


* Instale os pacotes necessários:
```bash
pip install -r requirements.txt

```


---

## 💻 Execução

1. Execute o comando principal no terminal:
```bash
python main.py

```


2. O terminal exibirá um endereço local. Abra-o no seu navegador:
```
Running on http://127.0.0.1:5000

```
* **Obs:** *O idioma selecionado no site altera o idioma utilizado para a pesquisa.*


---

## 📬 Contato
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jorgemedeirosqneto/) [![email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:jorgemedeiros.qneto@gmail.com) 

## 📌 Versões

* **0.1** - Lançamento Inicial

## ⚖️ Licença

Este projeto está licenciado sob a Licença **MIT** - consulte o arquivo LICENSE para obter detalhes.
