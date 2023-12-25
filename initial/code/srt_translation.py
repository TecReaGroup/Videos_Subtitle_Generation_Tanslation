import itertools
import os

srt_split = ""

#该prompt效果不好，需要改进
'''
with open('prompt_system.txt', 'r', encoding='utf-8') as file1, open('prompt_system.txt', 'r', encoding='utf-8') as file2,  open('prompt_system.txt', 'r', encoding='utf-8') as file3:
    prompt_system = file1.read()
    prompt_user = file2.read()
    prompt_assistant = file3.read()
'''

def chatgpt_tanslate(prompt, chatgpt_api):
    from openai import OpenAI
    client = OpenAI(api_key=chatgpt_api)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        #{"role": "system", "content": None},
        {"role": "user", "content": prompt},
        #{"role": "assistant", "content": None},
    ]
    )
    return completion.choices[0].message.content

def main(srt_path, srt_translated_path, chatgpt_api, prompt_path):
    if os.path.exists(srt_translated_path):       #if srt file exists, skip
        return
    else:
        os.makedirs(os.path.dirname(srt_translated_path), exist_ok=True)

    with open(srt_path, 'r', encoding='utf-8') as file1, open(srt_translated_path, 'w', encoding='utf-8') as file2, open(prompt_path, 'r', encoding='utf-8') as file3:
        flag = True
        srt_split = ""
        prompt_ask = file3.read()
        while flag:
            for i in range(50):    #每次读取的字幕行数
                next_five_lines = list(itertools.islice(file1, 4))
                if not next_five_lines:
                    flag = False
                    break
                for line in next_five_lines:
                    srt_split += line
                if len(srt_split) > 2800:   #每次输入的最大字幕长度
                    break
            prompt = prompt_ask + srt_split
            print(prompt)
            respond = chatgpt_tanslate(prompt, chatgpt_api)
            file2.write(respond + "\n\n")
            srt_split = ""