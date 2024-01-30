from pydantic import BaseModel
from pathlib import Path


class Score(BaseModel):
    initials: str
    score: float


class HighScores(BaseModel):
    scores: list[Score]


def load_scores():
    highscore_path = Path('highscore.json')
    if highscore_path.exists():
        return HighScores.parse_file(highscore_path)
    return HighScores(scores=[])


def record_score(score: float):
    high_scores = load_scores()
    if len(high_scores.scores) < 3:
        print("You got a new high score!")
        initials = input("Type your initials: ")
        high_scores.scores.append(Score(initials=initials[:3], score=score))
    else:
        for record in high_scores.scores:
            if record.score > score:
                print("You got a new high score.")
                initials = input("Type your initials: ")
                high_scores.scores.append(Score(initials=initials[:3], score=score))
    high_scores.scores.sort(key=lambda s: s.score, reverse=True)
    high_scores.scores = high_scores.scores[:3]

    for record in high_scores.scores:
        print(f'{record.initials}: {record.score}')
    highscore_path = Path('highscore.json')
    with open(highscore_path, 'w') as fd:
        fd.write(high_scores.json(indent=4))