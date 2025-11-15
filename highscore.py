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
        with open(highscore_path, 'r') as fd:
            return HighScores.model_validate_json(fd.read())
    return HighScores(scores=[])


def check_score(score: float) -> bool:
    high_scores = load_scores()
    if len(high_scores.scores) < 3:
        return True
    else:
        for record in high_scores.scores:
            if score > record.score:
                return True
    return False


def record_score(initials: str, score: float):
    high_scores = load_scores()
    high_scores.scores.append(Score(initials=initials[:3], score=score))
    high_scores.scores.sort(key=lambda s: s.score, reverse=True)
    high_scores.scores = high_scores.scores[:3]

    for record in high_scores.scores:
        print(f'{record.initials}: {record.score}')
    highscore_path = Path('highscore.json')
    with open(highscore_path, 'w') as fd:
        fd.write(high_scores.model_dump_json(indent=4))
