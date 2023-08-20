import os 
import subprocess
import time
import os
import shutil

def launch_job(config_str, source_dir, source_script):
    #os.system("python3 fancy_launcher.py arg1 arg2 arg3")
    #subprocess.call(" ./ fancy_launcher.py", shell-True) cmd = 'python3 fancy_launcher.py -d 8r° % config_str
    #cmd = 'python3 example_launcher.py'
    #res = os. popen ( cmd) . read ( )
    script_path = source_script
    #script_path = source_dir + source_script
    #cmd = 'python ' + source_dir + source_script
    print("Launching job async")
    #os.path.abspath()
    #proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, shell=True)
    command = ['python', script_path] + config_str
    print(command)

    # Call another script using subprocess.Popen
    proc = subprocess.Popen(command, stdin=subprocess.PIPE)

    proc.communicate()
    print("Finished launching job")
    print ("waiting 2 seconds before next job.")
    time.sleep(2.0)
    #print(res)

def parse_config_into_json_dict_and_submit_job(config_dict):
    import json
    #data=('names': ("J.J.", "April"], 'years': [25,291) 
    data_str=json.dumps(config_dict) 
    launch_job(data_str)


def parse_config_into_argparse_format_and_submit_job(config_dict, source_dir, source_script):
    # Convert dictionary to command-line arguments
    args = []
    for key, value in config_dict.items():
        args.extend(['--' + key, str(value)])
    launch_job(args, source_script=source_script, source_dir=source_dir)

    
def create_directory(directory_path):
    # Check if the directory already exists
    if os.path.exists(directory_path):
        print(f"Directory '{directory_path}' already exists, deleting it...")
        shutil.rmtree(directory_path)
    else:
        print(f"Creating directory '{directory_path}'...")

    # Create the directory
    os.makedirs(directory_path)


def loop_over_images():
    #source_dir= '/Users/bradlystadie/Desktop/style-transfer-shit/fast-style-transfer-master/'
    #source_script = 'style.py'
    #source_script = 'example_job.py'
    source_script = 'style.py'
    source_dir = ''
    #source_script = 'style.py'
    #source_images = ['la_muse.jpg', 'the_scream.jpg']
    source_images = ['camel.jpg', 'music_book.jpg', 'mystic_moon.jpg', 'abstract.jpeg', 'clocks.jpeg', 'la_muse.jpg', 'red_woman.jpg',
                     'weird_kiss.jpg', 'sketch.jpg', 'rain_princess.jpeg', 'the_scream.jpeg', 'storm_ocean.jpeg', 'japan.jpg',
                     'starry_night.jpg', 'sword_art.jpg', 'waves.jpeg', 'bear.jpg', 'fire_bird.jpg', 'cow.png', 'elephants.jpg',
                     'pink_flamingo.jpg', 'purple.jpg', 'summer_family.jpg']
    for img in source_images:
        create_directory('/home/ubuntu/test_out/' + img.split('.')[0])
        create_directory('/home/ubuntu/checks/' + img.split('.')[0])
        param_dict = {}
        param_dict['style'] = '/home/ubuntu/imgs/' + img
        param_dict['checkpoint-dir'] = '/home/ubuntu/checks/' + img.split('.')[0]
        param_dict['test'] = '/home/ubuntu/test.jpg'
        param_dict['test-dir'] = '/home/ubuntu/test_out/' + img.split('.')[0]
        param_dict['style-weight'] = 2e2
        param_dict['checkpoint-iterations'] = 10
        param_dict['batch-size'] = 20
        parse_config_into_argparse_format_and_submit_job(param_dict, source_dir, source_script)



if __name__ == "__main__":
    loop_over_images()
        
