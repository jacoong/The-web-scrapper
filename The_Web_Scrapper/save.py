import csv

def save_to_file(jobs):
    file = open("jobs.csv" , mode="w", encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(["Company", "Position", "Location", "Experience", "Requirements", "Main Tasks", "Salary", "Link", "Source"])
    print(jobs)
    for job in jobs:
        writer.writerow([
            job.get('company', 'N/A'),
            job.get('position', 'N/A'),
            job.get('location', 'N/A'),
            job.get('experience', 'N/A'),
            job.get('requirements', 'N/A'),
            job.get('main_tasks', 'N/A'),
            job.get('salary', 'N/A'),
            job.get('link', 'N/A'),
            job.get('source', 'N/A')
        ])
    return