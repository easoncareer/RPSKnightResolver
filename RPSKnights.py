import copy

MYCOUNT = 4
OPPS = 'SPRPRPRPPRPRRS'


class RPSKnightResolver():
    RPS = dict(
        R=0,
        P=1,
        S=2,
    )

    def win(self, me, opp):
        result = me - opp
        if result in [1, -2]:
            return True
        elif result in [-1, 2]:
            return False
        else:
            return None

    def convert_opps(self, opps):
        array_opps = []
        for opp in opps:
            array_opps.append(self.RPS[opp])
        return array_opps

    def create_team(self, n, count):
        team = []
        t = []
        if n == 0:
            t = [0]
        else:
            while n:
                n, r = divmod(n, 3)
                t.append(r)
        for i in range(count):
            try:
                team.append(t[i])
            except Exception:
                team.append(0)
        team = team[::-1]
        RPSteam = ''
        for n in team:
            RPSteam += self.RPS.keys()[self.RPS.values().index(n)]
        return RPSteam, team

    def team_fight(self, myteam, opps):
        while True:
            result = self.win(myteam[0], opps[0])
            if result is None:
                del (myteam[0])
                del (opps[0])
            elif result is True:
                del (opps[0])
                myteam.append(myteam.pop(0))
            else:
                del (myteam[0])
                opps.append(opps.pop(0))
            if len(opps) == 0 and len(myteam) == 0:
                return 'TIE', 0
            elif len(opps) == 0:
                return 'WIN', len(myteam)
            elif len(myteam) == 0:
                return 'LOST', len(opps)

    def build_my_team(self, count):
        my_teams = []
        for i in range(3 ** count):
            my_teams.append(self.create_team(i, count))
        return my_teams

    def startfight(self, count, opps):
        RPSopps = self.convert_opps(opps)
        myteams = self.build_my_team(count)
        final = []
        for RPSteam, team in myteams:
            r, n = self.team_fight(copy.copy(team), copy.copy(RPSopps))
            final.append((RPSteam, r, n))
        RPSwin = []
        RPStie = []
        for RPSteam, r, n in final:
            if r == 'WIN':
                RPSwin.append((RPSteam, n))
            elif r == 'TIE':
                RPStie.append((RPSteam, n))
        if len(RPSwin) > 0:
            RPSwin = sorted(RPSwin, key=lambda x: -x[1])
            team, num = RPSwin[0]
            print('%s - %s' % (team, num))
        elif len(RPStie) > 0:
            team, num = RPStie[0]
            print('%s - %s' % (team, num))
        else:
            print('NOT Possible.')
            for item in final:
                print(item)


RPSKnightResolver().startfight(MYCOUNT, OPPS)
