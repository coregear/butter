from butter.base import env


def legacy_settings():
    """
    Deprecated method to add env global variables to the `env.settings`
    dictionary. These should instead be placed in `env.settings`.
    """
    print ('+ Using deprecated legacy settings')
    if 'db_db' in env:
        env.settings.db_db = env.db_db
    if 'db_user' in env:
        env.settings.db_user = env.db_user
    if 'db_pw' in env:
        env.settings.db_pw = env.db_pw
    if 'db_host' in env:
        env.settings.db_host = env.db_host
    if 'smtp_pw' in env:
        env.settings.smtp_pw = env.smtp_pw
    if 'base_url' in env:
        env.settings.base_url = env.base_url
