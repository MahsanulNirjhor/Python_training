from user import User
app_user_one = User("Nirjhor","Nirjhor@sagbrain.com","secret","Software Developer")
app_user_one.get_info()

app_user_one.change_job_title("DevOps Engineer")
app_user_one.get_info()