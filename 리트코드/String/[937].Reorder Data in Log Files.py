from dataclasses import dataclass


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

@dataclass
class Solution:
    def reorderLogFiles(self, logs) -> list:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit(): # 식별자 다음 문자가 숫자라면
                digits.append(log)
            else:
                letters.append(log)
        
        # 첫 번쨰 문자부터 끝까지 오름차순으로 정렬, 문자가 같을 시 식별자를 기준으로 정렬
        letters.sort(key= lambda x: (x.split()[1:], x.split()[0])) 
        return letters + digits