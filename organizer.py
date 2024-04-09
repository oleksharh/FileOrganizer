import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

run_create_folders = False

src_dir = r'C:\Users\<your username>\Downloads'
dest_dir = r'C:\Downloaded Files'

# | Destination directories, rename them as you wish to match your needs |
dest_zip = r"C:\Downloaded Files\Zip"
dest_documents = r"C:\Downloaded Files\Documents"
dest_music = r"C:\Downloaded Files\Music"
dest_photos = r"C:\Downloaded Files\Gallery\Photos"
dest_videos = r"C:\Downloaded Files\Gallery\Videos"
dest_codes = r"C:\Downloaded Files\Codes"
dest_threeD = r"C:\Downloaded Files\3D"
dest_applications = r"C:\Downloaded Files\Applications"
dest_other = r"C:\Downloaded Files\Other"

# | File types to match directories above |
zips = ["zip"]
documents = ["xlsx", "pdf", "txt", "pptx", "docx"]
music = ['mp3', 'wav', 'flac', 'aac', 'ogg', 'wma', 'm4a', 'opus', 'alac', 'mid']
photos = ["png", "jpg", "jpeg", "jpeg", "bmp", "gif", "tiff ", "tif", "raw", "cr2", "nef", "arw", "psd"]
videos = ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv', 'webm', 'mpeg', 'mpg', 'm4v']
codes = ['py', 'cpp', 'c', 'java', 'html', 'css', 'js', 'php', 'rb', 'swift', "sql", "csv", "circ", "asm"]
threeD = ['obj', 'stl', 'fbx', 'blend', 'dae', '3ds', 'ply', 'max', 'ma', 'x3d', "blend1"]
applications = ['exe', 'dmg', 'apk', 'app', 'deb', 'rpm', 'msi', 'bin', 'jar', 'sh']

# | Names of the folders that will be created |
folders = ["Zip", "Documents", "Music", "Gallery", "Codes", "3D", "Applications", "Other"]


# | One time function to create              |
# | the folders in the destination directory |
def create_folders():
    # | Creates path in the destination directory |
    # | so it then can be used to move files into |
    for folder_name in folders:
        folder_path = os.path.join(dest_dir, folder_name)

        # Check if the folder needs subdirectories
        subfolders = {
            "Gallery": ["Photos", "Videos"]
        }

        if folder_name in subfolders:
            for subfolder_name in subfolders[folder_name]:
                subfolder_path = os.path.join(folder_path, subfolder_name)
                os.makedirs(subfolder_path, exist_ok=True) # exist_ok = True - will not raise an exception error will just silently handle it
        else:
            os.makedirs(folder_path, exist_ok=True)

def move_files():

    file_types = {
        "documents": documents,
        "music": music,
        "photos": photos,
        "videos": videos,
        "codes": codes,
        "threeD": threeD,
        "applications": applications,
        "zip": zips
        # |Change the name of the key   |
        # |to match the folder name for |
        # |your custom folder that you  |
        # |have created earlier         |
    }

    for file in os.listdir(src_dir):

        file_path = os.path.join(src_dir, file)

        if os.path.isfile(file_path):
            file_extension = file.split('.')[-1].lower()

            destination = dest_other

            for category, extensions in file_types.items():
                if file_extension in extensions:
                    destination = globals()["dest_" + category]
                    break

            destination_path = os.path.join(destination, file)

            if not os.path.exists(destination_path):
                try:
                    file_size = os.path.getsize(file_path)  # Get file size in bytes
                    wait_time = file_size / (1024 * 1024 * 10)  # Coverts bytes to MB and divides by 10 MB/s in order to get the wait time in seconds
                    time.sleep(wait_time)  # Wait based on file size

                    shutil.move(file_path, destination_path)
                except PermissionError:
                    pass
                except FileNotFoundError:
                    pass


if __name__ == "__main__":

    event_handler = FileSystemEventHandler()

    if not run_create_folders:
        create_folders()
        run_create_folders = True
        print("Folders have been created")

    def on_modified(event): # event is the event that triggered the function
        move_files()

    event_handler.on_modified = on_modified 

    observer = Observer() 
    observer.schedule(event_handler, src_dir, recursive=False) # recursive=False - only watches the directory itself, recursive=True - watches the directory and all subdirectories
    observer.start() 

    try: 
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


###  pyinstaller --onefile --noconsole organizer.py  ###


