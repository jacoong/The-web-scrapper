from remoteok import get_remote_job
from weworkremotely import get_weworkremotely_job
from save import save_to_file

def start_scrapping(job):
    wework =get_weworkremotely_job(job)
    remote =get_remote_job(job)
    total = wework + remote
    
    return total




    

    