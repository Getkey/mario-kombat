# Mario Kombat : Le retour de Luigi

## Dependancies
* [protobuf3](http://pythonhosted.org/protobuf3/)
* [Protocol Buffers compiler](https://developers.google.com/protocol-buffers/docs/downloads)
* [bitstring](http://scott-griffiths.github.io/bitstring/)

## Get started
### Generate the protocol
```bash
$ protoc --python3_out=protocol/ protocol/server_to_client.proto
$ protoc --python3_out=protocol/ protocol/client_to_server.proto
```

### Work around a bug in protobuf3
TODO: Fix upstream
TODO: clean server/deserialize.py once bug is fixed
In `protobuf3/fields/message.py` edit:
```python
def _validate(self, value):
    return False   # Direct assignment is forbidden
```
to:
```python
def _validate(self, value):
    return True   # Direct assignment is forbidden
```

## Launch it
### Server
```bash
python3 -m server
```

### Client
```bash
```

## TODO:
Switch to Protocol Buffers 3 when it's released to get official support for Python 3.
