# /red-skeleton — RED ④ 스켈레톤 (ARRR Ask → Agent)

`validate_lines` TDD 사이클의 **RED 구현** 전용. `tests/`에 **실패하는 테스트 1개**를 AAA 스켈레톤으로 추가한다.

**추가 입력·질문 금지** — SSOT·`tests/` 상태를 읽고 다음 RED 케이스를 **자동 선정**해 바로 작성한다.  
직전에 `/red-test-plan` 설계표가 있으면 **그 Case ID를 우선** 따른다.

---

## Phase 선언 (필수)

- **응답 첫 줄**: `Phase: RED`
- **한국어**로 보고한다.
- 이 Phase에서는 `tests/`**만** 수정한다. `src/`는 **절대** 건드리지 않는다.

---

## SSOT (읽기 순서)

1. `.cursorrules` — Boundary · TDD RED 규칙
2. `docs/PRD.md` — Test Loop *(없으면 `.cursorrules`)*
3. `tests/test_validate_lines.py` — 기존 격자·함수
4. 채팅 직전 `/red-test-plan` 보고 *(있으면 Case ID·격자·Assert 재사용)*

---

## 자동 선정 (질문 금지)

`/red-test-plan`과 **동일 우선순위**:

| 우선 | Case ID | 핵심 Assert |
|------|---------|-------------|
| 1 | Red-T1 | `status == "fail"`, `"D2" in failed_lines` |
| 2 | Green-T1 | `status == "pass"`, `failed_lines == []` |
| 3 | Red-T2 | `status == "incomplete"`, `failed_lines == []` |

- 해당 `test_*`가 **이미 존재**하면 다음 우선순위로 넘긴다.
- 1~3 **모두 존재**하면: pytest만 실행하고 **「RED backlog 소진 — `/green-minimal` 또는 `/refactor-smell`」** 보고. **새 테스트 추가하지 않음.**

---

## RED 절차

1. Case ID 1개 확정.
2. `tests/test_validate_lines.py`에 **격자 상수 + test 함수 1개** 추가 *(또는 미완 스켈레톤 완성)*.
3. **AAA 주석**을 반드시 넣는다: `# Arrange`, `# Act`, `# Assert`.
4. `python -m pytest tests/test_validate_lines.py -v` 실행 → **의도적 FAIL** 확인.
5. 아래 **보고 형식**으로 결과를 보고한다.

### AAA 스켈레톤 규칙

| 단계 | 내용 |
|------|------|
| **Arrange** | `UPPER_SNAKE_GRID` 상수. 주석에 Case ID·실패 줄·sum |
| **Act** | `result = validate_lines(...)` **한 번** |
| **Assert** | `status`, `failed_lines` **구체적** 검증 |

### 격자 SSOT (Boundary)

```python
# Red-T1: D2(부대각선) sum == 38 — Mom Test 증거 3
RED_T1_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [8, 15, 14, 1],  # Green-T1과 [3][0]만 다름 → D2 fail
]

# Green-T1: 10선 모두 sum == 34
GREEN_T1_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# Red-T2: 빈칸(0) 포함 → incomplete
RED_T2_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]
```

---

## 보고 형식

```markdown
Phase: RED

## 추가·수정 테스트
- `test_<이름>` — <Case ID · 한 줄 설명>

## AAA 요약
- Arrange: <격자·의도>
- Act: validate_lines(grid)
- Assert: <status, failed_lines 기대>

## pytest 결과
- 명령: `python -m pytest tests/test_validate_lines.py -v`
- collected: N
- failed: N (의도됨) / passed: N
- 대표 실패: <AssertionError / TypeError / NotImplementedError 한 줄>

## 다음 단계
- `/green-minimal` — `src/validate_lines.py` 최소 구현
```

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/` **어떤 파일도** 수정 | RED = tests/ 전용 |
| assert **완화**, `@pytest.mark.skip`, `xfail` | 실패 숨김 |
| 한 번에 **2개 이상** test 추가 | 한 사이클 = 1케이스 |
| 구현 코드를 테스트에 **미리** 작성 | GREEN 침범 |
| 사용자 Case **질문** | 슬래시 단독 실행 |
| 솔버·UI·ECB·Hook/MCP | 범위 밖 |

---

## 참조

- RED 설계: `/red-test-plan`
- 레거시 RED: `/tdd-red`
- GREEN: `/green-minimal`
- `.cursorrules`
