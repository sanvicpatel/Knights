from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),    # A is either a knight or a knave
    Not(And(AKnight, AKnave)),  # A is not both a knight and a knave

    # A says "I am both a knight and a knave."
    Implication(AKnight, And(AKnight, AKnave)),     # If A is a knight, then it would be both a knight and a knave
    Implication(AKnave, Not(And(AKnight, AKnave)))  # If A is a knave, then it would not be both a knight and a knave
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),    # A is either a knight or a knave
    Not(And(AKnight, AKnave)),  # A is not both a knight and a knave
    Or(BKnight, BKnave),    # B is either a knight or a knave
    Not(And(BKnight, BKnave)),  # B is not both a knight and a knave

    # A says "We are both knaves."
    Implication(AKnight, And(AKnave, BKnave)),  # If A is a knight, then both A and B are knaves
    Implication(AKnave, Not(And(AKnave, BKnave)))   # If A is a knave, then both A and B are not knaves
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),    # A is either a knight or a knave
    Not(And(AKnight, AKnave)),  # A is not both a knight and a knave
    Or(BKnight, BKnave),    # B is either a knight or a knave
    Not(And(BKnight, BKnave)),  # B is not both a knight and a knave

    # A says "We are the same kind."
    # If A is a knight, then both A and B are knights OR both A and B are knaves
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a knave, then both A and B are not knights AND both A and B are not knaves
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),

    # B says "We are of different kinds."
    # If B is a knight, then A and B are of different kinds (A:Knight, B:Knave OR A:Knave, B:Knight)
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # If B is a knave, then A and B are NOT of different kinds
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

knowledge3 = And(
    Or(AKnight, AKnave),    # A is either a knight or a knave
    Not(And(AKnight, AKnave)),  # A is not both a knight and a knave
    Or(BKnight, BKnave),    # B is either a knight or a knave
    Not(And(BKnight, BKnave)),  # B is not both a knight and a knave
    Or(CKnight, CKnave),    # C is either a knight or a knave
    Not(And(CKnight, CKnave)),  # C is not both a knight and a knave

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    # If A said "I am a knight": If A is a knight, it is a knight. If A is a knave, then it is not a knight.
    # Or, if A said "I am a knave": If A is a knight, it is a knave. If A is a knave, it is not a knave.
    Or(And(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight))),
       And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))),

    # B says "A said 'I am a knave'."
    # If B is a knight, then A said "I am a knave".
    # If A said "I am a knave":  If A is a knight, it is a knave. If A is a knave, it is not a knave.
    Implication(BKnight, And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))),
    # If B is a knave, then A did not say "I am a knave". We put Not() around the second argument of the previous line.
    Implication(BKnave, Not(And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))))),

    # B says "C is a knave."
    Implication(BKnight, CKnave),   # If B is a knight, then C is a knave
    Implication(BKnave, Not(CKnave)),   # If B is a knave, then C is not a knave

    # C says "A is a knight."
    Implication(CKnight, AKnight),  # If C is a knight, then A is a knight
    Implication(CKnave, Not(AKnight))   # If C is a knave, then A is not a knight
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
