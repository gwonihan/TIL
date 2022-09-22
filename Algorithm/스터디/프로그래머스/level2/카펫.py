#카펫
def solution(brown, yellow):
    answer = []
    
    import math
    total_grid = brown + yellow
    root = total_grid ** (1/2)
    
    width = math.ceil(root)
    vertical = math.floor(root)
    
    while True:
        if width * vertical == total_grid:
            answer.append(width)
            answer.append(vertical)
            break
        elif width * vertical < total_grid:
            width += 1
        elif width * vertical > total_grid:
            vertical -= 1

    return answer