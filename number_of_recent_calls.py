"""
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.

Example 1:

    Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
    Output: [null,1,2,3,3]
"""

class RecentCounter(object):

    def __init__(self):
        self.q = []
        #self.count = 0   # Not needed


    def ping(self, t):
        self.q.append(t)
        #self.count += 1   # Not needed
        while self.q[0] < t-3000:
            #print("1st", self.q[0])   # Not needed
            self.q.pop(0)
        #    print("q", self.q)   # Not needed
        #print("count", self.count)   # Not needed
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


obj = RecentCounter()
param_1 = obj.ping(5)
param_1 = obj.ping(7)
param_1 = obj.ping(4000)
param_1 = obj.ping(5000)
print(param_1)
