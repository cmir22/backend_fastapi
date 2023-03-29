
### User Schema ###

user_schema = {
    'type': 'object',
    'properties': {
        '_id': {'type': 'string'},
        'name': {'type': 'string'},
            'password': {'type': 'string'},
            'is_active': {'type': 'boolean'},
    },
    'required': ['name']
}
