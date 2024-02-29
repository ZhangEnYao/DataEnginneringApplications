import ldap

class LightweightDirectoryAccessProtocol:
    ldap_connection = ldap.initialize(
        'ldap://localhost:389/'
    )
    @classmethod
    def execute(cls, identifier, password):
        try:
            cls.ldap_connection.simple_bind_s(
                'cn={common_name},dc=example,dc=org'.format(
                    common_name = identifier
                ),
                password
            )
            return True
        except:
            return False
