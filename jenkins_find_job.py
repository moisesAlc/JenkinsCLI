import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

JENKINS_URL = os.getenv("JENKINS_URL")
USER = os.getenv("JENKINS_USER")
TOKEN = os.getenv("JENKINS_TOKEN")

if not all([JENKINS_URL, USER, TOKEN]):
    raise ValueError("Faltam variáveis no .env (JENKINS_URL, JENKINS_USER, JENKINS_TOKEN)")

auth = HTTPBasicAuth(USER, TOKEN)

def find_job(url, target_name, path=""):
    """
    Busca recursivamente um job pelo nome e retorna o caminho completo.
    """
    resp = requests.get(f"{url}api/json?tree=jobs[name,url,_class]", auth=auth)
    resp.raise_for_status()
    jobs = resp.json().get("jobs", [])

    for job in jobs:
        job_name = job["name"]
        job_url = job["url"]
        job_class = job["_class"]

        # Se for pasta, entra recursivamente
        if "Folder" in job_class:
            result = find_job(job_url, target_name, path + "/" + job_name)
            if result:
                return result
        else:
            # Job real
            if job_name.lower() == target_name.lower():
                return path + "/" + job_name
    return None

if __name__ == "__main__":
    job_name = input("Digite o nome do job que deseja encontrar: ").strip()
    result = find_job(f"{JENKINS_URL}/", job_name)

    if result:
        print(f"✅ Job encontrado: {result}")
    else:
        print("❌ Job não encontrado.")

