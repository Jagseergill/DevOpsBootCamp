from user import User
from post import Post

app_user_one = User("js@js.com", "Jagseer Singh", "pwd", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "James Bond", "supersecret", "Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()
