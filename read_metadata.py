from libxmp import XMPFiles, consts # type: ignore

def get_current_image():
    return XMPFiles(file_path="./test.jpg", open_forupdate=True)

def get_metadata(image):
    return image.get_xmp()

def get_metadata_value_from_field(metadata, field):
    try:
        return metadata.get_property(consts.XMP_NS_DC, field)
    except:
        return None
    
def add_image_to_dataset(image):
    print("Image added to dataset!")

def dont_add_image_to_dataset(image):
    print("Image not added to dataset!")

if __name__ == "__main__":
    image = get_current_image() # Implementation differs for different platforms

    metadata = get_metadata(image) # Get the image metadata

    field = "Allow_For_AI_Use" # Custom metadata field

    # Read metadata
    value = get_metadata_value_from_field(metadata, field)
    print(f"Value of {field}: {value}")

    # Check if image creator allows the image to be used for AI
    if value == "True":
        add_image_to_dataset(image)

    if value == "False":
        dont_add_image_to_dataset(image)


