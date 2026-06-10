---
name: magic-square-tdd
description: >-
  magic-square-00 validate_lines ARRR TDD 워크플로. RED 설계·스켈레톤,
  GREEN 최소 구현, Golden Master, REFACTOR 스멜·안전 리팩터 Command 체인을
  따른다. /red-test-plan, /red-skeleton, /green-minimal, /golden-master,
  /refactor-smell, /refactor-safe, TDD, ARRR, validate_lines, pytest RED GREEN
  REFACTOR 작업 시 사용.
---

# magic-square-tdd — ARRR · validate_lines TDD

## SSOT

| 우선 | 문서 |
|------|------|
| 1 | `.cursorrules` — Entity · Control · Boundary · TDD |
| 2 | `docs/PRD.md` — FR · Test Loop *(없으면 `.cursorrules` + `Report/03.REPORT.md`)* |
| 3 | `.cursor/commands/*.md` — 슬래시 Command 절차 |

**추가 입력·질문 금지** — Command는 슬래시명만으로 SSOT·코드 상태를 읽고 자동 진행한다.

---

## ARRR ↔ Command 체인

| ARRR | 활동 | Command | 수정 범위 |
|------|------|---------|-----------|
| **A — Ask** | RED ③ 설계 | `/red-test-plan` | *(없음)* |
| **A — Ask** | RED ④ 스켈레톤 | `/red-skeleton` | `tests/` |
| **R — Respond** | GREEN ⑤ | `/green-minimal` | `src/` |
| **R — Respond** | Golden ⑥ | `/golden-master` | `tests/golden/` *(+ harness)* |
| **R — Refine** | REFACTOR ⑦ | `/refactor-smell` | *(없음)* |
| **R — Refine** | REFACTOR ⑧ | `/refactor-safe` | `src/` |
| **R — Repeat** | Export | `/export-session` | `Report/`, `Prompting/` |

### 권장 1사이클

```
/red-test-plan → /red-skeleton → /green-minimal (×N) → /golden-master
→ /refactor-smell → /refactor-safe → /export-session
```

레거시: `/tdd-red` = `/red-skeleton`과 동일 Phase (`Phase: RED`).

---

## 도메인 요약

- **격자**: 4×4, 빈칸 `0`, 채워진 칸 `1~16`
- **마법상수**: 34
- **10선 ID**: R1, R2, R3, R4, C1, C2, C3, C4, D1, D2
- **API**: `validate_lines(grid) -> {status, failed_lines}`
  - `pass` — 10선 모두 34
  - `fail` — 빈칸 없음, 하나 이상 ≠ 34 → `failed_lines`에 ID
  - `incomplete` — `0` 포함 → `failed_lines: []`

### Boundary Test Loop

| Case | 기대 | Mom Test |
|------|------|----------|
| Red-T1 | D2 fail, `"D2" ∈ failed_lines` | 증거 3 — 부대각선 38 |
| Green-T1 | pass, `failed_lines == []` | 증거 1 — 행·열만 34 착각 방지 |
| Red-T2 | incomplete | 빈칸 분기 |

---

## TDD 규칙 (엄격)

- 한 사이클 = **RED 케이스 1개**
- **assert 완화**, `@pytest.mark.skip`, `xfail` **금지**
- RED → `tests/` only · GREEN/REFACTOR → `src/` only
- **Phase 선언**: 응답 첫 줄 `Phase: RED` | `GREEN` | `REFACTOR` | `GOLDEN` | `RED (Ask)` | `REFACTOR (Ask)`
- **한국어** 소통
- git commit — **사용자 명시 시만**
- 솔버 · UI · ECB · Hook/MCP — **범위 밖**

---

## Command 자동 판단 요약

| Command | 자동 선정 |
|---------|-----------|
| `/red-test-plan` | Boundary 우선순위에서 **미구현** 첫 Case 설계표 |
| `/red-skeleton` | 동일 우선순위 → tests/에 test 1개 |
| `/green-minimal` | pytest **첫 FAIL** 1건 최소 통과 |
| `/golden-master` | pytest **전부 PASS** 후 미생성 golden 1 Case |
| `/refactor-smell` | src/ 스멜 P0~P2 표 |
| `/refactor-safe` | To-Do #1 또는 P0 1건, Budget 내 |

---

## pytest

```bash
python -m pytest tests/test_validate_lines.py -v
```

- RED: **의도적 FAIL** 확인
- GREEN · REFACTOR · GOLDEN: **전부 PASS** 목표

---

## 문서 Export

세션 마감 시 **magic-square-docs** Skill 또는 `/export-session` — `Report/NN.REPORT.md` + `Prompting/NN.Export-Transcript.md`.
