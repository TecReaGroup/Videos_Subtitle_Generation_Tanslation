import os
import datetime
import time
from zhconv import convert
from tqdm import tqdm
import imageio
import whisper
import video_subtitle_merging

def find_files(path, suffix):
    mp4_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.' + suffix):
                mp4_files.append(os.path.abspath(os.path.join(root, file)))
    return mp4_files

def seconds_to_hmsm(seconds):
    hours = str(int(seconds // 3600))
    minutes = str(int((seconds % 3600) // 60))
    seconds = seconds % 60
    milliseconds = str(int(int((seconds - int(seconds)) * 1000)))
    seconds = str(int(seconds))
    if len(hours) < 2:
        hours = '0' + hours
    if len(minutes) < 2:
        minutes = '0' + minutes
    if len(seconds) < 2:
        seconds = '0' + seconds
    if len(milliseconds) < 3:
        milliseconds = '0'*(3-len(milliseconds)) + milliseconds
    return f"{hours}:{minutes}:{seconds},{milliseconds}"

def main(video_file_path, srt_file_path, output_file_path):
    file_path = video_file_path
    mp4_files = find_files(file_path, suffix='mp4')
    model = whisper.load_model('medium.en')  #whisper model choice
    for file in tqdm(mp4_files):    #file: video file path
        video_name = file.split('\\')[-1][:-4]
        save_file = srt_file_path + "\\" + video_name + ".srt"  #srt file path
        if os.path.exists(save_file):
            time.sleep(0.01)
            continue
        start_time = datetime.datetime.now()
        print('正在识别：{} --{}'.format('\\'.join(file.split('\\')[2:]), start_time.strftime('%Y-%m-%d %H:%M:%S')))
        video = imageio.get_reader(file)
        duration = seconds_to_hmsm(video.get_meta_data()['duration'])
        video.close()
        print('视频时长：{}'.format(duration))
        res = model.transcribe(file, fp16=False, language='English') #语言选择
        with open(save_file, 'w', encoding='utf-8') as f:
            i = 1
            for r in res['segments']:
                f.write(str(i) + '\n')
                f.write(seconds_to_hmsm(float(r['start'])) + ' --> ' + seconds_to_hmsm(float(r['end'])) + '\n')
                i += 1
                f.write(r['text'] + '\n') 
                f.write('\n')
        end_time = datetime.datetime.now()
        print('完成识别：{} --{}'.format('\\'.join(file.split('\\')[2:]), end_time.strftime('%Y-%m-%d %H:%M:%S')))
        print('花费时间:', end_time - start_time)
        
        # add subtitles to video
        subtitled_video_path = output_file_path + "\\" + video_name + '_subtitled.mp4'
        video_subtitle_merging.add_subtitles_to_video(file,save_file,subtitled_video_path)