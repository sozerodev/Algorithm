import time
import os
from datetime import datetime, timedelta, timezone

# 사용하는 코딩 사이트 풀이를 모아놓은 폴더명 리스트 
SITE = ["백준", "프로그래머스", "LeetCode", "SamsungSWExpert", "thisIsCodingTest"]

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

        # 난이도별 풀이 개수 추가
        files_info[directory]["level"] = {}
        if directory == "LeetCode":
            for level in ["Easy", "Medium", "Hard"]:
                try:
                    files_info[directory]["level"][level] = len(os.listdir(f"./{directory}/{level}"))
                except:
                    pass
                
        elif directory == "백준":
            for level in ["Bronze", "Silver","Gold"]:
                files_info[directory]["level"][level] = len(os.listdir(f"./{directory}/{level}"))

    return files_info
  



def make_info(files_info, total_file_count):
    info = f"## Files Count In Folders\nTotal File Count: {total_file_count}\n"
    for directory_files_info in files_info:
        temp = f"- {directory_files_info[0]}: {directory_files_info[1]}\n"
        info += temp
    return info
    


def make_read_me(files_info):
    site_info = ""
    # for site in files_info.keys(): # 이거나 밑에나 둘다 같지만 그냥 순서를 내맘대로 해주고싶어서 밑에껄로 바꿈
    for site in SITE:
        if len(files_info[site].get('level')) > 0:
            site_info += f"</br></br>\n ## {site}(<i>{files_info[site].get('question_cnt')}</i> 문제 진행, "
            
            for level in files_info[site].get('level').keys():
                site_info += f"{level}:{files_info[site].get('level').get(level)} "
            site_info += ") </br>"
        else:
            site_info += f"</br></br>\n ## {site}(<i>{files_info[site].get('question_cnt')}</i> 문제 진행) </br>"
        

        site_info += "\n | Index | Difficulty |"
        site_info += "\n | ----- | ----- |"
        for key, value in files_info[site].items():
            if key != "question_cnt":
                # 폴더명으로부터 난이도 추출
                # difficulty = re.sub(r'[^0-9]', '', os.path.dirname(value).split("/")[-1])
                if key == "level": continue
                difficulty = os.path.dirname(value).split("/")[-2]
                site_info += f"\n | [{key}]({value}) | {difficulty} |"

        
        site_info += "</br></br> \n\n"
    

    # str_utc = time.localtime(time.time())


    return f"""

# PS (Problem Solving) 키우기


### last update
- {convert_kst(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))}


</br>

### [History👊](https://typeerror.notion.site/Algorithm-History-f12e001a8c954b2e96994f6e2f4235e0)

</br>

### 파이썬 알고리즘 스터디
- ~~2022.10.03 ~  (야근중단..)~~
- 2023.03.05 ~ 

    |   기간   | 주제 | 진행상황 |
    | -------- | --- | ----- |
    | 03월 2주차 | bfs | 🧐 |
    | 03월 3주차 | dfs | 😀 |
    | 03월 4주차 | 이진탐색| 🔒 |
    | 03월 5주차 | 완전탐색&백트래킹 | 🔒 |
    | 04월 2주차 | dp | 🔒 |
    | 04월 3주차 | dp | 🔒 |
    | 04월 4주차 | 다익스트라 | 🔒 |
    | 04월 5주차 | 플로이드-와샬 | 🔒 |
    | 05월 1주차 |  위상정렬   | 🔒 |
    | 05월 2주차 |  bfs,dfs 고난이도  | 🔒 |
    | 05월 3주차 |  카카오 기출  | 🔒 |






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

## etc
uploaded by [LeetHub](https://github.com/QasimWani/LeetHub), [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)



"""


def update_readme():
    files_info = read_files_info()
    return make_read_me(files_info)


def convert_kst(utc_string):
	# datetime 값으로 변환
	dt_tm_utc = datetime.strptime(utc_string,'%Y-%m-%d %H:%M:%S')
	
	# +9 시간
	tm_kst = dt_tm_utc + timedelta(hours=9)
	
	# 일자 + 시간 문자열로 변환
	str_datetime = tm_kst.strftime('%Y-%m-%d %H:%M:%S')
	
	return str_datetime



if __name__ == "__main__":
    readme = update_readme()

    # README.md 작성
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
