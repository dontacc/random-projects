class List:
    def __init__(self, *args):
        self._data = {}
        for arg in args:
            self.append(arg)

    def append(self, value):
        self._data[len(self._data)] = value

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return iter(self._data.values())

    def __delitem__(self, index):
        del self._data[index]

    def __str__(self):
        return str(self._data)


def main():
    """
    we have problem here
    """
    nums = List("salam")
    nums.append(5)
    print(nums)
    del nums[0]
    nums.append(6)
    nums.append(7)
    print(nums)
    # for num in nums:
    #     print(num)


main()
