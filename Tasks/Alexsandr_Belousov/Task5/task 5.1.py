# 1. Binary Search (рекурсивный, в идеале без слайсов)


x = [0,1,2,3,4,5,6,7,8,9]
f = int(input('число от 0 до 9\n'))

def search(x, f):
  left = 0 
  right = len(x)-1
  mid = (left + right)//2
  if (f == x[mid]):
     return mid
  if (f > x[mid]):
     return search(x[mid+1:], f) + (mid + 1)
  return search(x[:mid], f)

if __name__ == '__main__':
    print(search(x,f))