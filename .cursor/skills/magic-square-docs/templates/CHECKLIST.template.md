# magic-square-00 — 10선 검증 Checklist

| 항목 | 내용 |
|------|------|
| 프로젝트 | magic-square-00 |
| Checklist ID | CHECKLIST-NN |
| 일자 | YYYY-MM-DD |
| 격자 | <4×4 요약 또는 GRID 상수명> |
| Mom Test | [Report/01.REPORT.md](../../Report/01.REPORT.md) — SC1 부대각선 누락 방지 |

> **RULE-VAL-01**: 행 4 + 열 4 + 대각선 2 = **10선** 각 sum == 34일 때만 pass.  
> **하나라도 생략하면 Mom Test 증거 3(부대각선 38) 재현 실패.**

---

## 10선 체크 *(sum = 34?)*

| # | Line ID | 설명 | sum | pass |
|---|---------|------|-----|------|
| 1 | **R1** | 1행 | | ☐ |
| 2 | **R2** | 2행 | | ☐ |
| 3 | **R3** | 3행 | | ☐ |
| 4 | **R4** | 4행 | | ☐ |
| 5 | **C1** | 1열 | | ☐ |
| 6 | **C2** | 2열 | | ☐ |
| 7 | **C3** | 3열 | | ☐ |
| 8 | **C4** | 4열 | | ☐ |
| 9 | **D1** | 주대각선 ↘ | | ☐ |
| 10 | **D2** | 부대각선 ↙ | | ☐ |

**Magic Constant**: 34

---

## 코드 검증 *(선택)*

```bash
python -m pytest tests/test_validate_lines.py -v
```

| 결과 | status | failed_lines |
|------|--------|--------------|
| `validate_lines(<GRID>)` | | |

---

## 완료 판정

- [ ] 10선 **전부** 확인 *(D2 포함 — Mom Test 증거 3)*
- [ ] fail 줄이 있으면 ID 기록 — 행·열만 반복 **금지** *(증거 2)*
- [ ] 10선 pass 시에만 「완료」 *(증거 1 착각 방지)*

---

## 메모

<수동 검증·수업 메모>

---

*본 문서는 `Report/CHECKLIST-NN.md` — magic-square-00 10선 검증 Checklist입니다.*
