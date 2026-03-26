votes = []
while True:
    ID = int(input("enter your ID:"))
    if ID == -999:
        break
    if not 1 <= ID <= 100:
        continue
    votes.append(ID)

legal_voters = set()
invalid_voters = set()

for voter in set(votes):
    if votes.count(voter) == 1:
        legal_voters.add(voter)
    else:
        invalid_voters.add(voter)

print(f"legal voters: {legal_voters}")
print(f"invalid voters: {invalid_voters}")
print(f"Number of voting attempts today {len(votes)}")









