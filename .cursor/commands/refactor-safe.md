# /refactor-safe — REFACTOR ⑧ 안전 리팩터 (ARRR Refine)

`src/validate_lines.py`를 **동작·계약·Golden 불변**으로 유지하며 **P0 스멜 1건**만 리팩터한다.

**추가 입력·질문 금지** — `/refactor-smell` To-Do #1 *(없으면 src/ 자동 스캔 P0 1건)* 을 **자동 실행**한다.

---

## Phase 선언 (필수)

- **응답 첫 줄**: `Phase: REFACTOR`
- **한국어**로 보고한다.
- 이 Phase에서는 `src/`**만** 수정한다. `tests/` assert·Golden **변경 금지**.

---

## SSOT (읽기 순서)

1. `.cursorrules` — Entity · Control · 출력 계약
2. `docs/PRD.md` *(없으면 `.cursorrules`)*
3. 채팅 직전 `/refactor-smell` REFACTOR To-Do #1 *(있으면 그대로 실행)*
4. `src/validate_lines.py` · `tests/golden/*.json`

---

## 전제 (자동 — FAIL이면 중단)

1. `python -m pytest tests/test_validate_lines.py -v` 실행.
2. **FAILED > 0** → **코드 수정 없이** 중단:

```markdown
Phase: REFACTOR

## 중단 — pytest FAIL
- failed: N건
- 조치: `/green-minimal` 후 재실행
```

3. **전부 PASS**일 때만 리팩터 진행.

---

## Budget *(1 invocation — 초과 금지)*

| 항목 | 한도 |
|------|------|
| 수정 파일 | ≤ **3** |
| 신규 클래스 | ≤ **1** |
| 신규·추출 함수/메서드 | ≤ **3** |
| `validate_lines` 시그니처 | **불변** |
| 반환 `{status, failed_lines}` | **불변** |
| `tests/` · `tests/golden/` | **수정 금지** |

---

## 자동 작업 선정 (질문 금지)

1. 직전 `/refactor-smell` To-Do **#1** *(P0)* 실행.
2. To-Do 없으면 `src/validate_lines.py`에서 **S1 중복 합 계산** 등 P0 1건 자동 선택.
3. **Extract Function** 1회가 기본 패턴 *(예: `_sum_row`, `_collect_failed_line_ids`)*.
4. 리팩터 후 **즉시 pytest** — FAIL이면 **롤백**하고 원인 보고.

---

## REFACTOR 절차

1. pytest PASS 확인.
2. P0 작업 1건 적용 *(Behavior Preserving)*.
3. `python -m pytest tests/test_validate_lines.py -v` — **전부 PASS** 필수.
4. *(있으면)* golden harness test도 PASS.
5. 아래 **보고 형식** 출력.

### 허용 예

- private `_helper(grid) -> ...` 추출
- `LINE_IDS`·`MAGIC_CONSTANT` 일원화
- 중복 sum 루프 → 단일 순회

### 금지 예

- `validate_lines` 반환 키·값 의미 변경
- fail 줄 ID 명명 변경 (R1~D2)
- incomplete/fail/pass 분기 순서 변경으로 동작 변화
- 테스트·golden을 리팩터에 맞게 **수정**

---

## 보고 형식

```markdown
Phase: REFACTOR

## 적용 작업 *(P0 · 1건)*
- <Extract / Rename / … — 한 줄>

## src/ 변경
- `src/validate_lines.py` — <요약>
- Budget: 파일 N/3 · 함수 N/3 · 클래스 N/1

## pytest 결과
- collected: N · passed: N · failed: 0 ✅

## 잔여 To-Do
- <다음 P0/P1 한 줄>

## 다음 단계
- `/refactor-smell` — 잔여 스멜 재평가
- 또는 `/export-session`
```

---

## 금지

| 금지 | 이유 |
|------|------|
| pytest **FAIL** 상태에서 src/ 수정 | 안전 REFACTOR 아님 |
| Budget **초과** *(1 invocation에 P0 여러 건)* | `/refactor-safe` 1회 = 1건 |
| `tests/` · golden **수정** | 계약 고정 |
| 공개 API·동작 **변경** | Boundary |
| assert 완화·skip | 우회 |
| git commit *(사용자 요청 없이)* | `.cursorrules` |
| 솔버·UI·ECB·Hook/MCP | 범위 밖 |

---

## 참조

- 스멜 탐지: `/refactor-smell`
- Golden: `/golden-master`
- `.cursorrules`
