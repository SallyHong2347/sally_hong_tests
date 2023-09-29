# Overview
# This is a pseudo code for LRU distributed cache. It uses deque to track
# usage of each cache and remove content that reaches its life limit and 
# rarely use. The cache also sends replication to other location to reduce 
# loss from crash.


import collections

class LRUDistributedCache:
    def __init__(self, capacity: int, lifelimit: int, resource_manager: str):
        self.capacity = capacity
        self.lifelimit = lifelimit
        self.cache = {} # map that store key-value pair of cached content
        self.LRUOrder = collections.deque()
        self.inserttime = {} # key-value pairs stores insertion time of each element
        self.resource_manager = resource_manager
    
    # remove expired cached element 
    # based on LRUORDER and lifetimes
    def _remove_expire(self):
        while self.LRUOrder:
            key = self.LRUOrder[0]
            if curret_time - self.inserttime[key] > self.lifelimit:
                self.LRUOrder.popleft()
                del self.cache[key]
                del self.inserttime[key]
            else:
                break
    
    # get element from cache
    def get(self, key: str):
        if key in self.cache:
            self.LRUOrder.remove(key)
            self.LRUOrder.append(key)

            return self.cache[key]
        
        content = self.get_from_other_cache(self, key)
        if content == None:
            content = self.get_from_disk(self, key)
        else:
            # check content validity against a shadow copy        
        
        
        return content
    
    # put 
    def put(self, key: str, value: Any):
        self._expire_cache()
        if key in self.cache:
            self.LRUOrder.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest_key = self.order.popleft()
            del self.cache[oldest_key]
            del self.timestamp[oldest_key]
        
        self.cache[key] = value
        self.LRUOrder.append(key)
        self.inserttime[key] = current_time  

        # broadcast change 
        broadcast(key)
    
    # replicate data for security
    def replicate_data(self):
        # replicate data to other nodes


    def get_from_other_cache(self, key:str):
        # fetch data from nearest cache node
        
    
    def send_hearbeat(self):
        # send hearbeat to resource manager
    
    def recovery(self):
        # recovery process

