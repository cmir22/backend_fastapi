
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
        "city": {
            "type": "string",
        },
        "state": {
            "type": "string",
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
            "type": "string",
            "format": "date-time"
        },
    },
    "required": ["name"]
}
