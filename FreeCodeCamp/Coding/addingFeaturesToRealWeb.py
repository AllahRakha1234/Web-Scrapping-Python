from bs4 import BeautifulSoup
import requests
import time

# READING CONTENT FROM WEBSITE
html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=")
# print(html_text)      # <Response [200]> = this means we have successfully connected to the website
html_text = html_text.text # .text = this will print the html content of the website
# print(html_text) 

# CREATING INSTANCE OF BEAUTIFULSOUP
soup = BeautifulSoup(html_text, 'lxml')

# FUNCTION TO FIND JOBS
def find_jobs():
    # FINDING JOBS
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    # TAKING UNFAMILIEAR SKILL AS INPUT FROM USER
    print("Enter skill you are not familiar with: ")
    unfamiliar_skill = input(">")
    print(f'Filtering out {unfamiliar_skill}')
    # PRINTING JOBS
    for index, job in enumerate(jobs):
        publishData = job.find("span", class_="sim-posted").span.text
        if("few" in publishData): # Finding only jobs that are posted few days ago
            companyName = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")#.replace=remove spaces
            skillsRequired = job.find("span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a['href'] # Getting the link of the job
            jobLocationsUl = job.find("ul", class_='top-jd-dtl clearfix')
            jobLocation = jobLocationsUl.find_all("li")[-1].text.replace("location_on", "")
            if unfamiliar_skill not in skillsRequired:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {companyName.strip()} \n')
                    f.write(f'Required Skills: {skillsRequired.strip()} \n')
                    f.write(f'Published Date: {publishData.strip()} \n')
                    f.write(f'More Info: {more_info} \n')
                    f.write(f'Job Location: {jobLocation.strip()} \n')
                print(f'File saved: {index}')
                # print(f'Company Name: {companyName.strip()}')
                # print(f'Required Skills: {skillsRequired.strip()}')
                # print(f'Published Date: {publishData.strip()}')
                # print(f'More Info: {more_info}')
                # print()    
                
                
# CALLING FUNCTION
if __name__ == '__main__':
    while True:
        find_jobs()
        waiting_time = 0.1
        print(f"Waiting {waiting_time} minutes...")
        time.sleep(waiting_time * 60)