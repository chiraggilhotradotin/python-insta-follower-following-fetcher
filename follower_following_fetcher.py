import instaloader
import sys
import os
import shutil
if len(sys.argv)==2:
    user = sys.argv[1]
else:
    user = input("Enter username : ")

if not os.path.exists(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}"):
    os.makedirs(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}")

try:
    shutil.copy(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followers.txt",os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followers_backup.txt")
    shutil.copy(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followings.txt",os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followings_backup.txt")
except:
    print(f"You are fetching data for the first time for {user}. So you will not be able to see details.")

f = open(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followers.txt","w")
f.close()
f = open(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followings.txt","w")
f.close()

L = instaloader.Instaloader()
L.login("username", "password")

profile = instaloader.Profile.from_username(L.context, user)


f = open(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followers.txt","a")
followers = profile.get_followers()
for follower in followers:
    f.write(follower.username + "\n")
f.close()


f = open(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followings.txt","a")
followees = profile.get_followees()
for followee in followees:
    f.write(followee.username + "\n")
f.close()

os.system(sys.executable+" "+os.path.dirname(os.path.abspath(__file__))+"/details_shower.py "+user)