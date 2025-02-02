from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from ..nft import NftMetadata
from ..metadata import Metadata


@dataclass_json
@dataclass
class CollectionMetadata:
    id: Optional[int] = None
    creator: Optional[str] = None
    supply: Optional[int] = None
    metadata: Optional[NftMetadata] = None


@dataclass_json
@dataclass
class CreateCollectionArg:
    metadata: Optional[Metadata] = None
    supply: Optional[int] = None


@dataclass_json
@dataclass
class MintCollectionArg:
    token_id: Optional[int] = None
    amount: Optional[int] = None

