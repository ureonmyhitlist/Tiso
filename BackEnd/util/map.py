import math
import numpy as np

def binary_search(numbers, key, index):
    left = 0
    right = len(numbers)-1
    while left <= right:
        mid = (left + right) // 2
        if key[index] == numbers[mid][index]:
            return mid
        elif key[index] < numbers[mid][index]:
            right = mid - 1
        elif key[index] > numbers[mid][index]:
            left = mid + 1
    if right == -1:
        return 0
    elif left == len(numbers):
        return len(numbers)-1
    else:
        right_number = numbers[left][index]
        left_number = numbers[right][index]
            
        right_abs = abs(key[index] - right_number)
        left_abs = abs(key[index] - left_number)
        if right_abs == left_abs:
            return left
        elif right_abs > left_abs: # next is closer
            return right
        elif right_abs < left_abs:
            return left

def linear_search(coord_list,key,start=None,end=None):
    min_distance=math.dist(coord_list[0][0],key)
    min_distance_index=(0,0)
    if start==None:
        start=0
    if end==None:
        end=len(coord_list)
    else:#end로 들어온 인자는 실제 인덱스이기 때문에 range연산에 넣어줄 땐 +1을 해야 그곳까지 본다
        end+=1
    for i in range(start,end):
        for j in range(len(coord_list[0])):
            cur_distance=math.dist(coord_list[i][j],key)
            if min_distance>cur_distance:
                min_distance=cur_distance
                min_distance_index=(i,j)
    return min_distance_index

def lat_lon_array_binary_search(map:np.ndarray,key:tuple[float,float]) -> tuple[float,float]:
    # print("==========",key)

    #x=>행(위도)
    #y=>열(경도)
    last_column=len(map[0])-1
    last_row=len(map)-1

    x_up=0
    x_down=last_row
    y_left=0
    y_right=last_column
    # 찾는 key가 무조건 존재한다는 가정하에 조건을 분기
    while( x_up<=x_down and y_left<=y_right):
        x_mid=(x_up+x_down)//2
        y_mid=(y_left+y_right)//2
        cur_key=map[x_mid][y_mid]
        # print(f"x_up: {x_up} , x_down: {x_down}, y_left: {y_left} , y_right: {y_right}")
        # print(x_mid,y_mid)
        if key==cur_key:
            # 찾는 값과 일치한다면 바로 반환
            return (x_mid,y_mid)
        
        elif key[0]==cur_key[0]:
            # 위도가 같다면 위도의 범위를 한개로 좁힘
            x_up=x_mid
            x_down=x_mid

            if key[1]<cur_key[1]:
                # 경도가 더 작다면 경도의 범위를 왼쪽으로 좁힘
                y_right=y_mid-1

            elif key[1]>cur_key[1]:
                # 경도가 더 크다면 경도의 범위를 오른쪽으로 좁힘
                y_left=y_mid+1

        elif key[0]<cur_key[0]:
            # 위도가 더 작다면 위도의 범위를 아래로 좁힘 
            x_up=x_mid+1

            if key[1]>cur_key[1]:
                # 경도가 더 크다면 경도의 범위를 오른쪽으로 좁힘
                y_left=y_mid+1
            elif key[1]==cur_key[1]:
                # 경도가 같았다면 경도의 범위를 기준포함 오른쪽으로 좁힘
                y_left=y_mid

        elif key[0]>cur_key[0]:
            # 위도가 더 크다면 위도의 범위를 위로 좁힘
            x_down=x_mid-1
        
            if key[1]<cur_key[1]:
                # 경도가 더 작다면 경도의 범위를 왼쪽으로 좁힘
                y_right=y_mid-1
            elif key[1]==cur_key[1]:
                # 경도가 같다면 경도의 범위를 기준 포함 왼쪽으로 좁힘
                y_right=y_mid
    if x_up==x_down: 
        #특정 위도가 잡혔을 경우-
        min_y=map[x_up][0][1]
        max_y=map[x_up][last_column][1]
        if min_y<=key[1]<=max_y:
            return (x_up,binary_search(map[x_up],key,1))
        elif key[1]<min_y:
            #대전 영역 밖이므로 아웃
            return (-1,-1)
        elif max_y<key[1]:
            #대전 영역 밖이므로 아웃
            return (-1,-1)
    elif x_up!=len(map) and x_down!=-1:
        #특정 위도가 잡히진 않았지만 사이위도일 경우
        min_y=min(map[x_up][0][1],map[x_down][0][1])
        max_y=max(map[x_up][last_column][1],map[x_down][last_column][1])

        if min_y<=key[1]<=max_y:
            x_up_y=binary_search(map[x_up],key,1)
            x_down_y=binary_search(map[x_down],key,1)
            if math.dist(key,map[x_up][x_up_y])<math.dist(key,map[x_down][x_down_y]):
                return (x_up,x_up_y)
            else:
                return (x_down,x_down_y)
        elif key[1]<min_y:
            #대전 영역 밖이므로 아웃
            return (-1,-1)
        elif max_y<key[1]:
            #대전 영역 밖이므로 아웃
            return (-1,-1)
    elif x_down==-1:
        min_y=map[0][0][1]
        max_y=map[0][last_column][1]
        if min_y<=key[1]<=max_y:
            return (0,binary_search(map[0],key,1))
        elif key[1]<min_y:
            #대전 영역 밖이므로 아웃
            return (-1,-1)
        elif max_y<key[1]:
            #대전 영역 밖이므로 아웃
            return (-1,-1)
    elif x_up==len(map):
        min_y=map[last_row][0][1]
        max_y=map[last_row][last_column][1]
        if min_y<=key[1]<=max_y:
            return (last_row,binary_search(map[last_row],key,1))
        elif key[1]<min_y:
            return (last_row,0)
        elif max_y<key[1]:
            #대전 영역 밖이므로 아웃
            return (-1,-1)
    return (-1,-1)