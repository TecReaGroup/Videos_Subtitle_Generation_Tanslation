import subprocess
import shutil
import os   

def main(video_name, video_path, srt_translated_path, video_subtitled_folder_path):
    video = video_name + '.mp4'
    video_subtitled = video_name + '_subtitle.mp4'
    srt = video_name + '_tanslated.srt'
    shutil.copy(video_path, ".\\")
    shutil.copy(srt_translated_path, ".\\")

    command = f'ffmpeg -hwaccel nvdec -i "{video}" -vf "subtitles={srt}" -preset ultrafast -threads 0 "{video_subtitled}"'
    subprocess.run(command, shell=True)

    shutil.move(video_subtitled, video_subtitled_folder_path)
    os.remove(video)
    os.remove(srt)


