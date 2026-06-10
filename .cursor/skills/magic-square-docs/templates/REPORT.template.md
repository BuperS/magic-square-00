# magic-square-00 — <단계 제목>

| 항목 | 내용 |
|------|------|
| 프로젝트 | magic-square-00 |
| 단계 | <단계명 — 예: 세션 4 ARRR Ask RED> |
| 일자 | YYYY-MM-DD |
| Mom Test 근거 | [Report/01.REPORT.md](../../Report/01.REPORT.md) *(해당 시)* |
| 대응 Transcript | [Prompting/NN.Export-Transcript.md](../../Prompting/NN.Export-Transcript.md) |

---

## 1. 요약

<이번 세션에서 한 일·달성한 것 2~4문장>

---

## 2. 산출물

| 파일 | 설명 |
|------|------|
| `<path>` | <역할> |

---

## 3. ARRR / TDD Loop *(해당 시)*

| ARRR | Command | 상태 | 비고 |
|------|---------|------|------|
| Ask | `/red-test-plan` | ✅/⏳ | <Case ID> |
| Ask | `/red-skeleton` | ✅/⏳ | <test_*> |
| Respond | `/green-minimal` | ✅/⏳ | — |
| Respond | `/golden-master` | ✅/⏳ | <golden 파일> |
| Refine | `/refactor-smell` | ✅/⏳ | P0~P2 N건 |
| Refine | `/refactor-safe` | ✅/⏳ | <적용 1건> |

**pytest 결과**

```
<python -m pytest -v 출력 요약>
```

---

## 4. 성공 기준 판정 *(해당 시)*

| # | 기준 | 결과 | 근거 |
|---|------|------|------|
| SC1 | 10선 검사 (D2 포함) | ✅/⏳ | … |
| SC2 | fail 줄 ID 반환 | ✅/⏳ | Red-T1 |
| SC3 | 10선 pass → 완료 | ✅/⏳ | Green-T1 |

---

## 5. 미완 / 다음 세션

- <항목>

---

*본 문서는 `Report/NN.REPORT.md` — magic-square-00 <단계> 보고서입니다.*
