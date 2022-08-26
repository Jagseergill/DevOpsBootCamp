class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_current_job_title):
        self.current_job_title = new_current_job_title

    def get_user_info(self):
        print(f"User {self.name} currently working as a {self.current_job_title}. You can reach at "
              f"email {self.email}. Thank you")



