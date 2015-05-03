from protobuf3.message import Message
from enum import Enum
from protobuf3.fields import EnumField, UInt32Field, BytesField, SInt32Field, StringField, MessageField


class Datagram(Message):

    class Type(Enum):
        INPUT = 1
        CHAT = 2
        NICKNAME = 3


class Ack(Message):
    pass


class Input(Message):
    pass


class Chat(Message):
    pass


class Handshake(Message):
    pass

Datagram.add_field('type', EnumField(field_number=1, required=True, enum_cls=Datagram.Type))
Datagram.add_field('ack', MessageField(field_number=2, required=True, message_cls=Ack))
Datagram.add_field('reliable', SInt32Field(field_number=3, optional=True))
Ack.add_field('ack', SInt32Field(field_number=2, required=True))
Ack.add_field('ackfield', BytesField(field_number=3, required=True))
Datagram.add_field('input', MessageField(field_number=5, optional=True, message_cls=Input))
Input.add_field('x', UInt32Field(field_number=1, required=True))
Datagram.add_field('chat', MessageField(field_number=6, optional=True, message_cls=Chat))
Chat.add_field('msg', StringField(field_number=1, required=True))
Datagram.add_field('handshake', MessageField(field_number=7, optional=True, message_cls=Handshake))
Handshake.add_field('nickname', StringField(field_number=1, required=True))
