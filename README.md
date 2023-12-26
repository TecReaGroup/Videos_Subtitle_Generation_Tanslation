# Videos_Subtitle_Generation_Tanslation

If you think this project is okay, please star this repository. That would be my honour.

# Preface

## Support 

Language: Tanslate the English to Chinese, then generate bilingual subtitles
(It's easy to support more language in your hands)

System: Windows

## Statement

LLM's output is not always perfect, I try my best to solve these problems (Actually, I spend lost of time on these, and you will aware this in the code).
So when there are some errors please delete the files had been generated.
If you have good idea to face them. It's a good idea to share it.

# Discription

In this project, There are three steps to make subtitles for the videos.

* Extracte the subtitles from the videos as srt format
* Call chatgpt3.5turbo api to tanslate the subtitles
* Merge the video and the stbtitles

## First:	Extraction

It's easy to do this with the help of whisper made by openai.
Click underneath to get more information.
[Whisper_OpenAI](https://github.com/openai/whisper)

## Second:	Tanslation

In this project, you just need to get the api provided by [openai api](https://platform.openai.com)
(Each amount has initial balance of 5 dollars, and a video cost nearly 0.1 dollar).
And then copy it to the main.py file.
There some default paraments like RPM(the requirement times limit)...If you need, they are all changable.
Due to instability of large language model output, retranslate function in the srt_translation.py try to tanslate the missing text.
But it can't promise that there is no bug.

## Third:	Merger

If you don't need this function, you can pass it (comment out related code in main.py).
video_subtitle_merging.py call ffmpeg command to merge the both.
So you need to download and configure [ffmpeg](https://ffmpeg.org/).

# Instructions

## Run the program

Put videos in the video_initial folder
Then ust need to run the main.py
But before it, you should configure the environment.

### whisper

Follow the steps in the official documentation: [Whisper_OpenAI](https://github.com/openai/whisper).
pytorch is needed to use graphics card acceleration: [pytorch](https://pytorch.org/)

### chatgpt api

Create a amount of openai, and apply for the api from here: https://platform.openai.com/api-keys
Then put it to the chatpgt_api variable in main.py

### ffmpeg

Download here [ffmpeg](https://ffmpeg.org/), and then add it to the system PATH

### python library

It seems too much, so the best choice is review the code, and install libraries it needed.

# Details

* For efficiency, it is best to use a graphics card.
* Somewhere of the code is redundant, so there is still have space to enhance.
  * Especially the IO operations like when perform ffmpeg generation and srt tanslation.

## Demo sample

initial video：
https://youtu.be/92boYNpcP74?si=cfnZitB7j80mWXkT

subtitled video：
https://www.bilibili.com/video/BV1GC4y1T7Zf/?spm_id_from=333.999.0.0&vd_source=caae9647ee390689463b8d0c8037e561
