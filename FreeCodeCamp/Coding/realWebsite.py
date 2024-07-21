from bs4 import BeautifulSoup
import requests

# READING CONTENT FROM WEBSITE
html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=")
# print(html_text)      # <Response [200]> = this means we have successfully connected to the website
html_text = html_text.text # .text = this will print the html content of the website
# print(html_text) 

# CREATING INSTANCE OF BEAUTIFULSOUP
soup = BeautifulSoup(html_text, 'lxml')

# FINDING JOBS
jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

# PRINTING JOBS
for job in jobs:
    publishData = job.find("span", class_="sim-posted").span.text
    if("few" in publishData): # Finding only jobs that are posted few days ago
        companyName = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")#.replace=remove spaces
        skillsRequired = job.find("span", class_="srp-skills").text.replace(" ", "")
        jobLocationsUl = job.find("ul", class_='top-jd-dtl clearfix')
        jobLocation = jobLocationsUl.find_all("li")[-1].text.replace("location_on", "")
        print(f'''
Company Name: {companyName.strip()}
Required Skills: {skillsRequired.strip()}
Published Date: {publishData.strip()}
Job Location: {jobLocation.strip()}
            ''')     # .strip() to remove leading and trailing spaces