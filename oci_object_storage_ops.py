#import os
#code form https://github.com/oracle/oci-python-sdk/tree/master/examples/object_storage
from oci.config import from_file
from oci.config import validate_config
from oci.object_storage import ObjectStorageClient
from oci import object_storage
import oci
import logging

# Enable debug logging
logging.getLogger('oci').setLevel(logging.DEBUG)

config = from_file()
config = from_file(profile_name="mumbai_free")

bucket_name = '<bucket-name>' 
#bucket_name = 'koushik-bucket'
#namespace_name = 'bmt26qqdncmt'
namespace_name = '<namespace>'

max_retry_timeout = 16**2

def list_objects():
    """
    Lists the objects in a given bucket.

    Args:
        None

    Returns:
        A list of object names in the specified bucket.

    Example:
        To use this function, replace 'bucket-name' and '<namespace>'
            with your own bucket name and namespace respectively.
    """
    # Create an ObjectStorage client
    object_storage_client = ObjectStorageClient(config)

    # Get a list of objects in the bucket
    objects = object_storage_client.list_objects(namespace_name, bucket_name).data.objects

    # Print the names of all files in the bucket
    for obj in objects:
        print(obj.name)
        

def rename_object(old_name, new_name):
    """
    Renames an object within a specified bucket.

    Args:
        old_name (str): The current name of the object.
        new_name (str): The desired name for the object.

    Raises:
        oci.exceptions.ServiceError: If the operation fails due to a service error.

    Returns:
        None
    """
    object_storage_client = ObjectStorageClient(config)
    
        
    rename_request = oci.object_storage.models.RenameObjectDetails()
    rename_request.source_name = old_name
    rename_request.new_name = new_name

    object_storage_client.rename_object(namespace_name, bucket_name, rename_request)
    print(f"Renamed '{old_name}' to '{new_name}'")

def delete_object(object_):
    """
    Deletes an object from a specified bucket.
    Args:
        object_: The name of the object to be deleted.

    Raises:
        oci.exceptions.ServiceError: If the operation fails due to a service error.

    Returns:
        None
    """
    object_storage_client = ObjectStorageClient(config)
    response = None
    try:
        response = object_storage_client.delete_object(namespace_name, bucket_name, object_)
        #print(type(response))
        
    except Exception as e:
        if response:
            print(f"  Received {response.status} from API for object {object_}")
        else:
            print(f"  Received error from API for object {object_}")
            
    
        #time.sleep(interval_exp)
        #interval_exp **= 2
def upload_file(file_path, file_name):
    """
    Uploads a local file to Object Storage.

    Args:
        file_path (str): The path of the local file to be uploaded.
        file_name (str): The desired name for the object in Object Storage.

    Raises:
        oci.exceptions.ServiceError: If the operation fails due to a service error.

    Returns:
        None
    """
    # Upload the file to Object Storage
    object_storage_client = ObjectStorageClient(config)
    
    with open(file_path, 'rb') as file:
        object_storage_client.put_object(namespace_name, bucket_name, file_name, file)



file_path = '<file_path with file name>'
file_name = '<Uploaded File Name>'

upload_file(file_path,file_name)
list_objects()
#rename_object('no_sp.py','no1_sp.py')
#delete_object('jira_data.csv')