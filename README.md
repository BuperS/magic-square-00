# magic-square-00

4×4 부분 마방진에서 **10선**(행 4 + 열 4 + 대각선 2)의 합 34 여부를 한 번에 판정하는 `validate_lines` 프로젝트.

Mom Test에서 도출한 진짜 문제 — 검증 줄 누락(특히 **부대각선 D2**)으로 인한 잘못된 “완료” 판정과 시간 낭비 — 를 **Rule + Command + Test Loop** 로 다룬다.

| 항목 | 내용 |
|------|------|
| 버전 | v0.2 |
| SSOT | [docs/PRD.md](docs/PRD.md) → [.cursorrules](.cursorrules) → `Report/*.REPORT.md` |
| Mom Test | [Report/01.REPORT.md](Report/01.REPORT.md) *(⚠️ [시뮬레이션])* |

---

## 문제 (한 문장)

부분 마방진을 다 맞췄다고 **확신**했지만, 검사해야 할 줄·대각선 중 **하나(부대각선)를 빠뜨린 채** 행·열만 반복 검증했고, 그 **잘못된 “완료” 판정** 위에서 **약 35분**을 허비한 뒤에야 누락을 알게 되었다.

---

## API

```python
from src.validate_lines import validate_lines

result = validate_lines(grid)  # grid: 4×4 list[list[int]]
# → { "status": "pass" | "fail" | "incomplete", "failed_lines": [...] }
```

| status | 조건 | failed_lines |
|--------|------|--------------|
| `pass` | 10선 모두 sum == 34 | `[]` |
| `fail` | 빈칸 없음, 하나 이상 sum ≠ 34 | 해당 줄 ID *(예: `["D2"]`)* |
| `incomplete` | `0`(빈칸) 포함 | `[]` |

### 도메인

- 격자: 4×4, 빈칸 `0`, 채워진 칸 `1~16`
- 마법상수: **34**
- 10선 ID: **R1~R4**, **C1~C4**, **D1**(주대각), **D2**(부대각)

---

## 빠른 시작

```bash
# 의존성 (pytest)
pip install -e ".[dev]"

# 테스트
python -m pytest tests/test_validate_lines.py -v
```

---

## Test Loop

| Case | 의도 | 기대 |
|------|------|------|
| **Red-T1** | D2 sum = 38 | `status == "fail"`, `"D2" in failed_lines` |
| **Green-T1** | 10선 모두 34 | `status == "pass"`, `failed_lines == []` |
| **Red-T2** | 빈칸(0) 포함 | `status == "incomplete"`, `failed_lines == []` |

상세 격자·스키마는 [docs/PRD.md §6](docs/PRD.md) 참조.

---

## TDD · ARRR

| Phase | 수정 범위 | Command |
|-------|-----------|---------|
| RED | `tests/` only | `/red-test-plan` → `/red-skeleton` |
| GREEN | `src/` only | `/green-minimal` |
| Golden | `tests/golden/` | `/golden-master` *(pytest 전부 PASS 후)* |
| REFACTOR | `src/` only | `/refactor-smell` → `/refactor-safe` |
| Export | `Report/`, `Prompting/` | `/export-session` |

**금지**: assert 완화, `skip`/`xfail`, RED 단계에서 `src/` 수정.

권장 1사이클:

```
/red-test-plan → /red-skeleton → /green-minimal → /golden-master
→ /refactor-smell → /refactor-safe → /export-session
```

---

## 프로젝트 구조

```
magic-square-00/
├── README.md                  ← 본 문서
├── docs/
│   └── PRD.md                 ← 요구사항 SSOT
├── .cursorrules
├── .cursor/commands/          ← ARRR 슬래시 Command
├── src/
│   └── validate_lines.py      ← FR-VAL-01
├── tests/
│   ├── test_validate_lines.py
│   └── golden/                ← (선택) Golden Master
├── Report/                    ← NN.REPORT.md
└── Prompting/                 ← NN.Export-Transcript.md
```

---

## 범위 밖 (In Scope 아님)

- ECB 구조 전체 · 마방진 솔버 · GridUI 앱
- 1~16 중복·누락·범위 검증 *(v0.3+ FR-VAL-02)*
- Hook · MCP

---

## 참조

| 문서 | 역할 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | FR · Test Loop · 세션 로드맵 |
| [.cursorrules](.cursorrules) | Entity · Control · Boundary · TDD |
| [Report/01.REPORT.md](Report/01.REPORT.md) | Mom Test 원본 |
| [Report/03.REPORT.md](Report/03.REPORT.md) | 세션 3 워크북 |
| [Report/04.REPORT.md](Report/04.REPORT.md) | 계약 리뷰 |

---

*README — magic-square-00 v0.2. 상세 요구사항은 [docs/PRD.md](docs/PRD.md)를 따른다.*
