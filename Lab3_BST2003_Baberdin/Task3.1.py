import time
import string
#Алгоритм Кнута-Морриса-Пратта
def prefix(s):
    v = [0]*len(s)
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v

def kmp(s, t):
    index = -1
    f = prefix(s)
    k = 0
    for i in range(len(t)):
        while k > 0 and s[k] != t[i]:
            k = f[k-1]
        if s[k] == t[i]:
            k = k + 1
        if k == len(s):
            index = i - len(s) + 1
            break
    return index

#Упрощенный Бойера-Мура
def bmPredCompil(x):
    d = {}
    lenX = len(x)
    for i in range(len(x)):
        # сколько символов с правого края до этой буквы
        d[ord(x[i])] = lenX - i
    return d


def boyerMurSearch(x, s):
    d = bmPredCompil(x)
    # k - проход по s
    # j - проход по x
    # i - место начала прохода по s
    lenX = i = j = k = len(x)
    while j > 0 and i <= len(s):
        # совпали, двигаемся дальше (от конца к началу)
        if s[k - 1] == x[j - 1]:
            k -= 1
            j -= 1
        # иначе, продвигаемся по строке на d и начинаем с правого конца подстроки снова
        else:
            i += d[ord(s[i])]
            j = lenX
            k = i
    if j <= 0:  # нашли
        return k
    return None  # не нашли


def search(s, t, alg=kmp, ignore_case=False, ignore_space=False):
    if ignore_case:
        s = s.lower()
        t = t.lower()

    if ignore_space:
        s = s.replace(' ', '')
        t = t.replace(' ', '')

    return alg(s, t)

#Вывод
alg = {
    'Кнута-Морриса-Пратта': kmp,
    'Бойера-Мура': boyerMurSearch,
}

for key, a in alg.items():
    time_start = time.perf_counter()
    search('acD', 'aaaacd', alg=a, ignore_case=True, ignore_space=True)
    print(f'{key} - {time.perf_counter() - time_start}')

time_start = time.perf_counter()
'aaaacd'.find('acD')
print(f'Встроенная сортировка - {time.perf_counter() - time_start}')