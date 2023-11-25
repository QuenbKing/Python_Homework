from LRUCache import LRUCache

lru = LRUCache(3)

lru.cache = ("key1", "value1")
lru.cache = ("key2", "value2")
lru.cache = ("key3", "value3")
lru.print_cache()

print(lru.get("key2"))
lru.cache = ("key4", "value4")
lru.print_cache()
