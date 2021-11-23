"""
Class queue implementation
"""
class Queue:
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
                return self.__item_list.pop(0)
            raise RuntimeError('Queue is empty!')
        except RuntimeError as error:
            print(error)
            raise StopIteration
if __name__ == "__main__":
    q = Queue(10)
    for i in '123456789':
        q.add_item(i)
    for item in q:
        print(item)