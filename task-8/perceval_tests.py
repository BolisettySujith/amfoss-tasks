from perceval.backends.core.git import Git
from perceval.backends.core.github import GitHub
from collections import Counter
import json

def git_repos():
    users = [] # creating empty lists
    test = []
    repo_url = 'https://github.com/amfoss/cms' #target url

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