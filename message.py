from skpy import Skype
sk = Skype("boristimp@gmail.com", "skype2301")
ch = sk.chats.create()
ch.sendMsg("Changed Backgroungimage on desktop!")
print("Message send")