from typing import List


class Twitter:

    def __init__(self):
        from collections import defaultdict
        self.tweets = {}  # key: userId, value: List[tweetId: int]
        self.follows = defaultdict(set)  # key: userId, value: List[followeeId: int]
        self.tick = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        timestamp = self.tick
        self.tick += 1
        self.tweets[userId].append((tweetId, timestamp))

    def getNewsFeed(self, userId: int) -> List[int]:
        import heapq

        limit = 10
        news_feed_heap = []

        # add userId's own tweets to the news feed heap first
        if self.tweets.get(userId):
            for tweetId, timestamp in self.tweets.get(userId):
                heapq.heappush(news_feed_heap, (-timestamp, tweetId))

        # if userId has followers, add all the tweets of their followers in the heap
        if self.follows.get(userId):
            for followeeId in self.follows.get(userId):
                if self.tweets.get(followeeId):
                    for tweetId, timestamp in self.tweets.get(followeeId):
                        heapq.heappush(news_feed_heap, (-timestamp, tweetId))

        # use the heap to fetch the 10 most recent tweets
        news_feed = []
        while len(news_feed) < limit and len(news_feed_heap) > 0:
            news_feed.append(heapq.heappop(news_feed_heap)[1])

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return

        self.follows[followerId].remove(followeeId)


def testTwitter(actions: List[str], inputs: List, expected: List):
    twitter = None
    for i, action in enumerate(actions):
        if action == "Twitter":
            twitter = Twitter()
        elif action == "postTweet":
            twitter.postTweet(inputs[i][0], inputs[i][1])
        elif action == "getNewsFeed":
            actual = twitter.getNewsFeed(inputs[i][0])
            assert actual == expected[i], f"getNewsFeed failed!: actual: {actual}, expected: {expected[i]}, inputs: {inputs[i]}"
        elif action == "follow":
            twitter.follow(inputs[i][0], inputs[i][1])
        elif action == "unfollow":
            twitter.unfollow(inputs[i][0], inputs[i][1])

    print(f"Test Case Passed!")


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

testTwitter(
    ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"],
    [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]],
    [None, None, [5], None, None, [6, 5], None, [5]]
)
testTwitter(
    ["Twitter", "postTweet", "getNewsFeed", "follow", "getNewsFeed", "unfollow", "getNewsFeed"],
    [[], [1, 1], [1], [2, 1], [2], [2, 1], [2]],
    [None, None, [1], None, [1], None, []]
)
testTwitter(
    ["Twitter", "follow", "getNewsFeed"],
    [[], [1, 5], [1]],
    [None, None, []]
)
testTwitter(
    ["Twitter", "postTweet", "postTweet", "getNewsFeed"],
    [[], [1, 5], [1, 3], [1]],
    [None, None, None, [3, 5]]
)
# testTwitter(
#     ["Twitter", "postTweet", "postTweet", "unfollow", "getNewsFeed"],
#     [[], [1, 4], [2, 5], [1, 2], [1]],
#     [[], [1, 4], [2, 5], [1, 2], [1]]
# )
