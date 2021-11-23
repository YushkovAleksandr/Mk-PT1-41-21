"""
Class stack implementation
"""
class Stack:   
    def __init__(self):
        self.__item_list = []
    def add_item(self, item):
        self.__item_list.append(item)
    def size_list(self):
        return len(self.__item_list)
    def __iter__(self):
        return self
    def __next__(self):
        try:
            while self.__item_list:
                return self.__item_list.pop()
            raise RuntimeError('Empty')
        except RuntimeError as error:
            print(error)
            raise StopIteration

if __name__ == "__main__":
    s = Stack()
    for i in range(10):
        s.add_item(i)
    for item in s:
        print(item)