
roots = {
    'com': {
        'extend': None,

        'domain_name':				r'Domain Name:\s?(.+)',
        'registrar':				r'Registrar:\s?(.+)',
        'registrant':				None,

        'creation_date':			r'Creation Date:\s*(.+)\s*',
        'expiration_date':			r'Expiration Date:\s*(.+)\s*',
        'updated_date':				r'Updated Date:\s*(.+)\s*',

        'name_servers':				r'Name Server:\s*(.+)\s*',
        'status':					r'Status:\s?(.+)',
        'emails':					r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
    },

    'net': {
        'extend': 'com',
    },

    'org': {
        'extend': 'com',

        'creation_date':			r'\nCreated On:\s*(.+)\s*',
        'expiration_date':			r'\nRegistry Expiry Date:\s?(.+)',
        'updated_date':				r'\nLast Updated On:\s*(.+)\s*',

        'name_servers':				r'Name Server:\s?(.+)\s*',
    },

    'edu': {
        'extend': 'com',

        'creation_date':			r'Domain record activated:\s+(.+)',
        'expiration_date':			r'Domain expires:\s+(.+)',
        'updated_date':				r'Domain record last updated:\s+(.+)',
    },

    'uk': {
        'extend': 'com',

        'registrant':				r'Registrant:\n\s*(.+)',

        'creation_date':			r'Registered on:\s*(.+)',
        'expiration_date':			r'Renewal date:\s*(.+)',
        'updated_date':				r'Last updated:\s*(.+)',

        'name_servers':				r'Name Servers:\s*(.+)\s*',
        'status':					r'Registration status:\n\s*(.+)',
    },

    'pl': {
        'extend': 'uk',

        'creation_date':			r'\ncreated:\s*(.+)\n',
        'updated_date':				r'\nlast modified:\s*(.+)\n',

        'name_servers':				r'\nnameservers:\s*(.+)\n\s*(.+)\n',
        'status':					r'\nStatus:\n\s*(.+)',
    },

    'ru': {
        'extend': 'com',

        'domain_name':				r'\ndomain:\s*(.+)',

        'creation_date':			r'\ncreated:\s*(.+)',
        'expiration_date':			r'\npaid-till:\s*(.+)',
        'updated_date':				r'\nLast updated on\s*(.+)',

        'name_servers':				r'\nnserver:\s*(.+)',
        'status':					r'\nstate:\s*(.+)',
    },

    'ru_rf': {
        'extend': 'com',

        'domain_name':				r'\ndomain:\s*(.+)',

        'creation_date':			r'\ncreated:\s*(.+)',
        'expiration_date':			r'\npaid-till:\s*(.+)',

        'name_servers':				r'\nnserver:\s*(.+)',
        'status':					r'\nstate:\s*(.+)',
    },

    'su': {
        'extend': 'ru',
    },

    'lv': {
        'extend': 'ru',

        'creation_date':			r'Registered:\s*(.+)\n',
        'updated_date':				r'Changed:\s*(.+)\n',

        'status':					r'Status:\s?(.+)',
    },

    'jp': {
        'domain_name':				r'\[Domain Name\]\s?(.+)',
        'registrar':				None,
        'registrant':				r'\[Registrant\]\s?(.+)',

        'creation_date':			r'\[Created on\]\s*(.+)\n',
        'expiration_date':			r'\[Expires on\]\s*(.+)\n',
        'updated_date':				r'\[Last Update\]\s*(.+)\n',

        'name_servers':				r'\[Name Server\]\s*(.+)',
        'status':					r'\[Status\]\s?(.+)',
        'emails':					r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
    },

    'co_jp': {
        'extend': 'jp',

        'creation_date':			r'\[Registered Date\]\s?(.+)',
        'expiration_date':			r'\[State\].+\((.+)\)',
    },

    'de': {
        'extend': 'com',
        'domain_name':				r'\ndomain:\s*(.+)',
        'updated_date':				r'\nChanged:\s?(.+)',
        'name_servers':				r'Nserver:\s*(.+)',
    },

    'at': {
        'extend': 'com',
        'domain_name':				r'domain:\s?(.+)',
        'updated_date':				r'changed:\s?(.+)',
        'name_servers':				r'nserver:\s*(.+)',
    },

    'eu': {
        'extend': 'com',

        'domain_name':				r'\ndomain:\s*(.+)',
        'registrar':				r'Name:\s?(.+)',
    },

    'biz': {
        'extend': 'com',

        'registrar':				r'Sponsoring Registrar:\s?(.+)',
        'registrant':				r'Registrant Organization:\s?(.+)',

        'creation_date':			r'Creation Date:\s*(.+)\s*',
        'expiration_date':			r'Registry Expiry Date:\s*(.+)\s*',
        'updated_date':				r'Updated Date:\s*(.+)\s*',

        'status':					None,
    },

    'info': {
        'extend': 'biz',

        'creation_date':			r'Created On:\s?(.+)',
        'expiration_date':			r'Expiration Date:\s?(.+)$',
        'updated_date':				r'Last Updated On:\s?(.+)$',

        'status':					r'Status:\s?(.+)',
    },

    'name': {
        'extend': 'com',

        'status':					r'Domain Status:\s?(.+)',
    },

    'us': {
        'extend': 'name',
    },

    'co': {
        'extend': 'biz',

        'status':					r'Status:\s?(.+)',
    },

    'me': {
        'extend': 'biz',

        'creation_date':			r'Creation Date:\s?(.+)',
        'expiration_date':			r'Expiry Date:\s?(.+)',
        'updated_date':				r'Updated Date:\s?(.+)',

        'name_servers':				r'Nameservers:\s?(.+)',
        'status':					r'Domain Status:\s?(.+)',
    },

    'be': {
        'extend': 'pl',

        'domain_name':				r'\nDomain:\s*(.+)',
        'registrar':				r'Company Name:\n?(.+)',

        'creation_date':			r'Registered:\s*(.+)\n',

        'status':					r'Status:\s?(.+)',
    },

    'nz': {
        'extend': None,

        'domain_name':				r'domain_name:\s?(.+)',
        'registrar':				r'registrar_name:\s?(.+)',
        'registrant':				r'registrant_contact_name:\s?(.+)',

        'creation_date':			r'domain_dateregistered:\s?(.+)',
        'expiration_date':			r'domain_datebilleduntil:\s?(.+)',
        'updated_date':				r'domain_datelastmodified:\s?(.+)',

        'name_servers':				r'ns_name_[0-9]{2}:\s?(.+)',
        'status':					r'query_status:\s?(.+)',
        'emails':					r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
    },

    'cz': {
        'extend': 'com',

        'domain_name':				r'Domain:\s?(.+)',
        'registrar':				r'registrar:\s?(.+)',
        'registrant':				r'registrant:\s?(.+)',

        'creation_date':			r'registered:\s?(.+)',
        'expiration_date':			r'expire:\s?(.+)',
        'updated_date':				r'changed:\s?(.+)',

        'name_servers':				r'nserver:\s*(.+) ',
    },

    'it': {
        'extend': 'com',

        'domain_name':				r'Domain:\s?(.+)',
        'registrar':				r'Registrar:\s*Organization:\s*(.+)',
        'registrant':				r'Registrant:\s?Name:\s?(.+)',

        'creation_date':			r'Created:\s?(.+)',
        'expiration_date':			r'Expire Date:\s?(.+)',
        'updated_date':				r'Last Update:\s?(.+)',

        'name_servers':				r'Nameservers:\s?(.+)\s?(.+)\s?(.+)\s?(.+)',
        'status':					r'Status:\s?(.+)',
    },

    'fr': {
        'extend': 'com',

        'domain_name':				r'domain:\s?(.+)',
        'registrar':				r'registrar:\s*(.+)',
        'registrant':				r'contact:\s?(.+)',

        'creation_date':			r'created:\s?(.+)',
        'expiration_date':			None,
        'updated_date':				r'last-update:\s?(.+)',

        'name_servers':				r'nserver:\s*(.+)',
        'status':					r'status:\s?(.+)',
    },

    'io': {
        'extend': 'com',
        'expiration_date':			r'\nRegistry Expiry Date:\s?(.+)',
    },

    'br': {
        'extend': 'com',
        'domain_name':              r'domain:\s?(.+)',
        'registrar':                'nic.br',
        'registrant':               None,
        'owner':                    r'owner:\s?(.+)',
        'creation_date':            r'created:\s?(.+)',
        'expiration_date':          r'expires:\s?(.+)',
        'updated_date':             r'changed:\s?(.+)',
        'name_servers':             r'nserver:\s*(.+)',
        'status':                   r'status:\s?(.+)',
    },

    'ma': {
        'extend': 'com',
        'registrar':				r'Registrar:\s?(.+)',
        'registrant':				r'Registrant Name:\s?(.+)',
        'expiration_date':			r'\nRegistry Expiry Date:\s?(.+)',
        'status':					r'Domain Status:\s?(.+)',
    },

    'tv': {
        'extend': 'com',
        'expiration_date':			r'Registry Expiry Date:\s?(.+)',
    },

    'in': {
        'extend': 'com',

        'creation_date':            r'Created On:\s*(.+)\s*',
        'updated_date':             r'Last Updated On:\s*(.+)\s*',
    },

    'qa': {
        'extend': 'com',

        'updated_date':             r'Last Modified:\s+(.*)\n',
    },

    'om': {
        'extend': 'qa',
    },

    'ir': {
        'extend': 'br',
        'domain_name':              r'domain:\s?(.+)',
        'creation_date':            None,
        'expiration_date':          r'expire-date:\s?(.+)',
        'updated_date':             r'last-updated:\s?(.+)',
    },

    'tw': {
        'extend': 'com',

        'creation_date':            r'Record created on (.+) \(YYYY-MM-DD\)',
        'expiration_date':          r'Record expires on (.+) \(YYYY-MM-DD\)',
    },

    'hk': {
        'extend': 'com',

        'creation_date':            r'Domain Name Commencement Date:\s?(.+)',
        'expiration_date':          r'Expiry Date:\s?(.+)\s*',
    },

    'th': {
        'extend': 'com',

        'domain_name':              r'Domain:\s*(.+)\s*',
        'creation_date':            r'Created date:\s*(.+)\s*',
        'expiration_date':          r'Exp date:\s*(.+)\s*',
        'updated_date':             r'Updated date:\s*(.+)\s*',
    },

    'tr': {
        'extend': 'com',

        'creation_date':            r'Created on\.+:\s*(.+)\.',
        'expiration_date':          r'Expires on\.+:\s*(.+)\.',
    },

    'mx': {
        'extend': 'com',

        'creation_date':			r'Created On:\s*(.+)\s*',
        'updated_date':				r'Last Updated On:\s*(.+)\s*',
    },

    'ch': {
        'extend': 'com',

        'creation_date':			r'First registration date:\s*(.+)\s*',
        'name_servers':				r'Name servers:\s*(.+)(?:\s*(.+)(?:\s*(.+)(?:\s*(.+)(?:\s*(.+))?)?)?)?',
    },

    'dk': {
        'extend': 'com',

        'domain_name':              r'Domain:\s*(.+)\s*',
        'creation_date':            r'Registered:\s*(.+)\s*',
        'expiration_date':          r'Expires:\s*(.+)\s*',
    },

    'fi': {
        'extend': 'com',

        'domain_name':              r'domain\.+:\s*(.+)\s*',
        'creation_date':            r'created\.+:\s*(.+)\s*',
        'expiration_date':          r'expires\.+:\s*(.+)\s*',
        'updated_date':				r'modified\.+:\s*(.+)\s*',
    },

    'cn': {
        'extend': 'com',

        'creation_date':            r'Registration Time:\s*(.+)\s*',
        'expiration_date':          r'Expiration Time:\s*(.+)\s*',
    },

    'rs': {
        'extend': 'com',

        'creation_date':            r'Registration date:\s*(.+)\s*',
        'updated_date':				r'Modification date:\s*(.+)\s*',
    },

    'sk': {
        'extend': 'cz',

        'creation_date':			r'Created:\s*(.+)\s*',
        'expiration_date':			r'Valid Until:\s*(.+)\s*',
        'updated_date':				r'Updated:\s*(.+)\s*',

        'name_servers':				r'Nameserver:\s*(.+)\s*',
    },

    'id': {
        'extend': 'com',

        'creation_date':			r'Created On:(.+)\s*',
        'expiration_date':			r'Expiration Date:(.+)\s*',
        'updated_date':				r'Last Updated On:(.+)\s*',
    },

    'ua': {
        'extend': 'com',

        'domain_name':              r'domain:\s*(.+)\s*',
        'creation_date':            r'created:\s*(.+)\s*',
        'expiration_date':          r'expires:\s*(.+)\s*',
        'updated_date':				r'modified:\s*(.+)\s*',
    },

}
