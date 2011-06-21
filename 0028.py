def main():
    i = 1
    sum_ = 0
    increment = 2
    for j in range((1001-1)/2):
        for f in 1, 2, 3, 4:
            i += increment 
            sum_ += i
        increment += 2
    print sum_ + 1


if __name__ == "__main__":
    main()
