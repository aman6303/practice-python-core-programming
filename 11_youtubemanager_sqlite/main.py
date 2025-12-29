import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXIST videos(
    id INTERGER PRMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)



def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    cursor.commit()

def update_videos(id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, id))
    cursor.commit()

def delete_videos(id):
    cursor.execute("DELETE FROM videos where id = ?", (id,))
    cursor.commit()

def main():
    while True:
        print("\n youtube manager with db")
        print("1. list videos")
        print("2. add videos")
        print("3. upadate videos")
        print("4. delete videos")
        print("5. exit")

        choice = input("Enter your choice: ")
        match choice:
            case '1': list_videos(videos)
            case '2':
                name = input("Enter the video name ")
                time = input("Enter the video time ")
                add_video(name, time)
            case '3': 
                id = input("Enter video Id to update ")
                name = input("Enter the video name ")
                time = input("Enetr the video time")
                update_videos(videos)

            case '4': 
                id = input("Enter video id to delete ")
                delete_videos(videos)
            case '5': break

            case _: print("Invalid Input")

    con.close()

if __name__ == "__main__":
    main()