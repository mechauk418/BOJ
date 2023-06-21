import heapq

def solution(book_time):
    answer = 0
    min_book_time = []

    for i in range(len(book_time)):

        start_hour = int(book_time[i][0].split(':')[0])*60
        start_min = int(book_time[i][0].split(':')[1])
        start = start_hour+start_min

        end_hour = int(book_time[i][1].split(':')[0]) * 60
        end_min = int(book_time[i][1].split(':')[1]) + 10
        end = end_hour + end_min

        min_book_time.append([start,end])

    min_book_time.sort(key=lambda x:(x[0]))
    cnt = 1

    b = [0]

    for start, end in min_book_time:
        if start >= b[0]:
            heapq.heappop(b)
        else:
            cnt += 1
        heapq.heappush(b, end)

    answer = cnt

    return answer