from enum import Enum
from protobuf3.message import Message
from protobuf3.fields import BoolField, EnumField, MessageField, UInt32Field, StringField, Int32Field


class Datagram(Message):

    class Type(Enum):
        POSITION = 1
        HEALTH = 2
        CHAT = 3
        NICKNAME = 4

    class Ack(Message):
        pass


class Position(Message):

    class Character(Message):
        pass


class Health(Message):
    pass


class Chat(Message):

    class Character(Message):
        pass


class GameOver(Message):
    pass

Datagram.Ack.add_field('ack', UInt32Field(field_number=1, required=True))
Datagram.Ack.add_field('ackfield', Int32Field(field_number=2, required=True))
Datagram.add_field('type', EnumField(field_number=1, required=True, enum_cls=Datagram.Type))
Datagram.add_field('ack', MessageField(field_number=2, optional=True, message_cls=Datagram.Ack))
Datagram.add_field('reliable', UInt32Field(field_number=3, optional=True))
Datagram.add_field('position', MessageField(field_number=4, optional=True, message_cls=Position))
Position.Character.add_field('nickname', StringField(field_number=1, required=True))
Position.Character.add_field('x', UInt32Field(field_number=2, required=True))
Position.Character.add_field('y', UInt32Field(field_number=3, required=True))
Position.add_field('character', MessageField(field_number=1, repeated=True, message_cls=Position.Character))
Datagram.add_field('health', MessageField(field_number=5, optional=True, message_cls=Health))
Health.add_field('hp', StringField(field_number=1, required=True))
Datagram.add_field('chat', MessageField(field_number=6, optional=True, message_cls=Chat))
Chat.Character.add_field('nickname', StringField(field_number=1, required=True))
Chat.Character.add_field('msg', StringField(field_number=2, required=True))
Chat.add_field('character', MessageField(field_number=1, repeated=True, message_cls=Chat.Character))
Datagram.add_field('game_over', MessageField(field_number=7, optional=True, message_cls=GameOver))
GameOver.add_field('winner', BoolField(field_number=1, required=True))
