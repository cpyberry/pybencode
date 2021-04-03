ENCODING = "ascii"


class Encode:
	@staticmethod
	def encode_bytes(data: bytes) -> bytes:
		"""Convert bytes type to bencode format

		Args:
			data (bytes): you want to convert to bencode format

		Returns:
			bytes: bencode format
		"""
		data_len = str(len(data)).encode(ENCODING)
		return data_len + b":" + data

	@staticmethod
	def encode_integer(integer: int) -> bytes:
		"""Convert int type to bencode format

		Args:
			integer (int): you want to convert to bencode format

		Returns:
			bytes: bencode format
		"""
		integer = str(integer).encode(ENCODING)
		return b"i" + integer + b"e"

	@classmethod
	def encode_list(cls, lst: bytes) -> bytes:
		"""Convert list type to bencode format

		Args:
			lst (bytes): you want to convert to bencode format

		Returns:
			bytes: bencode format
		"""
		data = b""
		for value in lst:
			add_data = cls.encode(value)
			data += add_data

		return b"l" + data + b"e"

	@classmethod
	def encode_dictionary(cls, dictionary: dict) -> bytes:
		"""Convert dict type to bencode format

		Args:
			dictionary (dict): you want to convert to bencode format

		Returns:
			bytes: bencode format
		"""
		data = b""
		for key, value in dictionary.items():
			encode_key = cls.encode(key)
			encode_value = cls.encode(value)
			data += encode_key + encode_value

		return b"d" + data + b"e"

	@classmethod
	def encode(cls, value) -> bytes:
		"""Convert various types to bencode format

		Args:
			value: you want to convert to bencode format

		Raises:
			ValueError: unexpected type

		Returns:
			bytes: bencode format
		"""
		value_type = type(value)
		functions = {
			bytes: cls.encode_bytes,
			int: cls.encode_integer,
			list: cls.encode_list,
			dict: cls.encode_dictionary
		}

		for key in functions:
			if value_type == key:
				encode_data = functions[key](value)
				break
		else:
			raise TypeError(f"unexpected type: {value_type}")

		return encode_data


class Decode:
	@staticmethod
	def decode_bytes(data: bytes) -> tuple:
		"""Convert bencode format to bytes decoded and the rest of bencode format

		Args:
			data (bytes): bencode format

		Returns:
			tuple: bytes decoded and the rest of bencode format
		"""
		data_len, data_all = data.split(b":", 1)
		data_len = int(data_len)

		data_content = data_all[:data_len]
		data_remain = data_all[data_len:]

		return data_content, data_remain

	@staticmethod
	def decode_integer(data: bytes) -> tuple:
		"""Convert bencode format to int decoded and the rest of bencode format

		Args:
			data (bytes): bencode format

		Returns:
			tuple: int decoded and the rest of bencode format
		"""
		data_integer, data_remain = data.split(b"e", 1)

		# skip b"i"
		data_integer = int(data_integer[1:])
		return data_integer, data_remain

	@classmethod
	def decode_list(cls, data: bytes) -> tuple:
		"""Convert bencode format to list decoded and the rest of bencode format

		Args:
			data (bytes): bencode format

		Returns:
			tuple: list decoded and the rest of bencode format

		Todo:
			* Create a function that automatically determines types and converts bencode format to it
		"""
		contents = []

		# skip b"l"
		data = data[1:]
		while data and (not data.startswith(b"e")):
			content, remain = cls.decode(data)
			contents.append(content)
			data = remain

		# skip b"e"
		remain = data[1:]

		return contents, remain

	@classmethod
	def decode_dictionary(cls, data: bytes) -> tuple:
		"""Convert bencode format to dict decoded and the rest of bencode format

		Args:
			data (bytes): bencode format

		Returns:
			tuple: dict decoded and the rest of bencode format
		"""
		content = {}

		# get a list with the contents of key, value, key, value ...
		items, remain = cls.decode_list(data)

		for key_index in range(0, len(items), 2):
			key = items[key_index]
			content[key] = items[key_index + 1]

		return content, remain
