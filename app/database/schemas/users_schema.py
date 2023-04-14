
### User Schema ###

user_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "password": {
            "type": "string",
        },
        "is_active": {
            "type": "boolean"
        },
        "created_date": {
            "type": "string",
            "format": "date-time"
        },
        "email": {
            "type": "string",
            "format": "email"
        }
    },
    "required": [
        "name",
        "password",
        "email"
    ]

}
