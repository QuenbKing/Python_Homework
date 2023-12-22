class MyDict(dict):

    def get(self, key, value=0):
        if key not in self:
            return value
        else:
            return self[key]
