class User:
    def __init__(self,name,email,password,job_title):
        self.name = name
        self.email = email
        self.password = password
        self.job_title = job_title
    def change_password(self,new_password):
        self.password = new_password
    def change_job_title(self,change_job_title):
        self.job_title = change_job_title
    def get_info(self):
        print(f"User Name:{self.name}\nUser Email:{self.email}\nUser Job_titile:{self.job_title}\n") 

