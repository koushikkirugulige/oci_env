from oci.config import from_file
from oci.config import validate_config
config = from_file()
config = from_file(profile_name="mumbai_free")

try:
    validate_config(config)
    print("Configuration is valid")
except Exception as e:
    print(f"Invalid configuration: {str(e)}")