def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if len(phone_book[i]) > len(phone_book[j]):
                if (phone_book[i].find(phone_book[j]) == 0):
                    return False
            else:
                if (phone_book[j].find(phone_book[i]) == 0):
                    return False
    return True


def solution(phone_book):
    phone_book.sort(key=len)
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if len(phone_book[i]) < len(phone_book[j]):
                if (phone_book[j].find(phone_book[i]) == 0):
                    return False
    return True
