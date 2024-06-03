#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Twitter:
    def __init__(self) -> None:
        self.feed = {}
        self.followers = {}

    # Compose a new tweet
    def postTweet(self, userId: int, tweetId: int):
        # Code here
        if userId not in self.feed:
            self.feed[userId] = []
        self.feed[userId].append(tweetId)
        
    # Retrieve the 10 most recent tweet ids as mentioned in question
    def getNewsFeed(self, userId: int):
        # Code here
        #print(self.feed[userId][::-1])
        #print(self.feed[userId][-10:][::-1])
        return self.feed[userId][-10:][::-1]
        
    # Follower follows a followee. If the operation is invalid, it should be a no-op.
    def follow(self, followerId: int, followeeId: int):
        # Code here
        if followerId not in self.followers:
            self.followers[followerId] = []
        self.followers[followerId].append(followeeId)
        
    # Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    def unfollow(self, followerId: int, followeeId: int):
        # Code here
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    obj = Twitter()
    totalQueries = int(input ())
    for _ in range (totalQueries):
        query = list(map(int, input().split()))
        if (query[0] == 1):
            userId, tweetId = query[1], query[2]
            obj.postTweet(userId, tweetId)
        elif (query[0] == 2):
            userId =  query[1]
            vec = obj.getNewsFeed(userId)
            for val in vec:
                print(val, end = ' ')
            print()
        elif (query[0] == 3):
            follower, followee = query[1], query[2]
            obj.follow(follower, followee)
        else:
            follower, followee = query[1], query[2]
            obj.unfollow(follower, followee)
# } Driver Code Ends



# Tested inputs :
'''
6
# Post user 1 tweet 5
1 1 5
# News feed 1
2 1
# postTweet user 2 tweet 6
1 2 6
# News feed 1
2 1
# Unfollow
4 1 2
# News feed 1
2 1
'''
'''
7
1 1 5
2 1
3 1 2
1 2 6
2 1
4 1 2
2 1
'''
