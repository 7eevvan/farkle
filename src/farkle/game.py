import random


class Farkle:

    def __init__(self, num_dice, trials):
        self.num_dice = num_dice
        self.trials = trials


    def roll_dice(self):
        return [random.randint(1, 6) for _ in range(self.num_dice)]


    def calculate_score(self, dice):
        score = 0
        farkle = True
        combo = False
        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0
        count_5 = 0
        count_6 = 0
        pair_count = 0
        triple_count = 0
        quadruple_count = 0

        for n in dice:
            if n == 1:
                count_1 += 1
            if n == 2:
                count_2 += 1
            if n == 3:
                count_3 += 1
            if n == 4:
                count_4 += 1
            if n == 5:
                count_5 += 1
            if n == 6:
                count_6 += 1

        if count_1 == 2:
            pair_count += 1
        if count_2 == 2:
            pair_count += 1
        if count_3 == 2:
            pair_count += 1
        if count_4 == 2:
            pair_count += 1
        if count_5 == 2:
            pair_count += 1
        if count_6 == 2:
            pair_count += 1

        if count_1 == 3:
            triple_count += 1
        if count_2 == 3:
            triple_count += 1
        if count_3 == 3:
            triple_count += 1
        if count_4 == 3:
            triple_count += 1
        if count_5 == 3:
            triple_count += 1
        if count_6 == 3:
            triple_count += 1

        if count_1 == 4:
            quadruple_count += 1
        if count_2 == 4:
            quadruple_count += 1
        if count_3 == 4:
            quadruple_count += 1
        if count_4 == 4:
            quadruple_count += 1
        if count_5 == 4:
            quadruple_count += 1
        if count_6 == 4:
            quadruple_count += 1

        # check combos
        if count_1 == 3:
            score = 300
            farkle = False
        if count_2 == 3:
            score = 200
            farkle = False
        if count_3 == 3:
            score = 300
            farkle = False
        if count_4 == 3:
            score = 400
            farkle = False
        if count_5 == 3:
            score = 500
            farkle = False
        if count_6 == 3:
            score = 600
            farkle = False

        if quadruple_count == 1:
            score = 1000
            farkle = False
        if count_1 == 5 or count_2 == 5 or count_3 == 5 or count_4 == 5 or count_5 == 5 or count_6 == 5:
            score = 2000
            farkle = False
        if count_1 == 6 or count_2 == 6 or count_3 == 6 or count_4 == 6 or count_5 == 6 or count_6 == 6:
            score = 3000
            combo = True
            farkle = False
        if count_1 == count_2 == count_3 == count_4 == count_5 == count_6 == 1:
            score = 1500
            combo = True
            farkle = False
        if pair_count == 3:
            score = 1500
            combo = True
            farkle = False
        if triple_count == 2:
            score = 2500
            combo = True
            farkle = False
        if quadruple_count == 1 & pair_count == 1:
            score = 1500
            combo = True
            farkle = False

        # 1s and 5s
        if farkle or not combo:
            if count_1 == 1 or count_1 == 2:
                score += count_1 * 100
                farkle = False
            if count_5 == 1 or count_5 == 2:
                score += count_5 * 50
                farkle = False

        print(f"Score: {score}. Farkle: {farkle}. Dice: {dice}")
        return score

    def is_farkle(self, dice):
        score = 0
        farkle = True
        combo = False
        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0
        count_5 = 0
        count_6 = 0
        pair_count = 0
        triple_count = 0
        quadruple_count = 0

        for n in dice:
            if n == 1:
                count_1 += 1
            if n == 2:
                count_2 += 1
            if n == 3:
                count_3 += 1
            if n == 4:
                count_4 += 1
            if n == 5:
                count_5 += 1
            if n == 6:
                count_6 += 1

        if count_1 == 2:
            pair_count += 1
        if count_2 == 2:
            pair_count += 1
        if count_3 == 2:
            pair_count += 1
        if count_4 == 2:
            pair_count += 1
        if count_5 == 2:
            pair_count += 1
        if count_6 == 2:
            pair_count += 1

        if count_1 == 3:
            triple_count += 1
        if count_2 == 3:
            triple_count += 1
        if count_3 == 3:
            triple_count += 1
        if count_4 == 3:
            triple_count += 1
        if count_5 == 3:
            triple_count += 1
        if count_6 == 3:
            triple_count += 1

        if count_1 == 4:
            quadruple_count += 1
        if count_2 == 4:
            quadruple_count += 1
        if count_3 == 4:
            quadruple_count += 1
        if count_4 == 4:
            quadruple_count += 1
        if count_5 == 4:
            quadruple_count += 1
        if count_6 == 4:
            quadruple_count += 1

        # check combos
        if count_1 == 3:
            score = 300
            farkle = False
        if count_2 == 3:
            score = 200
            farkle = False
        if count_3 == 3:
            score = 300
            farkle = False
        if count_4 == 3:
            score = 400
            farkle = False
        if count_5 == 3:
            score = 500
            farkle = False
        if count_6 == 3:
            score = 600
            farkle = False

        if quadruple_count == 1:
            score = 1000
            farkle = False
        if count_1 == 5 or count_2 == 5 or count_3 == 5 or count_4 == 5 or count_5 == 5 or count_6 == 5:
            score = 2000
            farkle = False
        if count_1 == 6 or count_2 == 6 or count_3 == 6 or count_4 == 6 or count_5 == 6 or count_6 == 6:
            score = 3000
            combo = True
            farkle = False
        if count_1 == count_2 == count_3 == count_4 == count_5 == count_6 == 1:
            score = 1500
            combo = True
            farkle = False
        if pair_count == 3:
            score = 1500
            combo = True
            farkle = False
        if triple_count == 2:
            score = 2500
            combo = True
            farkle = False
        if quadruple_count == 1 & pair_count == 1:
            score = 1500
            combo = True
            farkle = False

        # 1s and 5s
        if farkle or not combo:
            if count_1 == 1 or count_1 == 2:
                score += count_1 * 100
                farkle = False
            if count_5 == 1 or count_5 == 2:
                score += count_5 * 50
                farkle = False

        print(f"Farkle: {farkle}. Score: {score}. Dice: {dice}")
        if score == 0:
            return True
        else:
            return False


    def calculate_farkle_percentage(self):
        count = 0
        print("Results")
        for _ in range(self.trials):
            dice = self.roll_dice()
            farkle = self.is_farkle(dice)
            if farkle:
                count += 1
        return (count / self.trials) * 100


    def calculate_average(self):
        total = 0
        print("Results")
        for _ in range(self.trials):
            dice = self.roll_dice()
            score = self.calculate_score(dice)
            total += score
        return total / self.trials

    def calculate_score_and_farkle_percentage(self):
        total_score = 0
        farkle_count = 0

        for _ in range(self.trials):
            dice = self.roll_dice()
            score = self.calculate_score(dice)
            total_score += score

            if score == 0:
                farkle_count += 1

        average_score = total_score / self.trials
        farkle_percentage = (farkle_count / self.trials) * 100

        return average_score, farkle_percentage
