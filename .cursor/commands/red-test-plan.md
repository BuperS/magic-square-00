# /red-test-plan — RED ③ 설계 (ARRR Ask)

`validate_lines` TDD 사이클의 **RED 설계** 전용. 테스트 **코드는 작성하지 않고** 다음 RED 케이스 1개의 설계표만 만든다.

**추가 입력·질문 금지** — 슬래시명만으로 SSOT·현재 `tests/` 상태를 읽고 다음 케이스를 **자동 선정**한다.

---

## Phase 선언 (필수)

- **응답 첫 줄**: `Phase: RED (Ask)`
- **한국어**로 보고한다.
- 이 Phase에서는 **파일을 수정하지 않는다** (설계표 출력만).

---

## SSOT (읽기 순서)

1. `.cursorrules` — Entity · Control · Boundary · TDD
2. `docs/PRD.md` — 있으면 FR·Test Loop 우선 *(없으면 `.cursorrules` + `Report/03.REPORT.md` §5)*
3. `tests/test_validate_lines.py` — 이미 구현된 테스트 함수·격자 상수
4. `Report/01.REPORT.md` · `Report/03.REPORT.md` — Mom Test 증거·성공 기준

---

## 대상

| 항목 | 내용 |
|------|------|
| API | `validate_lines(grid) -> {status, failed_lines}` |
| 도메인 | 4×4, 빈칸 `0`, 채워진 칸 `1~16`, 마법상수 `34` |
| 10선 ID | R1~R4, C1~C4, D1(주대각), D2(부대각) |
| Mom Test | 부대각선(D2) 누락 → 35분 허비 *(증거 2·3)* |

---

## 자동 선정 규칙 (질문 금지)

1. `tests/test_validate_lines.py`에서 `test_*` 함수·격자 상수를 스캔한다.
2. 아래 **Boundary 우선순위**에서 **아직 없는** 첫 케이스 1개를 고른다.

| 우선 | Case ID | 조건 | Mom Test |
|------|---------|------|----------|
| 1 | **Red-T1** | D2 sum ≠ 34 → `status: fail`, `"D2" ∈ failed_lines` | 증거 3 — 부대각선 38 |
| 2 | **Green-T1** | 10선 모두 34 → `status: pass`, `failed_lines: []` | 증거 1 — 행·열만 34 착각 방지 |
| 3 | **Red-T2** | 0(빈칸) 포함 → `status: incomplete` | incomplete 분기 |

3. **1~3 모두 존재**하면 → REFACTOR 또는 다음 FR(`docs/PRD.md`) 후보를 표에 명시하고 RED 설계는 **「사이클 완료 — `/refactor-smell` 또는 Export 권장」**으로 보고한다.
4. 사용자에게 케이스 선택·확인 **요청하지 않는다**.

---

## 설계표 작성 절차

1. SSOT·테스트 파일을 읽고 Case ID를 확정한다.
2. 아래 **설계표 템플릿**을 **실제 값**으로 채운다 (빈 칸·TODO 금지).
3. AAA(Arrange · Act · Assert)를 **문장**으로 적되, 코드는 **작성하지 않는다**.
4. `/red-skeleton`에서 바로 옮길 수 있도록 격자·assert 기대값을 구체적으로 적는다.
5. 아래 **보고 형식**으로 출력한다.

### 설계표 필드

| 필드 | 내용 |
|------|------|
| Case ID | Red-T1 / Green-T1 / Red-T2 / … |
| Mom Test | `Report/01` 증거 번호·한 줄 연결 |
| Arrange | 4×4 `GRID` 이름·값 의도 (실패 줄·sum 명시) |
| Act | `result = validate_lines(GRID)` |
| Assert | `status`, `failed_lines` 기대 (모호한 표현 금지) |
| pytest 예상 | FAIL *(구현 전)* / PASS *(이미 GREEN)* |
| 다음 Command | `/red-skeleton` |

---

## 보고 형식

```markdown
Phase: RED (Ask)

## 선정 Case
- **Case ID**: <Red-T1|Green-T1|Red-T2|…>
- **근거**: <Boundary 우선순위 N · Mom Test 증거>

## RED 설계표

| 필드 | 내용 |
|------|------|
| Case ID | … |
| Mom Test | … |
| Arrange | … |
| Act | validate_lines(…) |
| Assert | status=…, failed_lines=… |
| pytest 예상 | FAIL (의도) |

## 격자 초안 *(스켈레톤용)*

<4×4 배열 — 주석에 실패 줄·sum>

## 기존 테스트 현황
- 존재: <test_* 목록>
- 이번 설계: <신규|재확인>

## 다음 단계
- `/red-skeleton` — 위 설계표대로 tests/에 실패 테스트 1개 추가
```

---

## 금지

| 금지 | 이유 |
|------|------|
| `tests/` · `src/` **파일 수정** | Ask = 설계만 |
| 한 번에 **2개 이상** Case 설계 | 한 사이클 = 케이스 1개 |
| 사용자에게 Case·격자 **질문** | 슬래시 단독 실행 |
| assert **완화**·skip·xfail **제안** | TDD 우회 |
| 솔버·UI·ECB·Hook/MCP | 세션 범위 밖 |

---

## 참조

- TDD RED 구현: `/red-skeleton`, `/tdd-red`
- GREEN: `/green-minimal`
- 도메인·API: `.cursorrules`
- Export: `.cursor/commands/export-session.md` *(워크스페이스)*
