import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect("task-database.db")
        self.cursor = self.con.cursor()
        self. create_task_table()
   
    # Creating the task table
    def create_task_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id integer PRIMARY KEY AUTOINCREMENT, task varchar(50) NOT NULL, completed BOOLEAN NOT NULL CHECK (completedIN(0,1)))")
        self.con.commit() 

    # Creating the task
    def create_task(self, task, due_date):
        pass
        
