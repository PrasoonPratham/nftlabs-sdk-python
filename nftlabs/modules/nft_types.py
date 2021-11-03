"""Types for the NFT Module."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class MintArg:
    """
    Arguments for minting new tokens
    """
    name: str
    description: str = ""
    image: str = ""
    properties: Optional[dict] = None

