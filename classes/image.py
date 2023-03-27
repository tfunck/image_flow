
global SPACES
SPACES = ['stx','mri','pet']


class Image():
    def __init__(self, filename, origin_space, affine=None, step=None, origin=None, ndim=None):

        self.file={} 
        self.space=origin_space
        self.ndim = ndim

        if os.path.exists(filename)
            self.ndim = len( self.safe_load(filename).shape) 
            self.affine = img.affine
            self.step = 
            self.origin =

    def load(self):
        assert os.path.exists(self.filename), 'Error: does not exist\n{filename}'
        return nib.load(filename)

    def transform(self, reference_filename, tfm_file, output_filename):

        antsApplyTransform()


class ImageSet():
    def __init__(self,filename,origin_space):

        for space in SPACES:
            if space == origin_space :
                self.file[space] = Image(filename, space)
            else :
                self.file[space] = Image( rename_space(filename, origin_space, space), space)


    def rename_space(self, filename, space):
        if 'space-{self.origin_space}' in filename :
            filename = re.sub(f'space-{self.origin_space}', space, filename)
        else :
            filename = re.sub('.nii.gz, 'f'_space-{self.origin_space}.nii.gz',  filename)

        return filename

class Section(Image) :
    pass

class Label(Image):
    def __init__(self,erode=0,concat=False):
        self.erode=erode
        self.concat=concat



