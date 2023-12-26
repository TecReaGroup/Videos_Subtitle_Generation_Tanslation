# Videos_Subtitle_Generation_Tanslation

If this repository could help you, it would be my honour.<br />
If you think this project is okay, please star this repository.<br />
Wish all the best.<br />

# Preface

## Support 

Language: Tanslate the English to Chinese, then generate bilingual subtitles<br />
(It's easy to support more language in your hands).<br />

System: Windows<br />

## Statement

LLM's output is not always perfect, I try my best to solve these problems (Actually, I spend lost of time on these, and you will aware this in the code).<br />
So when there are some errors please delete the files had been generated and trg again.<br />
And we should konw tanslation errors aren't avoidable, we just try redudce the probability.<br />
If you have good idea to face them. It's a good idea to share it.<br />

# Discription

In this project, There are three steps to make subtitles for the videos.<br />

* Extracte the subtitles from the videos as srt format
* Call chatgpt3.5turbo api to tanslate the subtitles
* Merge the video and the stbtitles

## First:	Extraction

It's easy to do this with the help of whisper made by openai.<br />
Click underneath to get more information.<br />
[Whisper_OpenAI](https://github.com/openai/whisper)<br />

## Second:	Tanslation

In this project, you just need to get the api provided by [openai api](https://platform.openai.com)<br />
(Each amount has initial balance of 5 dollars, and a video cost nearly 0.1 dollar).<br />
And then copy it to the main.py file.<br />
There some default paraments like RPM(the requirement times limit)...If you need, they are all changable.<br />
Due to instability of large language model output, retranslate function in the srt_translation.py try to tanslate the missing text.<br />
But it can't promise that there is no bug.<br />

## Third:	Merger

If you don't need this function, you can pass it (comment out related code in main.py).<br />
video_subtitle_merging.py call ffmpeg command to merge the both.<br />
So you need to download and configure [ffmpeg](https://ffmpeg.org/).<br />

# Instructions

## Run the program

Put videos in the video_initial folder<br />
Then ust need to run the main.py<br />
But before it, you should configure the environment.<br />

### whisper

Follow the steps in the official documentation: [Whisper_OpenAI](https://github.com/openai/whisper).<br />
pytorch is needed to use graphics card acceleration: [pytorch](https://pytorch.org/)<br />

### chatgpt api

Create a amount of openai, and apply for the api from here: https://platform.openai.com/api-keys<br />
Then put it to the chatpgt_api variable in main.py<br />

### ffmpeg

Download here [ffmpeg](https://ffmpeg.org/), and then add it to the system PATH<br />

### python library

It seems too much, so the best choice is review the code, and install libraries it needed.<br />

# Details

* For efficiency, it is best to use a graphics card.
* Somewhere of the code is redundant, so there is still have space to enhance.
  * Especially the IO operations like when perform ffmpeg generation and srt tanslation.

## Demo sample

initial video：<br />
https://youtu.be/92boYNpcP74?si=cfnZitB7j80mWXkT

subtitled video：<br />
https://www.bilibili.com/video/BV1GC4y1T7Zf/?spm_id_from=333.999.0.0&vd_source=caae9647ee390689463b8d0c8037e561
