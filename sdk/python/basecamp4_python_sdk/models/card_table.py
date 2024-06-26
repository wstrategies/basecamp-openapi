# coding: utf-8

"""
    Basecamp4 API

    This is an API schema for the Basecamp4 API. It is used to generate client libraries to interact with the API.

    The version of the OpenAPI document: 1.0.0
    Contact: barry@wstrategies.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from basecamp4_python_sdk.models.bucket import Bucket
from basecamp4_python_sdk.models.person import Person
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CardTable(BaseModel):
    """
    CardTable
    """ # noqa: E501
    id: StrictInt
    status: Optional[StrictStr] = None
    visible_to_clients: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    title: Optional[StrictStr] = None
    inherits_status: Optional[StrictBool] = None
    type: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    app_url: Optional[StrictStr] = None
    bookmark_url: Optional[StrictStr] = None
    subscription_url: Optional[StrictStr] = None
    bucket: Optional[Bucket] = None
    creator: Optional[Person] = None
    subscribers: Optional[List[Person]] = None
    lists: Optional[List[CardTableColumn]] = None
    __properties: ClassVar[List[str]] = ["id", "status", "visible_to_clients", "created_at", "updated_at", "title", "inherits_status", "type", "url", "app_url", "bookmark_url", "subscription_url", "bucket", "creator", "subscribers", "lists"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CardTable from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of bucket
        if self.bucket:
            _dict['bucket'] = self.bucket.to_dict()
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in subscribers (list)
        _items = []
        if self.subscribers:
            for _item in self.subscribers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subscribers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in lists (list)
        _items = []
        if self.lists:
            for _item in self.lists:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lists'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CardTable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "visible_to_clients": obj.get("visible_to_clients"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "title": obj.get("title"),
            "inherits_status": obj.get("inherits_status"),
            "type": obj.get("type"),
            "url": obj.get("url"),
            "app_url": obj.get("app_url"),
            "bookmark_url": obj.get("bookmark_url"),
            "subscription_url": obj.get("subscription_url"),
            "bucket": Bucket.from_dict(obj.get("bucket")) if obj.get("bucket") is not None else None,
            "creator": Person.from_dict(obj.get("creator")) if obj.get("creator") is not None else None,
            "subscribers": [Person.from_dict(_item) for _item in obj.get("subscribers")] if obj.get("subscribers") is not None else None,
            "lists": [CardTableColumn.from_dict(_item) for _item in obj.get("lists")] if obj.get("lists") is not None else None
        })
        return _obj

from basecamp4_python_sdk.models.card_table_column import CardTableColumn
# TODO: Rewrite to not use raise_errors
CardTable.model_rebuild(raise_errors=False)

