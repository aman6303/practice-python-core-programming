
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId

#loading the dotenv data
load_dotenv()

# Get the connection string safely
connection_string = os.getenv("MONGO_URI")

client = MongoClient(connection_string)

# print(client)
# not a good idea to include id and password in code file

db = client["pythonyoutubemanager"]

video_collection = db["videos"]

# print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Name: {video['name']} and Time: {video['time']}")

def update_video(id, name, time):
    video_collection.update_one({'_id': ObjectId(id)},{'$set': {"name": name, "time": time}})

def delete_video(id):
    video_collection.delete_one({"_id":ObjectId(id)})

def main():
    while True:
        print("youtube manager app ")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_videos()
            
        elif choice == '2':
            name = input("Enter video Name: ")
            time = input("Enter video time: ")
            
            add_video(name, time)
            
        elif choice == '3':
            id = input('Enter the video id to update: ')
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(id, name, time)
            
        elif choice == "4":
            id = input("Enter a video id to delete: ")
            delete_video(id)
            
        elif choice == '5':
            break
        else:
            print("Invalid Input")
            
            

if __name__ == "__main__":
    main()