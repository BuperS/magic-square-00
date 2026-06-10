# magic-square-00 — Product Requirements Document (PRD)

| 항목 | 내용 |
|------|------|
| 프로젝트 | magic-square-00 |
| 버전 | **v0.2** |
| 일자 | 2026-06-10 |
| SSOT 우선순위 | **본 문서** → `.cursorrules` → `Report/*.REPORT.md` |
| Mom Test 근거 | [Report/01.REPORT.md](../Report/01.REPORT.md) *(⚠️ [시뮬레이션])* |
| 세션 3 워크북 | [Report/03.REPORT.md](../Report/03.REPORT.md) |
| 계약 리뷰 | [Report/04.REPORT.md](../Report/04.REPORT.md) |

> **계약 확정 (v0.2)**  
> [Report/04.REPORT.md](../Report/04.REPORT.md) 리뷰에서 지적된 워크북(§5)의 `row_*` / `diag_secondary`·줄별 `{ line_id, sum, pass }` 스키마는 **초안**이었다.  
> 구현·테스트·`.cursorrules` 기준 **현행 계약**은 `validate_lines` → `{ status, failed_lines }` 와 줄 ID **R1~R4, C1~C4, D1, D2** 이다.

---

## 1. 문제 정의 (Mom Test)

### 1.1 페르소나 *(가상 · 시뮬레이션)*

프로그래밍 수업(`자료구조`)에서 **4×4 부분 마방진(빈칸 2개)** 과제를 받은 2학년 학생. 손으로 빈칸을 채운 뒤 행·열·대각선 합 34를 검증하고, 이어서 ECB 분류 과제를 제출해야 하는 맥락.

### 1.2 진짜 문제 (한 문장)

부분 마방진을 다 맞췄다고 **확신**했지만, 검사해야 할 줄·대각선 중 **하나(부대각선)를 빠뜨린 채** 행·열만 반복 검증했고, 그 **잘못된 “완료” 판정** 위에서 **약 35분**을 허비한 뒤에야 누락을 알게 되었다.

### 1.3 Mom Test 증거 3줄

| # | 인용 | 제품 연결 |
|---|------|-----------|
| 1 | 「빈칸 두 개에 11이랑 6 넣었고, 네 줄 행이랑 네 줄 열은 손으로 더해서 전부 34 맞는 거 확인했어.」 | Green-T1 — 행·열만 34여도 대각선 미확인 시 **완료 착각** 방지 |
| 2 | 「그다음부터 행·열만 다시 더하고 빈칸 값을 바꿔 봤는데, **35분 정도** 그렇게만 돌았어.」 | fail 시 **어느 줄**인지 반환 — 행·열만 무한 반복 차단 |
| 3 | 「**부대각선**은 아예 안 더했어. 부대각선 더하니까 38이 나와서 …」 | Red-T1 — **D2** sum=38 → `failed_lines`에 `"D2"` |

### 1.4 표면 문제 (In Scope 아님)

| # | 하지 않을 것 |
|---|--------------|
| 1 | ECB 구조 **전체** 마방진 검증·솔버 프로그램 |
| 2 | GridUI · MissingFinder · **마방진 앱** UI |
| 3 | 빈칸 **자동 탐색·솔버** |
| 4 | 1~16 **중복·누락·범위** 전체 검증기 *(후속 FR)* |
| 5 | Hook · MCP *(세션 4 이전 제외)* |

---

## 2. 주제 · R-G-I-O

### 2.1 주제 (한 문장)

> **4×4 부분 마방진에서 “다 맞췄다”고 착각하기 전에, 행·열·대각선 **10개 줄**의 합 34 여부를 빠짐없이 판정한다.**

### 2.2 R-G-I-O

| | 내용 |
|---|------|
| **Role** | 부분 마방진을 손·코드로 채운 **학습자** — 검증 누락으로 시간을 쓰지 않으려는 사람 |
| **Goal** | 격자가 **10선**(행 4 + 열 4 + 대각선 2) 모두 합 34인지 **한 번에 판정**하고, 틀린 줄 **ID**를 알아낸다 |
| **Input** | 4×4 정수 격자 `list[list[int]]` — 빈칸 `0`, 채워진 칸 `1~16` |
| **Output** | `{ "status": "pass"\|"fail"\|"incomplete", "failed_lines": string[] }` |

---

## 3. 성공 기준 (SC1~SC3)

| # | 성공 기준 | Mom Test | 판정 방법 *(현행 계약)* |
|---|-----------|----------|-------------------------|
| **SC1** | **10선** 모두 검사 — **D2(부대각선)** 포함, 생략 없음 | 증거 3 | `validate_lines`가 내부적으로 R1~R4·C1~C4·D1·D2 **전부** 합산. Green-T1에서 `status == "pass"` |
| **SC2** | 합 ≠ 34인 **줄 ID** 반환 — 행·열만 반복 루프 방지 | 증거 2 | Red-T1: `status == "fail"`, `"D2" in failed_lines` *(D2 sum = 38)* |
| **SC3** | 10선 모두 pass일 때만 “완료” | 증거 1 | Green-T1: `status == "pass"`, `failed_lines == []` |

---

## 4. Entity (도메인)

### 4.1 격자

| 항목 | 규칙 |
|------|------|
| 크기 | 4×4 |
| 빈칸 | `0` |
| 채워진 칸 | `1`~`16` *(중복·누락 검증은 v0.2 범위 밖)* |
| 마법상수 | **34** — 각 줄 sum == 34일 때만 해당 줄 pass |

### 4.2 10선 ID

| 유형 | ID | 설명 |
|------|-----|------|
| 행 | R1, R2, R3, R4 | 1~4행 |
| 열 | C1, C2, C3, C4 | 1~4열 |
| 대각선 | D1 | 주대각선 ↘ |
| 대각선 | D2 | 부대각선 ↙ *(Mom Test 누락 항목)* |

### 4.3 Rule

```
RULE-VAL-01: 10선 각각 sum == 34 → 해당 줄 pass.
RULE-VAL-02: 10선 중 하나라도 fail → 전체 "완료" 판정 금지 (status: fail).
RULE-VAL-03: fail 시 failed_lines에 줄 ID를 반드시 포함한다.
RULE-VAL-04: 격자에 0(빈칸)이 남아 있으면 합 검증 전 incomplete 판정.
```

---

## 5. Control — `validate_lines`

### 5.1 FR-VAL-01 — 10선 검증 Command

| 항목 | 내용 |
|------|------|
| **파일** | `src/validate_lines.py` |
| **함수** | `validate_lines(grid: list[list[int]]) -> ValidateResult` |
| **공개 API** | **`validate_lines` 하나만** 노출 |

### 5.2 처리 순서

1. 격자 형식·크기(4×4) 확인
2. `0`(빈칸) 존재 여부 → 있으면 `incomplete` 반환
3. R1~R4, C1~C4, D1, D2 각 줄 합 계산
4. 줄별 pass/fail 판정 후 전체 `status` 결정

### 5.3 출력 스키마

```python
class ValidateResult(TypedDict):
    status: Literal["pass", "fail", "incomplete"]
    failed_lines: list[str]  # sum ≠ 34인 줄 ID (incomplete 시 [])
```

| status | 조건 | failed_lines |
|--------|------|--------------|
| `pass` | 10선 모두 sum == 34 | `[]` |
| `fail` | 빈칸 없음, 하나 이상 sum ≠ 34 | 해당 줄 ID 목록 *(예: `["D2"]`)* |
| `incomplete` | `0` 포함 | `[]` |

### 5.4 상수

| 이름 | 값 |
|------|-----|
| `MAGIC_CONSTANT` | 34 |
| `LINE_IDS` | R1, R2, R3, R4, C1, C2, C3, C4, D1, D2 |

---

## 6. Boundary (API · 테스트)

### 6.1 테스트 위치

- `tests/test_validate_lines.py`
- *(선택)* Golden: `tests/golden/*.json` — `/golden-master` PASS 후

### 6.2 Test Loop

| Case ID | 격자 상수 | Arrange 의도 | Assert |
|---------|-----------|--------------|--------|
| **Red-T1** | `RED_T1_GRID` | D2 sum = **38** *(Green-T1과 [3][0]만 8↔4 차이)* | `status == "fail"`, `"D2" in failed_lines` |
| **Green-T1** | `GREEN_T1_GRID` | 10선 모두 sum = 34 | `status == "pass"`, `failed_lines == []` |
| **Red-T2** | `RED_T2_GRID` | [2][2] = 0 빈칸 | `status == "incomplete"`, `failed_lines == []` |

#### Red-T1 격자

```text
16  3  2 13
 5 10 11  8
 9  6  7 12
 8 15 14  1   ← D2 = 38
```

#### Green-T1 격자

```text
16  3  2 13
 5 10 11  8
 9  6  7 12
 4 15 14  1   ← 10선 모두 34
```

#### Red-T2 격자

```text
16  3  2 13
 5 10 11  8
 9  6  0 12   ← 빈칸
 4 15 14  1
```

### 6.3 Golden Master 형식

```json
{
  "case_id": "Red-T1",
  "grid": [[16, 3, 2, 13], ...],
  "expected": { "status": "fail", "failed_lines": ["D2"] }
}
```

- **생성 조건**: `python -m pytest` **전부 PASS** 후 `/golden-master`
- FAIL 상태에서 golden 생성 **금지**

### 6.4 pytest

```bash
python -m pytest tests/test_validate_lines.py -v
```

- `pyproject.toml`: `testpaths = ["tests"]`, `pythonpath = ["."]`
- dev 의존: `pytest>=8.0`

---

## 7. TDD · ARRR

### 7.1 TDD 규칙

| Phase | 수정 범위 | 규칙 |
|-------|-----------|------|
| **RED** | `tests/` only | 실패 테스트 1케이스 추가 |
| **GREEN** | `src/` only | 최소 구현으로 통과 |
| **REFACTOR** | `src/` only | 동작·계약·Golden 불변 |

**금지**: assert 완화, `@pytest.mark.skip`, `xfail`, 한 사이클에 RED 2케이스 이상.

### 7.2 ARRR ↔ Cursor Command

| ARRR | 활동 | Command | Phase 선언 |
|------|------|---------|------------|
| **A — Ask** | RED 설계 | `/red-test-plan` | `Phase: RED (Ask)` |
| **A — Ask** | RED 스켈레톤 | `/red-skeleton` | `Phase: RED` |
| **R — Respond** | GREEN | `/green-minimal` | `Phase: GREEN` |
| **R — Respond** | Golden | `/golden-master` | `Phase: GOLDEN` |
| **R — Refine** | 스멜 탐지 | `/refactor-smell` | `Phase: REFACTOR (Ask)` |
| **R — Refine** | 안전 리팩터 | `/refactor-safe` | `Phase: REFACTOR` |
| **R — Repeat** | Export | `/export-session` | `Phase: EXPORT` |

**권장 1사이클**

```
/red-test-plan → /red-skeleton → /green-minimal → /golden-master
→ /refactor-smell → /refactor-safe → /export-session
```

- Command는 **슬래시명만**으로 SSOT·코드 상태를 읽고 자동 진행 *(추가 질문 금지)*
- 레거시: `/tdd-red` ≈ `/red-skeleton`

### 7.3 REFACTOR Budget *(1 invocation)*

| 항목 | 한도 |
|------|------|
| 수정 파일 | ≤ 3 |
| 신규 클래스 | ≤ 1 |
| 신규·추출 함수 | ≤ 3 |
| `validate_lines` 시그니처·반환 스키마 | **불변** |

---

## 8. Cursor 8계층 · 세션 로드맵

| 계층 | 세션 1~3 | 세션 4+ | 산출물 |
|------|----------|---------|--------|
| Mom Test | ✅ STEP 1 | — | `Report/01.REPORT.md` |
| Rule | ✅ | — | RULE-VAL-01~04 |
| Command | ✅ | ARRR Commands | `validate_lines`, `.cursor/commands/*.md` |
| Skill | △ | ✅ | `magic-square-tdd`, `magic-square-docs` |
| Test Loop | ✅ | ✅ Golden | `tests/`, `tests/golden/` |
| Hook | ❌ | 후속 | — |
| MCP | ❌ | 후속 | — |
| ARRR | ❌→✅ | ✅ | Command 체인 |
| Entity FR 전체 | △ | 후속 | v0.2 = FR-VAL-01만 |

| 세션 | 단계 | 상태 |
|------|------|------|
| STEP 1 | Mom Test 인터뷰 | ✅ [Report/01](../Report/01.REPORT.md) |
| STEP 2 | 세션 3 워크북 (R-G-I-O·SC) | ✅ [Report/03](../Report/03.REPORT.md) |
| STEP 3 | 계약 리뷰 | ✅ [Report/04](../Report/04.REPORT.md) |
| STEP 4 | ARRR TDD · Harness | ⏳ Command·Skill 배치 완료, GREEN·Golden·REFACTOR 진행 |

---

## 9. 프로젝트 구조

```
magic-square-00/
├── docs/
│   └── PRD.md                 ← 본 문서 (SSOT)
├── .cursorrules               ← Entity · Control · Boundary · TDD
├── .cursor/
│   ├── commands/              ← ARRR 슬래시 Command
│   └── skills/
│       ├── magic-square-tdd/
│       └── magic-square-docs/
├── src/
│   └── validate_lines.py      ← FR-VAL-01
├── tests/
│   ├── test_validate_lines.py
│   └── golden/                ← (선택) Golden Master
├── Report/                    ← NN.REPORT.md
└── Prompting/                 ← NN.Export-Transcript.md
```

---

## 10. AI · 협업 규칙

- 사용자와 **한국어** 소통
- TDD·ARRR 작업 시 응답 **첫 줄**에 Phase 선언
- **git commit** — 사용자 명시 요청 시만
- 범위 밖(솔버, ECB 전체, UI, Hook/MCP) 제안·구현 금지
- Export: `Report/NN.REPORT.md` ↔ `Prompting/NN.Export-Transcript.md` 동일 NN·상호 링크

---

## 11. 후속 FR *(v0.3+ 예정)*

| ID | 요약 | 비고 |
|----|------|------|
| FR-VAL-02 | 1~16 중복·누락·범위 검증 | Report/03 §4 #4 |
| FR-SOL-01 | 빈칸 자동 탐색·솔버 | In Scope 아님 |
| FR-UI-01 | GridUI · 검증 앱 | In Scope 아님 |
| FR-ECB-01 | ECB 분류 전체 | In Scope 아님 |

---

## 12. 참조 문서

| 문서 | 역할 |
|------|------|
| [docs/PRD.md](./PRD.md) | 요구사항·FR·Test Loop SSOT |
| [.cursorrules](../.cursorrules) | Agent Entity/Control/Boundary/TDD |
| [Report/01.REPORT.md](../Report/01.REPORT.md) | Mom Test 원본 |
| [Report/03.REPORT.md](../Report/03.REPORT.md) | 세션 3 워크북 *(초안 ID·스키마는 §본문 주석 참고)* |
| [Report/04.REPORT.md](../Report/04.REPORT.md) | 워크북↔계약 갭 리뷰 |
| `.cursor/commands/*.md` | ARRR 절차 |
| `.cursor/skills/magic-square-*/SKILL.md` | TDD·문서 Skill |

---

*PRD v0.2 — magic-square-00 validate_lines (세션 3~4 ARRR). Mom Test [Report/01](../Report/01.REPORT.md) 기반.*
