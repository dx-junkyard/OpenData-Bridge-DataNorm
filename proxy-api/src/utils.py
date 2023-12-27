from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# シークレットを取得する関数
def get_secret(secret_name):
    #KEY_CONTAINER_NAME = "odb-test-proxy-api-key" 
    KEY_CONTAINER_NAME = "DataNorm-key-container"
    key_vault_url = f"https://{KEY_CONTAINER_NAME}.vault.azure.net/"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=key_vault_url, credential=credential)
    retrieved_secret = client.get_secret(secret_name)

    return retrieved_secret.value

