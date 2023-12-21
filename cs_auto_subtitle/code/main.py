import srt_extraction
import video_subtitle_merging

if __name__ == "__main__":
    video_file_path = r"..\video_inital"
    srt_file_path = r"..\srt_files"
    output_file_path = r"..\videos_subtitled"
    srt_extraction.main(video_file_path,srt_file_path,output_file_path)
