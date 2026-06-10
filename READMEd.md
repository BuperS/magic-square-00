
**강의 자료**
https://github.com/kznetwork/CursorAI_basic
https://github.com/kznetwork/CursorAI
https://github.com/kznetwork/CusorAI
https://github.com/BuperS/magic-square-00

**사전 설문**
https://naver.me/GKIt8qzf

**팀빌딩**
https://naver.me/5t7rOpEX

github mcp server
https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-cursor.md

---

문서: test plan
코드: skeleton plan

RED 단계에서는 스켈레톤만 만든다. 구현 코드를 작성하지 않는다.

## 프롬프팅

- 페르소나
  - 역할을 부여해주면 더 좋은 결과를 냄
- 포맷
  - 출력형식을 지정해주기
- 프로젝트 맥락
  - AI Agent 에게 충분한 정보를 주기
  - AI Agent 친화적인 환경부터 구성


- 개념 - 방향성, 철학, 거시적인 도메인 경계, 
  - 경계를 나눌 줄 알아야 함
  - ECB 개념 모델, 역할 분류
  - BCE(Boundary Context Entity)
- 책임
- 검증
- 코드
  - 기존 UT 에 그쳤던 시험을 E2E 까지 확장할 수 있게 됨.

- PRD 시나리오쪽에 거킨 형식 시나리오를 씀

- Mom Test
  - AI Agent 에게 설문을 하는 방식
  - 내가 문제를 지적하지 말고, 얘한테 뭐가 문제인지를 말하게 하는것
  - 정답을 알려주지말고 얘가 추론하게 해서 패인포인트를 찾는 기법
  - AI 에게 패인포인트를 묻지 않는다. PRD 가 이상하게 나온다. 사람이 생각해낸 패인 포인트가 아니기 때문이다. 프롬프팅을 잘못하고 있는 것이다.
  - 내가 대답이 가능하도록, AI Agent 가 mom test 전문 인터뷰어로 페르소나를 설정하고 나에게 질문하게 한다.
  - 커서에게 묻지 않는다는 게 핵심이다.
  - 레가시코드는 커서가 더 패인포인트를 잘 찾는다. 그러나 신규 요구사항에 대해서는 내가 더 잘 알기 때문에 내가 패인포인트를 더 잘 찾을 수 있다. 질문의 방향이 서로 반대다. 패인포인트를 더 잘 찾을 줄 아는 대상에게 질문이 향한다.
  - 근데 걍 둘 다 하면 될듯

- 하나의 커밋 단위가 세션 단위
- mom test 는 3턴이 좋타고 함
- mom test 는 커맨드화 하는 게 좋음

- user research 를 mom test 기법으로 하는듯
