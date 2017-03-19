# Schema definitions, based on Cerberus grammar.
# Check the Cerberus project at
# (https://github.com/pyeve/cerberus) for details.

accounts_schema = {
    # 'role' is a list, and can only contain values from 'allowed'.
    'role': {
        'type': 'list',
        'allowed': ["admin", "member"],
    },
    'username': {
        'type': 'string',
        'required': True,
    },
    'password': {
        'type': 'string',
        'required': True,
    }
}

people_schema = {
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 32,
        'required': True,
    },
    'position': {
        'type': 'string',
        'allowed': ["undergraduate student", "phd student", "post-doc", "researcher", "professor"],
        'required': True,
    },
    # An embedded 'strongly-typed' dictionary.
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'affiliation': {
        'type': 'string',
    },
}
