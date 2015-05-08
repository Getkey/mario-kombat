# no no no
# Every packet includes a bitfield and a sequence number
# This Class is used to generate 'em
# Thus it is on the receiver's side
# TODO: make this a generator
import bitstring

UINT32MAX = 2**32 - 1

class remote_seq(object):
	def __init__(self):
		self.ack_field = bitstring.BitArray(length=32)
		self.ack_field.set(True, 31)#debug
		self.ack_field.set(True, 25)#debug
		self.last_ack =  UINT32MAX - 2

	def update_bitfield(self, id):
		ack_pos = id - self.last_ack

		if ack_pos > UINT32MAX / 2:
			ack_pos -= UINT32MAX
		elif ack_pos < - (UINT32MAX / 2):
			ack_pos += UINT32MAX

		print('At first I was like', self.ack_field.bin)

		if ack_pos == 0:
			raise EOFError("Ack has already been received")

		if ack_pos >= 32:
			self.ack_field = bitstring.BitArray(length=32)
		elif ack_pos > 0:
			print("More recent than last_ack")
			del self.ack_field[32 - ack_pos:]# Discard olds bits, we only have room for 32 of them
			self.ack_field = bitstring.BitArray(ack_pos) + self.ack_field# The bits between id and last_ack are 0s
		elif ack_pos > -32:
			print("In the field")
			if self.ack_field[-ack_pos] != True:
				self.ack_field.set(True, -ack_pos)# set a bit in the ack field
			else:
				raise EOFError("Ack has already been received")
		else:
			raise BufferError("Packet is too old")

			# Deleting then adding is more efficient
		print('But then I was like', self.ack_field.bin)

	def compose_ack():
		return (self.last_ack, self.ack_field)

class local_seq(object):
	def __init__(self):
		self.id = 1#Uses 1 instead of 0 as first number because of a weakness in protobuf3

	def get_id(self):
		to_return = self.id

		self.id += 1
		if self.id > UINT32MAX:# Max value for an int32
			self.id = 0

		return to_return
