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

from datetime import date, datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from basecamp4_python_sdk.models.bucket import Bucket
from basecamp4_python_sdk.models.card_table_column import CardTableColumn
from basecamp4_python_sdk.models.person import Person
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CardTableCard(BaseModel):
    """
    CardTableCard
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
    comments_count: Optional[StrictInt] = None
    comments_url: Optional[StrictStr] = None
    position: Optional[StrictInt] = None
    parent: Optional[CardTableColumn] = None
    bucket: Optional[Bucket] = None
    creator: Optional[Person] = None
    description: Optional[StrictStr] = None
    completed: Optional[StrictBool] = None
    content: Optional[StrictStr] = None
    due_on: Optional[date] = None
    assignees: Optional[List[Person]] = None
    completion_subscribers: Optional[List[Person]] = None
    completion_url: Optional[StrictStr] = None
    comment_count: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "status", "visible_to_clients", "created_at", "updated_at", "title", "inherits_status", "type", "url", "app_url", "bookmark_url", "subscription_url", "comments_count", "comments_url", "position", "parent", "bucket", "creator", "description", "completed", "content", "due_on", "assignees", "completion_subscribers", "completion_url", "comment_count"]

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
        """Create an instance of CardTableCard from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict['parent'] = self.parent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bucket
        if self.bucket:
            _dict['bucket'] = self.bucket.to_dict()
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in assignees (list)
        _items = []
        if self.assignees:
            for _item in self.assignees:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assignees'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in completion_subscribers (list)
        _items = []
        if self.completion_subscribers:
            for _item in self.completion_subscribers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['completion_subscribers'] = _items
        # set to None if due_on (nullable) is None
        # and model_fields_set contains the field
        if self.due_on is None and "due_on" in self.model_fields_set:
            _dict['due_on'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CardTableCard from a dict"""
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
            "comments_count": obj.get("comments_count"),
            "comments_url": obj.get("comments_url"),
            "position": obj.get("position"),
            "parent": CardTableColumn.from_dict(obj.get("parent")) if obj.get("parent") is not None else None,
            "bucket": Bucket.from_dict(obj.get("bucket")) if obj.get("bucket") is not None else None,
            "creator": Person.from_dict(obj.get("creator")) if obj.get("creator") is not None else None,
            "description": obj.get("description"),
            "completed": obj.get("completed"),
            "content": obj.get("content"),
            "due_on": obj.get("due_on"),
            "assignees": [Person.from_dict(_item) for _item in obj.get("assignees")] if obj.get("assignees") is not None else None,
            "completion_subscribers": [Person.from_dict(_item) for _item in obj.get("completion_subscribers")] if obj.get("completion_subscribers") is not None else None,
            "completion_url": obj.get("completion_url"),
            "comment_count": obj.get("comment_count")
        })
        return _obj


