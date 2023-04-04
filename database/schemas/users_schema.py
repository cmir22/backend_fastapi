
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
        },
        "created_date": {
            "type": "string",
            "join_date": "date-time"
        }
    },
    "required": ["name", "password"]
}
