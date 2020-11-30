from perceval.backends.core.git import Git
from perceval.backends.core.github import GitHub
from collections import Counter
import json

def git_repos():
    users = [] # creating empty lists
    test = []

    #target url"vidyaratna.git"
    repo_url = 'https://github.com/amfoss/vidyaratna.git'

    repo_dir ='/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details

     #target url"cms"
    repo_url = 'https://github.com/amfoss/cms.git'

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details


    #target url""TempleApp"
    repo_url = 'https://github.com/amfoss/TempleApp.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    #target url""website.git"
    repo_url = 'https://github.com/amfoss/website.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
     #target url""WebApp.git"
    repo_url = 'https://github.com/amfoss/WebApp.git'

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    #target url"cms-mobile""
    repo_url = 'https://github.com/amfoss/cms-mobile.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
   
    #target url 
    repo_url = 'https://github.com/amfoss/Praveshan.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/bot.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/tasks.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/star-me.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    
    repo_url = 'https://github.com/amfoss/amdec-website.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/Wiki.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/GitLit.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/Qujini.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/attendance-tracker.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/events.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/Hack4Amrita.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/master-syllabus.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/test-repo.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/webspace.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/internal-hackathon.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/foss-meetups.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/automated-scripts.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/fosswebsite.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/fosster.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/Foss-talks.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/cybergurukulam.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/kdeconf.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/android-workshop-summer-2018.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/App.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/Workshops.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/Wikimedia_Hackathon_Amrita_University.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details
    
    repo_url = 'https://github.com/amfoss/website_old.git' 

    repo_dir = '/perceval.tests' #target directory 

    repo = Git(uri = repo_url, gitpath=repo_dir) #it wil search in git

    for commit in repo.fetch(): # repo.fetch() fetch the commits in the repo (every line)
        users.append(commit['data']['Author']) # collect the data and author details


    for u in Counter(users).keys():
        a = "Commits:" + str(Counter(users).get(u)) + "\t User: " + u + "\n"
        test.append(a) # appending all the fetched commits into 'test' 
       
    return test 
    

def main() :
    test=git_repos() 
    test=''.join(test) 
    open('commits.json','w').write(test)


main()