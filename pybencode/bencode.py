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

		Todo:
			* Create a function that automatically determines types and converts it to bencode format
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

		Todo:
			* Create a function that automatically determines types and converts it to bencode format
		"""
		data = b""
		for key, value in dictionary.items():
			encode_key = cls.encode(key)
			encode_value = cls.encode(value)
			data += encode_key + encode_value

		return b"d" + data + b"e"
