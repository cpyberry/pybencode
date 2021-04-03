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
