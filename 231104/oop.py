class Client:
    def setName(self, name):
        self.name = name
    def dispName(self):
        print("my name is", self.name)

client = Client()
client.setName("shayan")
client.dispName()