import os
import subprocess


def create_new_path_name(source, solution):
    dir_name, base_name = os.path.split(source)
    file_name, file_ext = os.path.splitext(base_name)
    new_name = file_name + solution 
    new_file_name = new_name + file_ext
    new_path = os.path.join(dir_name, new_file_name)
    return new_path

def convert_to_480p(source):
    solution = '_480p'
    new_path_name = create_new_path_name(source, solution)
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, new_path_name)
    result = subprocess.run(cmd, capture_output=True)
    
    print('Return code:', result.returncode)
    print('Standard output:', result.stdout)
    print('Standard error:', result.stderr)