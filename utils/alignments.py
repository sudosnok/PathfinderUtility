class Alignment:
    x: int
    y: int
    #
    # 0,0:LG | 0,1:NG | 0,2:CG
    # 1,0:LN | 1,1:TN | 1,2:CN
    # 2,0:LE | 2,1:NE | 2,2:CE
    #
    # treat alignment as a 3x3 grid, top to bottom, left to right
    # to calculate all alignments within a step;
    # divmod(position, 3) gives y, x coord; eg; divmod(5, 3) = 1, 2
    # with y, x == (1, 2), all steps are (0, 2), (1, 1), (2, 2)
    # there must be an easier way, but I'm going to be lazy about this (hope it doesn't bite me in the ass)

    graph: dict[tuple[int, int], tuple[str]] = {
        (0,0): ('NG', 'LN'),        (0,1): ('LG', 'TN', 'CG'),          (0,2): ('NG', 'CN'),
        (1,0): ('LG', 'TN', 'LE'),  (1,1): ('NG', 'CN', 'NE', 'LN'),    (1,2): ('CG', 'TN', 'CE'),
        (2,0): ('LN', 'NE'),        (2,1): ('LE', 'TN', 'CE'),          (2,2): ('NE', 'CN'),
    }

    dispatch: dict[str, tuple[int, int]] = {
        'LG': (0,0), 'NG': (0,1), 'CG': (0,2),
        'LN': (1,0), 'TN': (1,1), 'CN': (1,2),
        'LE': (2,0), 'NE': (2,1), 'CE': (2,2),
    }

    def __init__(self, alignment: str) -> None:
        alignment = alignment.upper()
        self.y, self.x = self.dispatch[alignment]

    def one_step(self) -> tuple[str]:
        return self.graph[(self.x, self.y)]
