class RandomPlayer:
  def __init__(self):
    self.name = 'Random Player'
    self.score = 0
    self.data = []

  def bid(self, purse, current_bids, totalscores):
    import random
    return random.randint(-1, 10)
  
  def round_result(self, my_chance, bids, results):
    self.score += results[my_chance-1]
    if (my_chance==3):
      self.data.append(results[my_chance-1])

class Aggressive:
  def __init__(self):
    self.name = 'Aggressive Player'
    self.score = 0

  def bid(self, purse, bids, totalscores):
    if (purse<20): 
      return -1
    if len(bids) == 0:
      return 30
    if len(bids) == 1:
      return purse-5
    if len(bids) == 2:
      return purse
    if len(bids) == 3:
      return purse
    return -1
  
  def round_result(self, my_chance, bids, results):
    self.score += results[my_chance-1]
    
class ConservativePlayer:
    def __init__(self):
        self.name = 'Conservative Player'
        self.score = 0

    def bid(self, purse, current_bids, totalscores):
        if purse > 40:
            return 5
        elif purse > 20:
            return 3
        else:
            return -1  # Decline if purse is too low

    def round_result(self, my_chance, bids, results):
        self.score += results[my_chance-1]

class AdaptivePlayer:
    def __init__(self):
        self.name = 'Adaptive Player'
        self.score = 0
        self.round_count = 0

    def bid(self, purse, current_bids, totalscores):
        self.round_count += 1
        if self.round_count % 10 == 0:
            return 40  # Every 10 rounds, bid high
        if purse > 30:
            return 15
        elif purse > 10:
            return 10
        else:
            return -1

    def round_result(self, my_chance, bids, results):
        self.score += results[my_chance-1]
class HarshitKansal:
    def __init__(self):
        self.name = 'Harshit Kansal'
        self.score = 0

    def bid(self, purse, current_bids, totalscores):
        # Identify player's position on the leaderboard
        my_position = sorted(range(len(totalscores)), key=lambda k: totalscores[k], reverse=True).index(self.score)

        # Case 1: First bid chance
        if len(current_bids) == 0:
            if my_position == 0:
                return 16
            elif my_position == 1:
                return 18
            else:
                return 21
        
        # Case 2: Second bid chance
        elif len(current_bids) == 1:
            first_bidder_position = sorted(range(len(totalscores)), key=lambda k: totalscores[k], reverse=True).index(totalscores[0])
            first_bid = current_bids[0]
            if first_bidder_position == 0 and first_bid > 16:
                return first_bid - 1
            elif first_bid > 20:
                return first_bid - 1
            else:
                return purse // 2 + 1 if first_bidder_position != 0 else first_bid // 2 + 4
        
        # Case 3: Third bid chance
        elif len(current_bids) == 2:
            declines = current_bids.count(-1)
            second_bidder_position = sorted(range(len(totalscores)), key=lambda k: totalscores[k], reverse=True).index(totalscores[1])
            second_bid = current_bids[1]
            if declines == 2:
                return -1
            elif declines == 1:
                if second_bidder_position == 0 and second_bid > 18:
                    return second_bid - 1
                else:
                    return purse // 2 + 1 if second_bidder_position != 0 else purse // 2 + 4
            else:
                if second_bid > 22:
                    return second_bid - 1
                else:
                    return purse // 2 + 1 if second_bidder_position != 0 else purse // 2 + 4
        
        # Case 4: Fourth bid chance
        elif len(current_bids) == 3:
            declines = current_bids.count(-1)
            third_bidder_position = sorted(range(len(totalscores)), key=lambda k: totalscores[k], reverse=True).index(totalscores[2])
            third_bid = current_bids[2]
            if declines == 3 or (declines == 2 and third_bid == 0):
                return -1
            elif declines == 1:
                if third_bidder_position == 0:
                    return -1
                else:
                    return purse if purse > 14 else -1
            else:
                return purse

    def round_result(self, my_chance, bids, results):
        self.score += results[my_chance-1]

# Adding HarshitKansal player to the game

