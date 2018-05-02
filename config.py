import os


def _var_or_default(env, default):
    value = os.getenv(env)
    if value:
        print("Loaded value for config env variable %s" % env)
        return value
    print("Using default value for config env variable %s" % env)
    return default


db_host = _var_or_default("POSTGRES_HOST", "localhost")
db_name = _var_or_default("POSTGRES_DB", "demo")
db_user = _var_or_default("POSTGRES_USER", "demo")
db_password = _var_or_default("POSTGRES_PASSWORD", "")
