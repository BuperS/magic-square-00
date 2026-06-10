---
name: magic-square-docs
description: >-
  magic-square-00 세션 Report·Transcript·10선 검증 Checklist 문서를
  export-session 규칙과 동일 NN·상호 링크 형식으로 생성한다. /export-session,
  Report, Transcript, Export, ARRR Repeat, Mom Test, checklist, 10선 검증
  문서화 시 사용.
---

# magic-square-docs — Report · Transcript · Checklist

## SSOT

| 문서 | 역할 |
|------|------|
| `.cursor/commands/export-session.md` | Export 절차·금지·보고 형식 *(워크스페이스)* |
| `.cursorrules` | 프로젝트·TDD·Phase 규칙 |
| `docs/PRD.md` | FR · 세션 단계 *(없으면 Report/03)* |

템플릿: 이 Skill 디렉터리 `templates/` — **실제 내용으로 채울 것**, TODO·빈 칸 금지.

---

## Phase 선언

- Export: **`Phase: EXPORT`**
- Checklist만: **`Phase: DOCS`**
- **한국어**

---

## Export — `/export-session` 위임

Report + Transcript 쌍 생성은 **`.cursor/commands/export-session.md`** 절차를 따른다.

### 핵심 규칙

| 규칙 | 내용 |
|------|------|
| NN | `Report/NN.REPORT.md` ↔ `Prompting/NN.Export-Transcript.md` **동일 2자리** |
| 순번 | 기존 max(NN)+1, 사용자 지정 시 그 NN |
| 링크 | Report ↔ Transcript 상호 링크 |
| 금지 | NN 불일치 · 기존 덮어쓰기 · 허구 Transcript · 임의 commit |

템플릿: [templates/REPORT.template.md](templates/REPORT.template.md), [templates/TRANSCRIPT.template.md](templates/TRANSCRIPT.template.md)

---

## ARRR Repeat Report 보강

TDD/ARRR 세션이면 Report **§3 TDD / Test Loop**에 Command 이력을 남긴다:

| Phase | Command | 상태 |
|-------|---------|------|
| Ask | `/red-test-plan` → `/red-skeleton` | ✅/⏳ |
| Respond | `/green-minimal` → `/golden-master` | ✅/⏳ |
| Refine | `/refactor-smell` → `/refactor-safe` | ✅/⏳ |

pytest 결과 블록 포함 *(해당 시)*.

---

## 10선 Checklist — `Report/CHECKLIST-NN.md`

Mom Test SC1 — **10줄 누락 방지** 습관용. 수동·Agent 검증 체크리스트.

### 생성 규칙

1. `Report/CHECKLIST-*.md` max(NN)+1 → `Report/CHECKLIST-NN.md`
2. 템플릿: [templates/CHECKLIST.template.md](templates/CHECKLIST.template.md)
3. 격자·세션 메타는 **실제 값**으로 채움
4. git commit — 사용자 명시 시만

### 10선 ID (`.cursorrules`)

R1, R2, R3, R4, C1, C2, C3, C4, D1, D2 — **하나도 생략 금지**

---

## 완료 보고 (Export)

```markdown
Phase: EXPORT

## 생성 파일
- `Report/NN.REPORT.md` — …
- `Prompting/NN.Export-Transcript.md` — …

## 순번
- NN = …

## 세션 요약
- …

## 링크
- Report ↔ Transcript 상호 링크 완료
```

---

## 금지

- `01.XXX` 형식 위반 (`report.md` 등)
- 채팅에 없는 대화 **허구**
- Report/Prompting/Checklist **외** 임의 파일
- orientation/ 참조·수정
