from wanted import get_wanted_job
from saramin import get_saramin_job
from remoteok import get_remoteok_job
from weworkremotely import get_weworkremotely_job
from save import save_to_file

def start_scrapping(job):
    wanted_jobs = get_wanted_job(job)
    saramin_jobs = get_saramin_job(job)
    remoteok_jobs = get_remoteok_job(job)
    weworkremotely_jobs = get_weworkremotely_job(job)
    total = wanted_jobs + saramin_jobs + remoteok_jobs + weworkremotely_jobs
    
    return total




    

    