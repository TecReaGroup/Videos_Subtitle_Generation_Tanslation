import os
from tqdm import tqdm
import time
from srt_extraction import find_files
import srt_extraction
import srt_translation
import video_subtitle_merging

if __name__ == "__main__":
    #文件路径
    prompt_path = r"..\prompt\prompt.txt"
    #文件夹路径
    video_folder_path = r"..\video_inital"
    srt_initial_folder_path = r"..\srt_folder\initial"
    srt_translation_folder_path = r"..\srt_folder\translated"
    video_subtitled_folder_path = r"..\videos_subtitled"

    #文件处理
    mp4_files = find_files(video_folder_path, suffix='mp4')
    for file in tqdm(mp4_files):    #file: video file path
        video_name = file.split('\\')[-1][:-4]
        chatgpt_api = "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"     #chatgpt api

        #文件路径
        video_path = file
        srt_path = srt_initial_folder_path + "\\" + video_name + ".srt"
        srt_translated_path = srt_translation_folder_path + "\\" + video_name + "_tanslated.srt"
        video_subtitled_path = video_subtitled_folder_path + "\\" + video_name + "_subtitled.mp4"

        if os.path.exists(video_subtitled_path):       #if srt file exists, skip
            time.sleep(0.01)
            continue

        srt_extraction.main(video_path, srt_path)    
        srt_translation.main(srt_path, srt_translated_path, chatgpt_api, prompt_path)
        video_subtitle_merging.main(video_name, video_path, srt_translated_path, video_subtitled_folder_path)
