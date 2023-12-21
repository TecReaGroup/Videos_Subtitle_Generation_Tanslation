from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip

def add_subtitles_to_video(video_path,subtitle_path,subtitled_video_path):
    """ 将srt字幕添加到视频中. """
    video = VideoFileClip(video_path)
    
    def generator(txt):
        words = txt.split()
        lines = [' '.join(words[i:i+10]) for i in range(0, len(words), 10)]   #打印字幕及换行（每10行）
        txt = '\n'.join(lines)
        return TextClip(txt, font='Arial', fontsize=16, color='white')     #fontsize字幕字体大小

    subtitles = SubtitlesClip(subtitle_path, generator)

    final = CompositeVideoClip([video, subtitles.set_position(('center', 'bottom'))])       #字幕位置
    final.write_videofile(subtitled_video_path)

# 引用格式 in srt_extraction.py
#video_subtitle_merging.add_subtitles_to_video(file,save_file,subtitled_video_path)