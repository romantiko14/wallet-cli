# Wallet-cli & TRON Account Documentation

Welcome to the extended developer reference guide for `wallet-cli` and the TRON Account Model. This document details account architectures, cryptographic key pair generation, address format conversions, and active environments using the Shasta Testnet.

---

## 1. The TRON Account Model

TRON utilizes an **account model** where the address of an account serves as its unique identifier. Operating an account requires a valid private key cryptographic signature. 

### Account Attributes
Every account on the TRON network tracks several core data structures and parameters:
* **Token Balances:** TRX native coin, TRC-10, and TRC-20 token asset balances.
* **Network Resources:** Accumulated Bandwidth and Energy metrics used to fuel network execution.
* **Smart Contracts:** The structural capability to deploy smart contracts and trigger existing transactions released on-chain.
* **Governance Layer:** The ability to apply to become a Super Representative (SR) or vote for elected nodes.

---

## 2. Account Types

TRON supports two primary account models. Both types possess the capability to receive, hold, and send TRX/tokens, as well as execute transaction payloads.

| Account Type | Functional Description | Control Mechanism |
| :--- | :--- | :--- |
| **Externally Owned Account (EOA)** | A general user address space. | Controlled explicitly by any entity holding the corresponding **private key**. |
| **Contract Account** | A smart contract deployed on the TRON ledger. | Controlled strictly by its underlying **compiled smart contract code**. No standalone private key exists. |

---

## 3. Accounts & Key Pairs

An account consists of a cryptographic pair of keys: a **public key** and a **private key**. 
* **Public Key:** Mapped directly to the publicly viewable account address.
* **Private Key:** Used to sign transactions, proving authenticity and preventing malicious actors from broadcasting forged data.

### Externally-Owned Account Creation Process
TRON's key pair generation algorithm matches Ethereum's implementation, utilizing the **Elliptic Curve Digital Signature Algorithm (ECDSA)** with the **secp256k1** curve standard.
