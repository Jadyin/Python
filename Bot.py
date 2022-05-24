# importing the module 
import praw  
# initialize with appropriate values 
client_id = "MDWbffUu3VkHWaBzBztQAle" 
client_secret = "IaFIqNQJUSHiwfoOrK3erM1Vy2YslQ" 
username = "Jadyin" 
password = "Dovah8320" 
user_agent = "fhTdafZI-0ClEzzYORfBSCR7x3M" 



  
# creating an authorized reddit instance 
reddit = praw.Reddit(client_id = client_id,  
                     client_secret = client_secret,  
                     username = username,  
                     password = password, 
                     user_agent = user_agent) 
                     
# to find the top most submission in the subreddit "Skaven" 
subreddit = reddit.subreddit('Skaven') 
for submission in subreddit.top(limit = 1): 
    # displays the submission title 
    print(submission.title)   
    # displays the net upvotes of the submission 
    print(submission.score)   
    # displays the submission's ID 
    print(submission.id)    
    # displays the url of the submission 
    print(submission.url)  
 

# Obtain the moderator listing for r/redditdev

for moderator in reddit.subreddit("redditdev").moderator():

    print(moderator)