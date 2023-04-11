from secp256k1 import PrivateKey, PublicKey
import time, json, hashlib
from websocket import create_connection

def create_keypair():
    privkey = PrivateKey()
    privkey_ser = privkey.serialize()

    pubkey = privkey.pubkey
    pub = pubkey.serialize(compressed=True).hex()[2:]

    keypair = {
                "private_key" : privkey_ser, 
                "pub_key" : pub
               }
    return keypair

def create_timestamp():
    ts = int(time.time())
    return ts

def get_event_kind(type):
    if type == "short_note":
        kind = 1
    elif type == "long_form":
        kind = 30023
    elif type == "badge_definition":
        kind = 30009
    elif type == "badge_award":
        kind = 8
    elif type == "profile_badge":
        kind = 30008
    
    return kind


def create_event_id(pub, ts, kind, tags, content):
    # creating event_id
    # serialize
    # convert to bytes
    # encode to utf-8
    # hash
    # finally, hex. that creates the event_id
    event_data = json.dumps([0, pub, ts, kind, tags, content], separators=(',', ':'))
    event_id = hashlib.sha256(event_data.encode('utf-8')).hexdigest()
    return event_id

# creating signature
def create_signature(event_id, private_key):
    id_bytes = (bytes(bytearray.fromhex(event_id)))
    private_key = PrivateKey(bytes(bytearray.fromhex(private_key)), raw=True)
    sig = private_key.schnorr_sign(id_bytes, bip340tag='', raw=True)
    sig = sig.hex()
    return sig

def broadcast_event(event, relay_uri):
    ws = create_connection(f"{relay_uri}")

    ws.send(
        json.dumps(
            [
                "EVENT", 
                event
            ]
        ).encode('utf-8')
    )

    result =  ws.recv()
    print("Received '%s'" % result)
    ws.close()

def publish_short_note(private_key, public_key, relay_uri, content, tags):
    ts = create_timestamp()
    kind = get_event_kind("short_note")
    event_id = create_event_id(public_key, ts, kind, tags, content)
    print(event_id)
    sig = create_signature(event_id, private_key)
    event = {"id":event_id,"pubkey":public_key,"created_at":ts,"kind":kind,"tags": tags,"content":content,"sig":sig}
    broadcasted_event = broadcast_event(event, relay_uri)
    event_data = {"event":event, "event_broadcast" : broadcasted_event}
    return event_data

def publish_longform_note(private_key, public_key, relay_uri, content, tags):
    ts = create_timestamp()
    kind = get_event_kind("long_form")
    event_id = create_event_id(public_key, ts, kind, tags, content)
    sig = create_signature(event_id, private_key)
    event = {"id":event_id,"pubkey":public_key,"created_at":ts,"kind":kind,"tags": tags,"content":content,"sig":sig}
    broadcasted_event = broadcast_event(event, relay_uri)
    event_data = {"event":event, "event_broadcast" : broadcasted_event}
    return event_data

def publish_badge_definition(private_key, public_key, relay_uri, content, tags):
    ts = create_timestamp()
    kind = get_event_kind("badge_definition")
    event_id = create_event_id(public_key, ts, kind, tags, content)
    sig = create_signature(event_id, private_key)
    event = {"id":event_id,"pubkey":public_key,"created_at":ts,"kind":kind,"tags": tags,"content":content,"sig":sig}
    broadcasted_event = broadcast_event(event, relay_uri)
    event_data = {"event":event, "event_broadcast" : broadcasted_event}
    return event_data

def publish_badge_award(private_key, public_key, relay_uri, content, tags):
    ts = create_timestamp()
    kind = get_event_kind("badge_award")
    event_id = create_event_id(public_key, ts, kind, tags, content)
    sig = create_signature(event_id, private_key)
    event = {"id":event_id,"pubkey":public_key,"created_at":ts,"kind":kind,"tags": tags,"content":content,"sig":sig}
    broadcasted_event = broadcast_event(event, relay_uri)
    event_data = {"event":event, "event_broadcast" : broadcasted_event}
    return event_data

def publish_profile_badge(private_key, public_key, relay_uri, content, tags):
    ts = create_timestamp()
    kind = get_event_kind("profile_badge")
    event_id = create_event_id(public_key, ts, kind, tags, content)
    sig = create_signature(event_id, private_key)
    event = {"id":event_id,"pubkey":public_key,"created_at":ts,"kind":kind,"tags": tags,"content":content,"sig":sig}
    broadcasted_event = broadcast_event(event, relay_uri)
    event_data = {"event":event, "event_broadcast" : broadcasted_event}
    return event_data
