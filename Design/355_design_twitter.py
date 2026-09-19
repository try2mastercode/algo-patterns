import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId):
        heap = []
        users = self.following[userId] | {userId}
        for user in users:
            for tweet in self.tweets[user][-10:]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)
        return [tid for _, tid in sorted(heap)]

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)


tw = Twitter()
tw.postTweet(1, 5)
assert tw.getNewsFeed(1) == [5]
tw.follow(1, 2)
tw.postTweet(2, 6)
assert tw.getNewsFeed(1) == [6, 5]
tw.unfollow(1, 2)
assert tw.getNewsFeed(1) == [5]
print("All tests passed")
