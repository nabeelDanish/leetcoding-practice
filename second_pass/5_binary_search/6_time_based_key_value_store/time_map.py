class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.map.get(key):
            self.map[key].append([value, timestamp])
        else:
            self.map[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key)
        if not values:
            return ""
        
        min_found = ""
        n = len(values)
        start = 0
        end = n - 1

        while start <= end:
            mid = (start + end) // 2
            if values[mid][1] <= timestamp:
                min_found = values[mid][0]
                start = mid + 1
            else:
                end = mid - 1

        return min_found
        


class TestTimeMap:
    @classmethod
    def test_time_map(cls, commands, inputs, expected):
        time_map = None

        for i, command in enumerate(commands):
            if command == "TimeMap":
                time_map = TimeMap()
            elif command == "set":
                time_map.set(inputs[i][0], inputs[i][1], inputs[i][2])
            else:
                actual = time_map.get(inputs[i][0], inputs[i][1])
                assert actual == expected[i], f"Test Case Failed! actual: {actual} expected: {expected[i]}"

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


TestTimeMap.test_time_map(
    ["TimeMap", "set", "get", "get", "set", "get", "get"],
    [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]],
    [None, None, "bar", "bar", None, "bar2", "bar2"]
)
