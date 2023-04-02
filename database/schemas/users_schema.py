
### User Schema ###

user_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "password": {
            "type": "string"
        },
        "is_active": {
            "type": "boolean"
        }
    },
    "required": ["name", "password"]
}
