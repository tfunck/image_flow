
class Transform():
    def __init__(self, filename, inverse_filename,  source_image, target_image):
        self.forward = filename
        self.inverse = inverse_filename
        self.source_space = source_image.space
        self.target_space = target_image.space
        self.source_file = source_image.filename
        self.target_file = target_image.filename
