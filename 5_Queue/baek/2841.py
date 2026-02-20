# 문제집공유용 10. 시크릿 문제집 2841 기타

import sys
input = sys.stdin.readline

finger_stack = [[] for _ in range(7)]

n, p = map(int, input().split())
cnt = 0
'''
1. 누르는 시점
  - finger_stack[line] 이 비어있을 때 -> 라인 위 플랫을 누르고 있지 않을 때
  - finger_stack[line][-1] < fret 일 때 -> 현재 누르고 있는 플랫보다 눌러야 할 플렛이 더 높아서 손가락을 떼지 않고 추가로 누르기만 할 때
  
2. 떼는 시점
  - finger_stack[line][-1] > fret 일 때 -> 현재 누르고 있는 플렛보다 눌러야 할 플렛이 더 낮아서 현재 플렛에서 손을 떼야 할 때
'''

for i in range(n):
    line, fret = map(int, input().split())
    
    while finger_stack[line] and finger_stack[line][-1] > fret:
        # 떼고
        finger_stack[line].pop()
        cnt += 1 
    
    if not finger_stack[line] or finger_stack[line][-1] < fret:
        # 누르기
        finger_stack[line].append(fret)
        cnt += 1

    #=================================
    # 실패 1 : 시간 초과
    # -> 중복되는 내용을 줄이자
        
    # if not finger_stack[line]:
    #     # 현재 줄에 누르고 있는 프렛이 없을 경우 누르기
    #     finger_stack[line].append(fret)
    #     cnt += 1
    #     continue
        
    # if finger_stack[line][-1] < fret:
    #     # 누르기
    #     finger_stack[line].append(fret)
    #     cnt += 1
        
    # elif finger_stack[line][-1] == fret:
    #     continue
    
    # else:
    #     while True:            
    #         if finger_stack[line] and finger_stack[line][-1] > fret:
    #             # 떼고
    #             finger_stack[line].pop()
    #             cnt += 1 
                
    #         elif finger_stack[line] and finger_stack[line][-1] == fret:
    #             break
        
    #         else:
    #             #누르기
    #             finger_stack[line].append(fret)
    #             cnt += 1
    #             break

print(cnt)