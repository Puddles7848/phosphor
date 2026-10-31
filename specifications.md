# Phosphor version 1
## Discovery
On default, phosphor nodes will discover each other on port 42068 (UDP). They will "shout" their Local IP (unsafe?) and their GPG Key Fingerprint. The Key Fingerprint is used for indentification.
## Connecting
Peer to Peer connections are made on port 42069 (TCP). To verify each others' identity, the nodes will challenge each other.
### Challenging
For example, Bob wants to connect to Alice. Alice's computer has already announced their public key. Bob will request Alice's full public key. Bob will generate random information. Alice has to sign this with their match private key to prove that they are really who they say they are.
