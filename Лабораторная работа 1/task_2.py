# TODO Найдите количество книг, которое можно разместить на дискете
size_mb = 1.44
pages = 100
lines = 50
symbols = 25
bytes_for_symbol = 4

size_bytes = size_mb * 1024 * 1024
count_all_symbols = symbols * lines * pages
book_size = count_all_symbols * bytes_for_symbol
count_books = int(size_bytes // book_size)

print("Количество книг, помещающихся на дискету:", count_books)
