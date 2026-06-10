"""Control: 4×4 마방진 10선 검증 Command."""

from typing import Literal, TypedDict

MAGIC_CONSTANT = 34

LINE_IDS = (
    "R1",
    "R2",
    "R3",
    "R4",
    "C1",
    "C2",
    "C3",
    "C4",
    "D1",
    "D2",
)

Status = Literal["pass", "fail", "incomplete"]


class ValidateResult(TypedDict):
    status: Status
    failed_lines: list[str]


def validate_lines(grid: list[list[int]]) -> ValidateResult:
    """10선(R1~R4·C1~C4·D1·D2) 합 34 여부를 검증한다.

    Returns:
        status: pass | fail | incomplete
        failed_lines: sum ≠ 34인 줄 ID 목록 (incomplete 시 빈 배열)
    """
    ...
