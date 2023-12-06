#importer de nødvendige bibliotekene


def Get_PowerBI_Token():
    tenant_id = os.environ.get("TENANT_ID")
    applicationId = os.environ.get("APPLICATION_ID")
    securePassword = os.environ.get("SECURE_PASSWORD")
    scope = 'https://analysis.windows.net/powerbi/api/.default'
    client_secret_credential_class = ClientSecretCredential(tenant_id=tenant_id, client_id=applicationId, client_secret=securePassword)
    access_token_class = client_secret_credential_class.get_token(scope)
    token_string = access_token_class.token

    return token_string