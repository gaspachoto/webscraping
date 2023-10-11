import time

from bs4 import BeautifulSoup
import requests

# print('Enter a skill you are not familiar with')
# unfamiliar_skill = input('>>>')
# print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    html_text = requests.get('https://www.jobs.bg/front_job_search.php?subm=1&categories%5B%5D=56&techs%5B%5D=Python').text
    soup = BeautifulSoup(html_text, 'lxml')
    all_jobs = soup.find('ul', class_='page-1')
    jobs = all_jobs.find_all('li')[3:]

    for index, job in enumerate(jobs):
        published_date = job.find('div', class_='card-date').text.split()[0].replace(' ', '')
        if 'днес' in published_date:
            company_name = job.find('div', class_='secondary-text').text
            skills = job.find_all('div', class_='skill')
            more_info = job.div.a['href']
            with open(f'posts/{index}.text', 'w') as f:
                f.write(f"Company name: {company_name}")
                f.write(f"\nSkills: {skills}")
                f.write(f"\nPublished date: {published_date}")
                f.write(f"\nMore info: {more_info}")
            print(f'File {index} saved.')


if __name__ == '__main__':
    while True:
        find_jobs()
        time.sleep(60)