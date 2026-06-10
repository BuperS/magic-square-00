# magic-square-00 — <단계> Transcript

| 항목 | 내용 |
|------|------|
| 프로젝트 | magic-square-00 |
| 단계 | <단계명> |
| 일자 | YYYY-MM-DD |
| Export | `Prompting/NN.Export-Transcript.md` |
| 대응 보고서 | [Report/NN.REPORT.md](../Report/NN.REPORT.md) |

---

## 세션 시작

**User**

```
<첫 사용자 요청 원문>
```

**Assistant**

<첫 응답 요약 — Phase 선언·파일 경로·pytest 결과 포함>

---

## Turn 2 … N

*(User 요청 + Assistant 응답을 Turn 단위로 반복)*

**User**

```
<원문>
```

**Assistant**

<요약 — Command(`/red-test-plan` 등)·코드·pytest 누락 없이>

---

## Export 확정

**User**

```
/export-session
```

**Assistant**

- `Report/NN.REPORT.md` — <한 줄 설명>
- `Prompting/NN.Export-Transcript.md` — 본 문서

---

*본 문서는 `Prompting/NN.Export-Transcript.md` — magic-square-00 <단계> 대화 Export입니다.*

**Transcript 규칙**

- User 발화 **원문** 코드블록 보존
- Assistant: 파일 경로·명령·pytest **누락 금지**
- ⚠️ [시뮬레이션] 세션이면 라벨 유지
- 채팅에 **없는 내용 지어내지 않음**
