# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

Str = "allan"
# Counter(): Create a new, empty Counter object(a Dictionary)
myCounter = Counter(Str)
print(myCounter)
print(myCounter.items())
print(myCounter.keys())
print(myCounter.values())
print(myCounter.most_common(2))
print(list(myCounter.elements()))

# namedtuple(): Returns a new subclass of tuple with named fields.
Point = namedtuple('Point', 'x,y')
pt = Point(1, -5)
print(pt)

# OrderedDict(): Dictionary that remembers insertion order
myOrderedDict = OrderedDict()  # Current Python versions also remember the order in a normal Dictionary
myOrderedDict['a'] = 3
myOrderedDict['b'] = 9
print(myOrderedDict)

# defaultdict:  dictionary with default factory
# The default factory is called without arguments to produce a new value when a key is not present
d = defaultdict(int)
d['a'] = 100
d['b'] = 200
print(d)

# deque(): A double-ended queue, has the feature of adding and removing elements from either end
myDeque = deque()

myDeque.append(1)
myDeque.append(2)
myDeque.appendleft(3)

last = myDeque.pop()
first = myDeque.popleft()

print(f"last -> {last}")
print(f"first -> {first}")
print(myDeque)

myDeque.extend([4, 5, 6])
myDeque.extendleft([0, 9])
