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
