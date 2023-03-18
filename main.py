# python3

def parallel_processing(n, m, data):
    output = []
    thr = [(0, i) for i in range (n)]

    for i in range(m):
        start, thri = thr.pop(0)
        output.append((thri, start))
        end = start + data[i]
        thr.append((end, thri))
        thr.sort()

    return output

def main():
    
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)

    for thri, start in result:
        print(thri, start)
    
if __name__ == "__main__":
    main()
