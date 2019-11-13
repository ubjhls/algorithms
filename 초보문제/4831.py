def solution(K, N, stops):
    answer = prev = 0
    status = K

    for i in range(len(stops) - 1):
        status -= stops[i] - prev

        if status < 0:
            return 0 
        if stops[i + 1] - stops[i] > status:
            status = K
            answer += 1
      
        prev = stops[i]

    last = stops[-1]
    status -= last - prev
    if N - last > K:
        return 0
    elif N - last > status:
        answer += 1
    return answer

def main():
    T = int(input())
    for test_case in range(T):
        K, N, M = map(int, input().split())
        stops = list(map(int, input().split()))
        print(f"#{test_case + 1} {solution(K, N, stops)}")
if __name__ == '__main__':
    main()