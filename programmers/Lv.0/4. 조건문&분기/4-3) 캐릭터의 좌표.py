def solution(keyinput, board):
    #현재 위치
    x,y = 0, 0
    
    #이동
    move = {
        'up': (0, 1),
        'down': (0, -1),
        'left': (-1, 0),
        'right': (1, 0)
    }

    # 이동 가능 최대 범위
    max_x = board[0] // 2
    max_y = board[1] // 2

    # 입력 처리
    for key in keyinput:
        dx, dy = move[key] # 방향키에 맞게 x, y 좌표 입력
        nx, ny = x + dx, y + dy
        
        # 경계 검사
        if -max_x <= nx <= max_x:
            x = nx
        if -max_y <= ny <= max_y:
            y = ny
    
    return [x, y]