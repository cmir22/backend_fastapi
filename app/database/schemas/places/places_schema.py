
### Places Schema ###

place_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "phone": {
            "type": "string",
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "web_site": {
            "type": "string",
        },
        "image": {
            "type": "string",
        },
        "is_active": {
            "type": "boolean"
        },
        "last_edit_date": {
            "format": "date-time"
        },
    },
    "required": [
        "name"
    ]
}
