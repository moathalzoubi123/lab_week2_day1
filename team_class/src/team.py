class Team():

    def __init__(self, team, players, coach):
        self.name = team
        self.players = players
        self.coach = coach
        self.points = 0

       

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player):
        return player in self.players

    def play_game(self, win_or_loose):
        if win_or_loose == True:
            self.points += 3 
            
    