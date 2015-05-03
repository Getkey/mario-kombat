# no no no
# Every packet includes a bitfield and a sequence number
# This Class is used to generate 'em
# Thus it is on the receiver's side
# TODO: make this a generator
import bitstring

class remote_seq(object):
	def __init__(self):
		self.ack_field = bitstring.BitArray(length=32)
		self.ack_field.set(True, 31)#debug
		self.ack_field.set(True, 25)#debug
		self.last_ack = 50

	def update_bitfield(self, id):
		ack_pos = id - self.last_ack
		print(ack_pos, id)

		print('field', self.ack_field.bin)
		
		if ack_pos == 0:
			raise EOFError("Ack has already been received")
			#Also raise error when already set in the bit field?
			return# Is return needed?

		if ack_pos > 0:
			print("jouj")
			del self.ack_field[32 - ack_pos:]# Discard olds bits, we only have room for 32 of them
			print('champ', self.ack_field.bin)
			self.ack_field = bitstring.BitArray(ack_pos) + self.ack_field# The bits between id and last_ack are represented as 0s
		elif ack_pos > -32:
			print("lul")
			self.ack_field.set(True, -ack_pos)# set a bit in the ack field
			# TODO: Prendre en compte le 33° bit
		else:
			raise BufferError("Packet is too old")

			# Deleting then adding is more efficient
		print('field', self.ack_field.bin)

	def compose_ack():
		return (self.last_ack, self.ack_field)
