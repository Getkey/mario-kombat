from protobuf3.fields import Int32Field, MessageField, BoolField, StringField, SInt32Field, EnumField, UInt32Field
from enum import Enum
from protobuf3.message import Message


class Datagram(Message):

    class Type(Enum):
        INPUT = 1
        CHAT = 2
        NICKNAME = 3

    class Ack(Message):
        pass


class Position(Message):

    class Character(Message):
        pass


class Chat(Message):

    class Character(Message):
        pass


class GameOver(Message):
    pass

Datagram.Ack.add_field('ack', SInt32Field(field_number=1, required=True))
Datagram.Ack.add_field('ackfield', Int32Field(field_number=2, required=True))
Datagram.add_field('type', EnumField(field_number=1, required=True, enum_cls=Datagram.Type))
Datagram.add_field('ack', MessageField(field_number=2, optional=True, message_cls=Datagram.Ack))
Datagram.add_field('reliable', SInt32Field(field_number=3, optional=True))
Datagram.add_field('position', MessageField(field_number=4, optional=True, message_cls=Position))
Position.Character.add_field('nickname', StringField(field_number=1, required=True))
Position.Character.add_field('x', UInt32Field(field_number=2, required=True))
Position.Character.add_field('y', UInt32Field(field_number=3, required=True))
Position.add_field('character', MessageField(field_number=1, repeated=True, message_cls=Position.Character))
Datagram.add_field('chat', MessageField(field_number=5, optional=True, message_cls=Chat))
Chat.Character.add_field('nickname', StringField(field_number=1, required=True))
Chat.Character.add_field('msg', StringField(field_number=2, required=True))
Chat.add_field('character', MessageField(field_number=1, repeated=True, message_cls=Chat.Character))
Datagram.add_field('game_over', MessageField(field_number=6, optional=True, message_cls=GameOver))
GameOver.add_field('winner', BoolField(field_number=1, required=True))
