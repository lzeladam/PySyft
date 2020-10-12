import weakref

import syft as sy
from nacl.signing import SigningKey, VerifyKey

# generate a signing key
signing_key = SigningKey.generate()
verify_key = signing_key.verify_key

node = sy.Network(name="OpenMined", verify_key=verify_key)