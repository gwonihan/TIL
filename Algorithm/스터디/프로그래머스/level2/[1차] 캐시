def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    cities = [city.lower() for city in cities]
    
    if cacheSize != 0:
        for city in cities:
            if city not in cache:
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
    else:
        answer = len(cities) * 5
    return answer