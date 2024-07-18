N, M = map(int, input().split())
books = sorted(list(map(int, input().split())))

minus_books = sorted(list(map(abs, filter(lambda x:x<0, books))))
plus_books = list(filter(lambda x:x>0, books))
spots = []

def collecting(books:list):
    global spots, M
    start = len(books) % M
    if start == 0:
        start = M
    for book in books[start-1::M]:
        spots.append(book)
collecting(minus_books)
collecting(plus_books)
print(2 * sum(spots) - max(spots))