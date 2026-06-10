# /refactor-smell — REFACTOR ⑦ 스멜 탐지 (ARRR Refine · Ask)

`src/validate_lines.py` **REFACTOR 전** 코드 스멜을 표로 정리한다. **코드는 수정하지 않는다.**

**추가 입력·질문 금지** — SSOT·`src/`·`tests/`를 읽고 스멜·우선순위를 **자동 도출**한다.

---

## Phase 선언 (필수)

- **응답 첫 줄**: `Phase: REFACTOR (Ask)`
- **한국어**로 보고한다.
- 이 Phase에서는 **파일을 수정하지 않는다** (스멜 표·To-Do만).

---

## SSOT (읽기 순서)

1. `.cursorrules` — Entity · Control · Boundary *(리팩터 후에도 계약 유지)*
2. `docs/PRD.md` — 구조·FR *(없으면 `.cursorrules`)*
3. `src/validate_lines.py`
4. `tests/test_validate_lines.py` · `tests/golden/*.json` *(있으면)*

---

## 전제 (자동 확인)

1. `python -m pytest tests/test_validate_lines.py -v` 실행.
2. **FAILED > 0** 이면:
   - 스멜 표만 **참고용 초안**으로 작성 가능하나, **`/refactor-safe` 진입 금지`** 명시.
   - 보고 첫 줄에 `⚠️ pytest FAIL — GREEN 선행 권장` 포함.

3. **전부 PASS**이면 REFACTOR Ask 정상 진행.

---

## 스멜 탐지 절차 (질문 금지)

1. `src/validate_lines.py` 전체를 읽는다.
2. 아래 **체크리스트**로 스멜 후보를 수집한다.
3. P0~P2로 우선순위를 매긴다.
4. `/refactor-safe` **Budget** 내 후보만 To-Do에 넣는다.

### 스멜 체크리스트

| ID | 스멜 | 신호 |
|----|------|------|
| S1 | **중복 합 계산** | 행·열·대각 sum 로직 반복 |
| S2 | **매직 넘버** | 34·4가 리터럴로 흩어짐 *(상수 미사용)* |
| S3 | **긴 함수** | `validate_lines` 한 함수에 전 단계 혼재 |
| S4 | **줄 ID 하드코딩** | R1~D2 문자열 반복 |
| S5 | **깊은 중첩** | if/for 3단 이상 |
| S6 | **TypedDict 미활용** | 반환 dict 수동 조립·키 오타 위험 |
| S7 | **테스트 없는 private API** | `_helper` 공개화·과다 분리 |

### 우선순위

| 등급 | 기준 | 예 |
|------|------|-----|
| **P0** | 중복·가독성·계약 위험 **낮음**, `/refactor-safe` 1회로 처리 | S1 `_line_sums` 추출 |
| **P1** | 구조 개선, Golden·테스트 불변 전제 | S3 단계별 함수 분리 |
| **P2** | 미미·취향 | 주석·이름 정리 |

### `/refactor-safe` Budget *(1 invocation)*

| 항목 | 한도 |
|------|------|
| 수정 파일 | **≤ 3** |
| 신규 클래스 | **≤ 1** |
| 신규·추출 함수/메서드 | **≤ 3** |
| 공개 API 변경 | **금지** (`validate_lines` 시그니처·반환 스키마) |
| Golden·Mom Test assert | **불변** |

---

## 보고 형식

```markdown
Phase: REFACTOR (Ask)

## pytest 전제
- passed: N / failed: N — <GREEN OK | FAIL ⚠️>

## 스멜 표

| P | ID | 위치 | 스멜 | `/refactor-safe` 후보 |
|---|-----|------|------|----------------------|
| P0 | S1 | validate_lines.py L… | … | ✅ `_…` 추출 |
| P1 | … | … | … | △ |
| P2 | … | … | … | — |

## REFACTOR To-Do *(Budget 순)*

1. [P0] <한 줄 작업>
2. [P1] …
3. [P2] …

## 다음 단계
- pytest PASS → `/refactor-safe` (To-Do #1만)
- pytest FAIL → `/green-minimal` 선행
```

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/` · `tests/` **수정** | Ask = 탐지만 |
| 공개 API·출력 스키마 **변경 제안** *(P0)* | Boundary |
| 한 번에 **Budget 초과** 작업 계획 | `/refactor-safe` 1회 = 1 변경 |
| 사용자 우선순위 **질문** | 슬래시 단독 실행 |
| 솔버·UI·ECB·Hook/MCP | 범위 밖 |

---

## 참조

- REFACTOR 실행: `/refactor-safe`
- Golden: `/golden-master`
- `.cursorrules`
