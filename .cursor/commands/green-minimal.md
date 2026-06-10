# /green-minimal — GREEN ⑤ 최소 구현 (ARRR Respond)

`validate_lines` TDD 사이클의 **GREEN** 전용. `src/`에 **테스트를 통과시키는 최소 구현**만 추가한다.

**추가 입력·질문 금지** — pytest 실패 목록을 읽고 **첫 FAIL 1건**을 GREEN 대상으로 자동 처리한다.

---

## Phase 선언 (필수)

- **응답 첫 줄**: `Phase: GREEN`
- **한국어**로 보고한다.
- 이 Phase에서는 `src/`**만** 수정한다. `tests/`는 **assert·케이스 추가 없이** 그대로 둔다.

---

## SSOT (읽기 순서)

1. `.cursorrules` — Control 흐름 · 출력 계약
2. `docs/PRD.md` — FR·처리 순서 *(없으면 `.cursorrules`)*
3. `src/validate_lines.py` — 현재 구현·스텁
4. `tests/test_validate_lines.py` — 실패 중인 test·assert 기대값

---

## 자동 판단 (질문 금지)

1. `python -m pytest tests/test_validate_lines.py -v` 실행.
2. **FAILED**가 0이면 → **「이미 GREEN — `/golden-master` 또는 `/refactor-smell`」** 보고. `src/` **수정하지 않음**.
3. FAILED ≥ 1이면 → **가장 앞선(파일·라인 순) test 1개**만 통과시키는 최소 코드 작성.
4. YAGNI: 해당 test에 **필요한 분기만** 구현. 다른 RED 케이스를 **미리** 풀지 않는다 *(단, 기존 PASS regression 금지)*.

### Control 처리 순서 *(`.cursorrules`)*

1. 격자 형식·크기 4×4 확인
2. `0`(빈칸) 존재 → `incomplete`, `failed_lines: []`
3. R1~R4, C1~C4, D1, D2 합 계산
4. sum ≠ 34인 줄 ID → `failed_lines`; 전부 34 → `pass`

### 출력 계약

```python
{"status": "pass" | "fail" | "incomplete", "failed_lines": list[str]}
```

- `LINE_IDS`: R1, R2, R3, R4, C1, C2, C3, C4, D1, D2
- `MAGIC_CONSTANT`: 34

---

## GREEN 절차

1. pytest로 FAIL test 1개 식별.
2. `src/validate_lines.py`에 **최소** 로직 추가 *(내부 헬퍼 허용, Entity/Control 위반 금지)*.
3. `python -m pytest tests/test_validate_lines.py -v` 재실행.
4. 아래 **보고 형식**으로 결과 보고.

---

## 보고 형식

```markdown
Phase: GREEN

## 대상 테스트
- `test_<이름>` — <실패 원인 한 줄>

## src/ 변경
- `src/validate_lines.py` — <추가·수정 요약>

## pytest 결과
- 명령: `python -m pytest tests/test_validate_lines.py -v`
- collected: N
- passed: N
- failed: N
- 상태: <전부 PASS | 아직 FAIL N건 — 다음 `/green-minimal`>

## 다음 단계
- FAIL 잔여 → `/green-minimal` 반복
- 전부 PASS → `/golden-master` 또는 `/refactor-smell`
```

---

## 금지

| 금지 | 이유 |
|------|------|
| `tests/` **수정** *(assert 완화·skip 포함)* | GREEN = src/ 전용 |
| **과잉** 구현 *(현 FAIL 외 케이스 선행 처리)* | YAGNI |
| 기존 PASS test **깨뜨림** | Regression |
| `@pytest.mark.skip`, `xfail` | 우회 |
| 솔버·UI·ECB·Hook/MCP | 범위 밖 |
| git commit *(사용자 요청 없이)* | `.cursorrules` |

---

## 참조

- RED: `/red-skeleton`, `/red-test-plan`
- Golden: `/golden-master`
- REFACTOR: `/refactor-smell`
- `.cursorrules`
