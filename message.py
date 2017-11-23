from skpy import Skype
sk = Skype("xxxxx", "yyyy")
ch = sk.chats.create()
ch.sendMsg("Changed Backgroungimage on desktop!")
print("Message send")
