from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={term}"
    request = requests.get(url, headers={"User-Agent": "Kimchii"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")

        job_list = soup.find_all("li","feature")
        
        jobs = []

        for job in job_list:
            jobs.append(jobs_detail(job))
        return jobs

    else:
        print("Can't get jobs.")


def jobs_detail(job):
    company = job.find("span","company").text
    position = job.find("span","title").text
    location = job.find("span","region").text
    links = job.find_all("a")

    link = links[1].get('href')

    return {'company':company,'position':position,'location':location,'link':f'https://weworkremotely.com/{link}'}

def get_weworkremotely_job(word):
    return extract_jobs(word)