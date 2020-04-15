# def solution(phone_book):
#     answer = True
#     phone_book = sorted(phone_book, key=lambda x: len(x))
#     for i in range(len(phone_book)):
#         temp = len(phone_book[i])
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i] == phone_book[j][:temp+1]:
#                 return False
#     return answer

def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    print(list(zip(phoneBook, phoneBook[1:])))
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1,p2)
        if p2.startswith(p1):
            return False
    return True

phone_book = ["12","123","1235","567","88"]
solution(phone_book)