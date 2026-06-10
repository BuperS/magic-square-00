# /golden-master — Golden ⑥ 승인 스냅샷 (ARRR Respond)

`validate_lines` **전 테스트 PASS**를 전제로, Mom Test Boundary 격자의 **Golden Master** 스냅샷을 기록한다.

**추가 입력·질문 금지** — pytest 결과·Boundary SSOT를 읽고 대상 Case·파일을 **자동 결정**한다.

---

## Phase 선언 (필수)

- **응답 첫 줄**: `Phase: GOLDEN`
- **한국어**로 보고한다.

---

## SSOT (읽기 순서)

1. `.cursorrules` — Boundary Red-T1 / Green-T1
2. `docs/PRD.md` — Golden 대상 Case *(없으면 Boundary 표)*
3. `tests/test_validate_lines.py` — 격자 상수명
4. `tests/golden/` — 기존 golden 파일 *(있으면)*

---

## PASS 전제 (필수)

1. `python -m pytest tests/test_validate_lines.py -v` 실행.
2. **FAILED > 0** 이면:
   - Golden 파일 **생성·수정하지 않는다**.
   - 아래만 보고하고 **종료**:

```markdown
Phase: GOLDEN

## 중단 — PASS 미충족
- pytest: failed N건
- 조치: `/green-minimal`로 GREEN 완료 후 재실행
```

3. **전부 PASS**일 때만 Golden 작업 진행.

---

## 자동 대상 선정 (질문 금지)

Boundary 격자마다 golden JSON 1개. **아직 없는** 첫 항목부터 생성:

| 우선 | Case | 격자 상수 | Golden 파일 |
|------|------|-----------|-------------|
| 1 | Red-T1 | `RED_T1_GRID` | `tests/golden/red_t1.json` |
| 2 | Green-T1 | `GREEN_T1_GRID` | `tests/golden/green_t1.json` |
| 3 | Red-T2 | `RED_T2_GRID` | `tests/golden/red_t2.json` |

- 해당 JSON이 **이미 존재**하고 내용이 현재 `validate_lines` 출력과 일치하면 → 다음 우선순위.
- **1~3 모두 존재·일치** → **「Golden complete — `/refactor-smell` 또는 `/export-session`」** 보고.

---

## Golden 형식

각 파일은 `validate_lines(GRID)` **실행 결과**를 그대로 담는다:

```json
{
  "case_id": "Red-T1",
  "grid": [[16, 3, 2, 13], ...],
  "expected": {
    "status": "fail",
    "failed_lines": ["D2"]
  }
}
```

- `expected`는 **실제 pytest PASS 시점**의 반환값과 동일해야 한다.
- `failed_lines` **순서**는 구현 의존 가능 — 테스트와 golden **일치**가 우선.

### Approval harness *(선택 · PASS 후)*

`tests/test_validate_lines.py`에 golden 대조 test **1개** 추가 가능:

```python
def test_golden_red_t1_matches_snapshot():
    import json
    from pathlib import Path
    golden = json.loads(Path("tests/golden/red_t1.json").read_text(encoding="utf-8"))
    result = validate_lines(golden["grid"])
    assert result == golden["expected"]
```

- harness 추가 시에도 **assert 완화·skip 금지**.
- 이번 invocation에서 golden **1 Case만** 처리.

---

## 절차

1. pytest PASS 확인 *(FAIL이면 중단)*.
2. 대상 Case 1개 확정.
3. `validate_lines`를 해당 격자에 실행해 `expected` 확정.
4. `tests/golden/<name>.json` 작성 *(디렉터리 없으면 생성)*.
5. *(선택)* 대응 harness test 1개 추가.
6. `python -m pytest tests/test_validate_lines.py -v` → **전부 PASS** 확인.
7. 보고.

---

## 보고 형식

```markdown
Phase: GOLDEN

## pytest 전제
- collected: N · passed: N · failed: 0 ✅

## Golden 생성·갱신
- `tests/golden/<file>.json` — <Case ID · status · failed_lines 요약>

## Approval harness
- <추가함: test_* | 없음>

## pytest 재확인
- collected: N · passed: N · failed: 0

## 다음 단계
- 잔여 Case golden → `/golden-master` 반복
- 완료 → `/refactor-smell` 또는 `/export-session`
```

---

## 금지

| 금지 | 이유 |
|------|------|
| pytest **FAIL** 상태에서 golden 생성 | 잘못된 SSOT |
| 한 번에 **2 Case 이상** golden | 1 invocation = 1 Case |
| `expected` **수동 조작** *(실행 결과와 불일치)* | Golden 신뢰성 |
| `src/` **동작 변경** *(golden 맞추기)* | GREEN/REFACTOR 침범 |
| assert 완화·skip·xfail | TDD 우회 |
| git commit *(사용자 요청 없이)* | `.cursorrules` |

---

## 참조

- GREEN: `/green-minimal`
- REFACTOR: `/refactor-smell`
- Export: `.cursor/commands/export-session.md`
- `.cursorrules`
