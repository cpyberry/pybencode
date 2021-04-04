# pybencode

Simple bencode library for python

## Usage

```python
import pybencode


pybencode.encode(256)  # return b"i256e"

pybencode.encode(b"neko")  # return b"4:neko"

pybencode.encode([1, 2, 3])  # return b"li1ei2ei3ee"

pybencode.encode({1: b"kuro", 2: b"sakura"})
# return b"di1e4:kuroi2e6:sakurae"

```

Nested lists and dicts can also be encoded.

```python
pybencode.encode([b"cat", 1024, [b"meow", b"woof"]])
# return b"l3:cati1024el4:meow4:woofee"

pybencode.encode({1: {b"yuki": b"ghost"}})
# return b"di1ed4:yuki5:ghostee"
```

Decode can do the opposite of the above.

Similarly, you can decode nested list and dict.

```python
pybencode.decode(b"5:night")  # return "night"
pybencode.decode(b"i128e")  # return 128

python.decode(b"di1ed4:yuki5:ghostee")
# return {1: {b"yuki": b"ghost"}}

python.decode(b"l3:cati1024el4:meow4:woofee")
# return [b"cat", 1024, [b"meow", b"woof"]]
```

If you want to encode the string to bencode format, you need to encode it with any character code first.

For example

```python
string = "coppelia"
pybencode.encode(string.encode("latin-1"))
```
