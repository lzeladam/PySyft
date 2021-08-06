# stdlib
from typing import Any
from typing import Optional

# third party
from nacl.signing import SigningKey

# syft absolute
# syft
from syft.core.common.message import ImmediateSyftMessageWithReply
from syft.core.io.address import Address
from syft.core.node.common.action.exception_action import ExceptionMessage
from syft.lib.python.dict import Dict

# grid absolute
from app.core.node import get_client


def send_message_with_reply(
    signing_key: SigningKey,
    message_type: ImmediateSyftMessageWithReply,
    address: Optional[Address] = None,
    reply_to: Optional[Address] = None,
    **content: Any
) -> Dict:
    client = get_client(signing_key)

    if address is None:
        address = client.address
    if reply_to is None:
        reply_to = client.address

    msg = message_type(address=address, reply_to=reply_to, **content)
    reply = client.send_immediate_msg_with_reply(msg=msg)

    check_if_syft_reply_is_exception(reply)
    return reply


def check_if_syft_reply_is_exception(reply: Dict) -> None:
    if isinstance(reply, ExceptionMessage):
        raise Exception(reply.exception_msg)
