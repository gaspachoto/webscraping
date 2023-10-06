from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.jobs.bg/front_job_search.php?subm=1&categories%5B%5D=56&techs%5B%5D=Python').text
soup = BeautifulSoup(html_text, 'lxml')
all_jobs = soup.find('ul', class_='page-1')
jobs = all_jobs.find_all('li')[3:]

for job in jobs:
    published_date = job.find('div', class_='card-date').text.split()[0].replace(' ', '')
    if 'днес' in published_date:
        company_name = job.find('div', class_='secondary-text').text
        skills = job.find_all('div', class_='skill')
        print(f'''
        Company Name: {company_name}
        Required Skills: {skills}
        Published Date: {published_date}
        ''')