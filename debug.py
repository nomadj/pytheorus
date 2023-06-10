import mimetypes

def check_file_type(file_path):
    file_type = mimetypes.guess_type(file_path)[0]

    if file_type not in ["image/png", "image/jpeg", "model/gltf-binary"]:
        raise ValueError("Invalid file type. The file must be in PNG, JPG, or GLB format.")
    return file_type

