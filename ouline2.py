#import beautifulsoup and request here
import bs4 as bs
import urllib.request

def displayJobDetails():
    print("Display job details")

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
    url = f'https://www.indeed.com/jobs?q={role}&l={location}'
    url = url.replace(" ", "%20")
    # Complete the missing part of this function here
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'html.parser')
    
    jobs = []

    for job in soup.find_all('div', class_='slider_item'):
        title = "Title: "+job.find('h2', class_= 'jobTitle').text
        company = "Company: "+job.find('span', class_= 'companyName').text
        description = "Description: "+job.find('div', class_= 'job-snippet').text
        if job.find('div', class_= 'salary-snippet-container') != None:
            salary = "Salary: "+job.find('div', class_= 'salary-snippet-container').text
        else: salary = "Salary: Not Provided"
        job = [title, company, description, salary]
        jobs.append(job)

    return jobs

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter location: ")
    location = input()
    print("Job role: ", role)
    print("location: ", location)
    print("\n\nResults:\n\n")
    jobs = getJobList(role,location)
    for job in jobs:
        for detail in job:
            print(detail)
        print("\n\n")
    
if __name__ == '__main__':
    main()
