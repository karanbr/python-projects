class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, followed_user):
        followed_user.followers += 1
        self.following += 1


user1 = User("001", "karanbr")
user2 = User("002", "peter")

print(user1.username)
print(user1.id)
print(user1.followers)

user1.follow(user2)
print(user1.following)
