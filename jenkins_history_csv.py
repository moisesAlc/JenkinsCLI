import os
import csv
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from datetime import datetime

# Carrega variáveis do .env
load_dotenv()

JENKINS_URL = os.getenv("JENKINS_URL")
USER = os.getenv("JENKINS_USER")
TOKEN = os.getenv("JENKINS_TOKEN")

if not all([JENKINS_URL, USER, TOKEN]):
    raise ValueError("Faltam variáveis no .env (JENKINS_URL, JENKINS_USER, JENKINS_TOKEN)")

auth = HTTPBasicAuth(USER, TOKEN)
OUTPUT_FILE = "jenkins_builds.csv"

def get_jobs(url, path=""):
    """
    Busca jobs recursivamente.
    Se encontrar folders, entra nelas.
    Retorna uma lista de {name, url, path}.
    """
    jobs_found = []
    resp = requests.get(f"{url}api/json?tree=jobs[name,url,_class]", auth=auth)
    resp.raise_for_status()
    jobs = resp.json().get("jobs", [])

    for job in jobs:
        job_name = job["name"]
        job_url = job["url"]
        job_class = job["_class"]

        if "Folder" in job_class:  # pasta -> recursivo
            jobs_found.extend(get_jobs(job_url, path + "/" + job_name))
        else:  # job real
            jobs_found.append({"name": job_name, "url": job_url, "path": path})
    return jobs_found

def get_builds(job):
    """
    Busca builds de um job específico (últimos 50).
    """
    resp = requests.get(
        f"{job['url']}api/json?tree=builds[number,result,timestamp,duration]{{0,50}}",
        auth=auth
    )
    resp.raise_for_status()
    return resp.json().get("builds", [])

# Escreve CSV
with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # Cabeçalho: Path vem antes do Job
    writer.writerow(["Path", "Job", "Build Number", "Status", "Timestamp", "Duration (s)"])

    all_jobs = get_jobs(f"{JENKINS_URL}/")

    for job in all_jobs:
        print(f"🔍 Coletando builds de: {job['path']}/{job['name']}")
        builds = get_builds(job)

        if not builds:
            writer.writerow([job['path'], job['name'], "-", "NO_BUILDS", "-", "-"])
            continue

        for build in builds:
            num = build["number"]
            result = build.get("result", "IN_PROGRESS")
            ts = datetime.fromtimestamp(build["timestamp"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
            dur = round(build["duration"] / 1000, 2)
            writer.writerow([job["path"], job["name"], num, result, ts, dur])

print(f"\n✅ Histórico exportado para {OUTPUT_FILE}")
