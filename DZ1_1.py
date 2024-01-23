import heapq


def connect_cables(cables):
    heapq.heapify(cables)
    cost = 0

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        new_cable = cable1 + cable2
        cost += new_cable
        heapq.heappush(cables, new_cable)
    return cost


cables = [12, 17, 4, 7, 25, 40, 6, 10, 11]
print(f"Мінімальна сума загальних витрат = {connect_cables(cables)}")
