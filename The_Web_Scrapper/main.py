from wanted import get_wanted_job
from saramin import get_saramin_job
from jobplanet import get_jobplanet_job
from worknet import get_worknet_job
from save import save_to_file

def start_scrapping(job):
    wanted_jobs = get_wanted_job(job)
    saramin_jobs = get_saramin_job(job)
    jobplanet_jobs = get_jobplanet_job(job)
    worknet_jobs = get_worknet_job(job)
    total = wanted_jobs + saramin_jobs + jobplanet_jobs + worknet_jobs
    
    return total




    

    