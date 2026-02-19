# 🎵 LensCore
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
### Get music recommendations from images.

[README em português](README.md)

## 📝 Description

**LensCore** is an application that utilizes the **Azure Vision API** to analyze images uploaded by the user, extract contextual tags, and based on them, recommend music using the **Deezer API**.

https://github.com/user-attachments/assets/236c292b-88c5-49ab-8428-50831304d808

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.11+** (recommended)
* **Azure Subscription:** An Azure Vision API key is required (a free tier is available for testing).

## 🛠️ Installation

1. **Azure Setup:**

* [Create an Azure account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
* [Create a Computer Vision resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesComputerVision) and copy your **API Key**.

2. **Clone the project:**

* Open the terminal, navigate to the desired folder, and run:

```bash
git clone https://github.com/nemesis-noctis/LensCore.git

```

* *Alternatively, download the project as a ZIP and extract it.*

3. **Environment Setup:**

* In the root directory, create a `.env` file and add your credentials:

```env
VISION_KEY=YOUR_API_KEY

```

4. **Virtual Environment and Dependencies:**

* Create the virtual environment:

```bash
python -m venv .venv

```

* Activate the environment:
* **Windows:** `.venv\Scripts\activate`
* **Linux/Mac:** `source .venv/bin/activate`
* Install the required packages:

```bash
pip install -r requirements.txt

```

---

## 💻 Execution

1. Run the main command in the terminal:

```bash
python main.py

```

2. The terminal will display a local address. Open it in your browser:

```
Running on http://127.0.0.1:5000

```

* **Note:** *The language selected on the website changes the language used for the search.*

---

## 📬 Contact
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jorgemedeirosqneto/) [![email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:jorgemedeiros.qneto@gmail.com) 

## 📌 Versions

* **0.1** - Initial Release

## ⚖️ License

This project is licensed under the **MIT** License - see the LICENSE file for details.
