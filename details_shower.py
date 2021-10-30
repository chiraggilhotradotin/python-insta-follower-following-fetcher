import os
import sys
if len(sys.argv)==2:
    user = sys.argv[1]
else:
    user = input("Enter username : ")
f = open(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followers.txt","r")
followers = f.read().split("\n")
f.close()
f = open(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followings.txt","r")
followings = f.read().split("\n")
f.close()

if os.path.exists(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followers_backup.txt"):
    f = open(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followers_backup.txt","r")
    followersbackup = f.read().split("\n")
    f.close()
else:
    followersbackup = []

if os.path.exists(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followings_backup.txt"):
    f = open(os.path.dirname(os.path.abspath(__file__))+f"/accounts/{user}/followings_backup.txt","r")
    followingsbackup = f.read().split("\n")
    f.close()
else:
    followingsbackup = []
followings.remove("")
followers.remove("")

ings = set(followings)
ers = set(followers)

ingsbackup = set(followingsbackup)
ersbackup = set(followersbackup)

print("Who don't follow you back\n")
for i in ings - ers:
    print(i)


print("\n\n\nYou don't follow them back\n")
for i in ers - ings:
    print(i)


print("\n\n\nUnfollowed by")
for i in ersbackup - ers:
    print(i)


print("\n\n\nYou unfollowed")
for i in ingsbackup - ings:
    print(i)


print("\n\n\nNew followers\n")
if len(ersbackup)==0:
    for i in ers - ersbackup:
        print(i)


print("\n\n\nNew following\n")
if len(ingsbackup)==0:
    for i in ings - ingsbackup:
        print(i)