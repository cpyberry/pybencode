# pybencode

シンプルなpythonのbencodeライブラリ

![license](https://shields.io/github/license/cpyberry/pybencode)

## 必要環境

* python 3.6, 3.7, 3.8, 3.9

## インストール方法

```shell
pip install cpyberry-pybencode
```

## 使い方

```python
import pybencode


pybencode.encode(256)  # return b"i256e"

pybencode.encode(b"neko")  # return b"4:neko"

pybencode.encode([1, 2, 3])  # return b"li1ei2ei3ee"

pybencode.encode({1: b"kuro", 2: b"sakura"})
# return b"di1e4:kuroi2e6:sakurae"

```

入れ子になったリストや辞書型もエンコード出来ます。

```python
pybencode.encode([b"cat", 1024, [b"meow", b"woof"]])
# return b"l3:cati1024el4:meow4:woofee"

pybencode.encode({1: {b"yuki": b"ghost"}})
# return b"di1ed4:yuki5:ghostee"
```

デコードは上記の逆を行うことができます。

同様に、入れ子になったリストや辞書型もデコード出来ます。

```python
pybencode.decode(b"5:night")  # return "night"
pybencode.decode(b"i128e")  # return 128

python.decode(b"di1ed4:yuki5:ghostee")
# return {1: {b"yuki": b"ghost"}}

python.decode(b"l3:cati1024el4:meow4:woofee")
# return [b"cat", 1024, [b"meow", b"woof"]]
```

文字列をbencode形式にエンコードする場合は、最初に任意の文字コードでエンコードする必要があります。

例えば

```python
string = "coppelia"
pybencode.encode(string.encode("latin-1"))
```
