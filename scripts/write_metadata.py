from libxmp import XMPFiles, consts # type: ignore

def get_current_image():
    return XMPFiles(file_path="./test2.jpg", open_forupdate=True)

def upload_edited_image(image):
    image.close_file()

def add_new_metadata_field(metadata, tag, value):
    metadata.delete_property(consts.XMP_NS_DC, tag)
    metadata.set_property(consts.XMP_NS_DC, tag, value)

def get_metadata(image):
    return image.get_xmp()

def is_able_to_modify_metadata(image, metadata):
    return image.can_put_xmp(metadata)

def update_image_metadata(image, metadata):
    image.put_xmp(metadata)

if __name__ == "__main__":
    image = get_current_image() # Implementation differs for different platforms

    metadata = get_metadata(image) # Get the image metadata

    field = "Creator_Twitter" # Custom metadata field
    value = "@fit1055" # Value for the custom metadata field

    # Write new metadata
    if is_able_to_modify_metadata(image, metadata):
        add_new_metadata_field(metadata, field, value)
        update_image_metadata(image, metadata)

    # Save the changes
    upload_edited_image(image)





