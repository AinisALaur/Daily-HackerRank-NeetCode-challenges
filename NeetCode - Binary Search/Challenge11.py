class TimeMap:
    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = [[value, timestamp]]
        else:
            self.mapping[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        values = self.mapping.get(key, [])
        h = len(values) - 1
        res = ""

        while l <= h:
            m = l + (h - l) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                if values[m][1] == timestamp:
                    break
                l = m + 1
            else:
                h = m - 1

        return res