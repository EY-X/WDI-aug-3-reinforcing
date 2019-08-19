ballots = [
            {'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
            {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
            {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
            {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
            {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
            {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}
        ]


points = {
    'gold': 3,
    'silver': 2,
    'bronze': 1
    }

final_score = {}

for ballot in ballots:
    for x, y in ballot.items():
        stats = points[x]
        if y in final_score.keys():
            final_score[y] += stats
        else:
            final_score[y] = 0
        
first_place = max(final_score, key=final_score.get)
print(first_place)


# Each dictionary represents
# a voting ballot, with
# three names in gold, silver, and bronze tiers. 
# A 'gold' is worth 3 points, 'silver' is worth 2 points, 
# and 'bronze' is worth 1 point.

# For example, 
# the first ballot {'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'} 
# shows that this voter chose Smudge for first place, Tigger for 2nd, and Simba for 3rd. 
# Smudge would be awarded 3 points, Tigger would be awarded 2 points, and Simba would be awarded 1 point.

# Tally up all the votes and determine who won.