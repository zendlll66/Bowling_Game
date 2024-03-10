"""The Bowling Game Scorer."""

# Standard Library

# 3rd Party Library

# Project Library


# -----------------------------------------------------------------------------
class BowlingFrame:
    """Keeping the record of each bowling frame."""

    def __init__(self, max_roll=2):
        """Construct a frame."""
        self.pins = [0] * max_roll
        self.max_roll = max_roll
        self.next_roll = 0

    def roll(self, pins: int):
        """Roll the ball and swipe pins."""
        if self.next_roll < self.max_roll:
            self.pins[self.next_roll] = pins
            self.next_roll += 1

    def score(self):
        """Calculate the score of the frame."""
        total = sum(self.pins)
        return total

    def is_spare(self):
        """Check if the current frame is a spare."""
        return self.score() == 10 and self.pins[0] != 10

    def is_strike(self):
        """Check if the current frame is a strike."""
        return self.pins[0] == 10


class BowlingFrame10(BowlingFrame):
    """Keeping the record of the 10th bowling frame."""

    def __init__(self):
        """Construct a frame."""
        super().__init__(3)


class BowlingGame:
    """The Bowling Game."""

    def __init__(self):
        """Construct a BowlingGame object."""
        self.frames = [BowlingFrame() for _ in range(9)]
        self.frames.append(BowlingFrame10())
        self.cur_frame = 0
        self.cur_roll = 1

    def roll(self, num_of_pins: int):
        """Roll a bowling ball."""
        frame = self.frames[self.cur_frame]
        frame.roll(num_of_pins)
        
        if frame.is_strike() or frame.next_roll == 2:
            self.cur_frame += 1
            self.cur_roll = 1
        else:
            self.cur_roll += 1

    def score(self):
        """Get the current score."""
        total_score = 0
        for frame in self.frames:
            total_score += frame.score()
            if frame.is_spare():
                next_frame = self.frames[self.frames.index(frame) + 1]
                total_score += next_frame.pins[0]
            elif frame.is_strike():
                next_frame = self.frames[self.frames.index(frame) + 1]
                total_score += next_frame.pins[0]
                if next_frame.is_strike() and not isinstance(next_frame, BowlingFrame10):
                    next_next_frame = self.frames[self.frames.index(frame) + 2]
                    total_score += next_next_frame.pins[0]
        return total_score

