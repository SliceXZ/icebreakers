import json
from django.db import models

class user(models.Model):

    #members
    userID = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    #UserInfo
    fullName = models.CharField(max_length=64)
    gender = models.CharField(max_length=16)
    orientation = models.CharField(max_length=16)
    city = models.CharField(max_length=64)
    lastOnline = models.DateTimeField('last online')
    interests = models.TextField()
    #CalculatedInfo
    interestTree = models.TextField()

    def determineUserInterests(self):
        if self.haveEnoughInterestData():
            return self.pullInterestsFromConversation(self)
        return self.pullInterestsFromProfile(self)

    def determineSharedInterests(self, userInterests):
        sharedInterests = []
        for a in self.interestTree:
            if a in userInterests:
                sharedInterests += a
        return sharedInterests

    def haveEnoughInterestData(self):
        if self.interestTree.recursiveCount() >= 5:
            return True
        return False

    def pullInterestsFromConversation(self):
        return "hello"

    def pullInterestsFromProfile(self):
        newInterests = []
        for interest in self.interests:
            if interest in self.availableInterests:
                newInterests += interest
        return newInterests


    # GETTERS AND SETTERS
    def setinterests(self):
        self.interests = json.dumps(self.determineUserInterests())

    def getinterests(self):
        return json.loads(self.interests)

    def setinterestTree(self):
        self.interests = json.dumps(self.determineUserInterests())

    def getinterestsTree(self):
        return json.loads(self.interestTree)