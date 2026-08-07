class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.listcache = []   # least recent -> most recent


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # move key to most recent
        self.listcache.remove(key)
        self.listcache.append(key)

        return self.cache[key]


    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            # update value
            self.cache[key] = value

            # move to most recent
            self.listcache.remove(key)
            self.listcache.append(key)

        else:
            # if full, remove least recent
            if len(self.cache) == self.capacity:
                oldest = self.listcache.pop(0)
                del self.cache[oldest]

            # add new item
            self.cache[key] = value
            self.listcache.append(key)