#import beautifulsoup and request here
import bs4 as bs
import urllib.request
import requests

def displayJobDetails():
    print("Display job details")

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
    url = 'https://www.indeed.com/jobs?q={role}&l={location}'
    url = url.replace("{role}", role)
    url = url.replace("{location}", location)
    # Complete the missing part of this function here
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')


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
    getJobList(role, location)
    
if __name__ == '__main__':
    main()
