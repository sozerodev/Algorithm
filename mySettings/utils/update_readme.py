from datetime import datetime
import os

# 사용하는 코딩 사이트 풀이를 모아놓은 폴더명 리스트 
SITE = ["백준", "프로그래머스", "SamsungSWExpert"]

def read_files_info():
    directory_list = [directory for directory in os.listdir("./") if directory in SITE]

    files_info = {}
    for directory in directory_list:
        
        files_info[directory] = {}
        
        question_cnt = 0

        for root, dir, files in os.walk(f"./{directory}"):
            # if os.path.splitext(exe)
            for file in files:
                if os.path.splitext(file)[1] == ".py":
                    question_cnt += 1
                    files_info[directory][root.split("/")[-1]] = os.path.join(root, file)


        files_info[directory]["question_cnt"] = question_cnt

    return files_info
  



def make_info(files_info, total_file_count):
    info = f"## Files Count In Folders\nTotal File Count: {total_file_count}\n"
    for directory_files_info in files_info:
        temp = f"- {directory_files_info[0]}: {directory_files_info[1]}\n"
        info += temp
    return info
    


def make_read_me(files_info):
    site_info = ""
    for site in files_info.keys():
        site_info += f"</br></br> \n## {site}(<i>{files_info[site].get('question_cnt')}</i> 문제 진행) </br>"

        site_info += "\n | Index | Difficulty |"
        site_info += "\n | ----- | ----- |"
        for key, value in files_info[site].items():
            if key != "question_cnt":
                # 폴더명으로부터 난이도 추출
                # difficulty = re.sub(r'[^0-9]', '', os.path.dirname(value).split("/")[-1])
                difficulty = os.path.dirname(value).split("/")[-2]
                site_info += f"\n | [{key}]({value}) | {difficulty} |"

        
        site_info += "\n"
    


    return f"""
# ps 

* [Obsidian](https://obsidian.md/)을 이용하여 기록 및 관리
    * 해당 repo를 iClound에 업로드하여 다른 기종에서도 연동이 가능


<br/>


### last update
- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}



{site_info}


<br/>


## TODO
- [ ] 파이썬 알고리즘 인터뷰
- [ ] Programmers
- [ ] LeetCode
- [ ] Baekjoon, Codeforce, Codibility, HackerRank...



## requirements.txt
```
mypy===0.971
mypy-extensions===0.4.3 

```


"""


def update_readme():
    files_info = read_files_info()
    return make_read_me(files_info)


if __name__ == "__main__":
    readme = update_readme()

    # README.md 작성
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
