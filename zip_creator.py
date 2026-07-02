import zipfile
import pathlib

def make_archive(filepaths, dest_dir):

    ''' zip path is created in destination dir '''
    dest_path = pathlib.Path(dest_dir, "compressed.zip")

    ''' This will create zip file if not already existed '''
    with zipfile.ZipFile(dest_path, 'w') as archive:

        '''Before for-loop every filepath is a string
        but after for-loop it converts to path object
        '''
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)

            ''' Add every file in created Zip document '''
            archive.write(filepath, arcname=filepath.name)



