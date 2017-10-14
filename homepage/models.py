import json
from django.db import models
import datetime
from django.utils import timezone

class user(models.Model):

    #members
    userID = models.CharField(max_length=16, default="foo")
    password = models.CharField(max_length=32, default="password")
    #UserInfo
    fullName = models.CharField(max_length=64, default="craig")
    gender = models.CharField(max_length=16, default="male")
    orientation = models.CharField(max_length=16, default="straight")
    city = models.CharField(max_length=64, default="Mars")
    lastOnline = models.DateTimeField('last online', default=timezone.now)
    interests = models.TextField(default="None")
    aboutMe = models.TextField(default="I did not write an about me")
    #CalculatedInfo
    interestTree = models.TextField(default="")

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