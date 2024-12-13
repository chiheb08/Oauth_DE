# OAuth for Data Engineers

This repository provides a simple implementation of OAuth using Python, Flask, and GitHub to help break down and explain the concept.

## Running the Project

Follow the steps below to set up and run the project:

### 1. Create a Virtual Environment

```bash
conda create --name github_oauth python=3.10
```

### 2. Install Dependencies

Activate your virtual environment and install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Generate a Self-Signed Certificate

Run the following command to generate a self-signed certificate:

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
```

### 4. Run the Project

Start the application by running:

```bash
python testapp.py
```


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mhamdi-chiheb/)

[![github](https://img.shields.io/badge/Github_account-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/chiheb08/) 


[![medium](https://img.shields.io/badge/medium_articles-000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@chiheb.mhamdi) 




