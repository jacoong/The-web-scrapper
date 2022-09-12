from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        company_positions = soup.find_all("td", "company_and_position")
        jobs = []
        for job in company_positions[1:]:
            jobs.append(jobs_detail(job))
        return jobs

    else:
        print("Can't get jobs.")


def jobs_detail(job):
    company = job.find("h3").get_text(strip=True)
    position = job.find("h2").get_text(strip=True)
    link = job.find("a", "preventLink")['href']
    region_pay = job.find_all("div","location")
    location = region_pay[0].text
    pay = region_pay[-1].text
    if (location == pay):
        location = ""
    
        
    return {'company':company,'position':position,'location':location,'link':f'https://remoteok.com/{link}'}

def get_remote_job(word):
    return (extract_jobs(word))