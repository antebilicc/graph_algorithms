def fun(m):
    if not m:
        return 
    print(*m[0])
    fun(m[1:])

def main():
    fun(
        [[1,2,3],
        [2,2,2],
        [45,7, 8]]
    )

if __name__ == "__main__":
    main()