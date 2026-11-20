# 여러 게임의 개발 하네스

첫 적용 프로젝트는 ModooMarbleUnity다. [Antigravity 전달문](ANTIGRAVITY.md)을 복사해 인수인계를 시작한다. 두 클라이언트의 시작 훅은 이 PC의 프로젝트 절대 경로를 사용한다. 폴더를 옮기면 양쪽 hooks.json 경로를 갱신한다. Codex에서는 신뢰한 프로젝트에서 새 훅 정의를 /hooks로 검토한 뒤 자동 실행할 수 있다. 실제 Unity 설치 경로는 기존 VerifySource.ps1과 검사용 컴파일 인자 파일을 함께 확인한다.

각 게임 폴더를 독립된 작업공간으로 연다. 같은 PC의 Codex와 Antigravity는 해당 게임의 작업 카드와 검증 결과를 공유한다. 모델 한도에 닿기 전 기능 단위로 기록하고, 교대할 때 다음 도구에서 해당 폴더를 연다.

프로젝트 루트에서 `python ../GameHarness/run.py status`, `doctor`, `check 검사명`을 사용한다. 중첩된 프로젝트는 이 파일 옆 run.py의 경로와 `--project 게임폴더`를 지정한다. doctor는 등록된 파일과 도구의 존재를 확인한다. check는 프로젝트가 등록한 명령을 실행하고 매번 새 결과 폴더에 실행 명령, 시간, 종료 상태, 로그를 남긴다.

새 게임 연결 시 harness.json에 requiredFiles, tools, reports, checks를 정의한다. checks의 각 항목은 command 인자 배열과 선택적인 timeout(초), identify(해시를 기록할 파일), result(결과 폴더 아래 status 필드가 있는 JSON)로 구성한다. {out}은 이번 결과 경로다. 아수라판의 harness.json을 예제로 삼고 해당 게임의 실제 검사만 등록한다. 기존 AGENTS.md에는 게임별 절차를 병합한다. 조사 프로젝트는 기록만 사용해도 된다.

## 위키 작업 기록

각 게임의 harness.json에 `wikiHistory`로 게임 폴더 안의 Markdown 이력 파일을 지정한다. 파일의 첫 줄은 제목으로 둔다. 해당 게임의 작업자가 구현과 관련 검증을 마친 뒤 변경 이유, 결과나 증거 경로, 남은 일을 입력한다. 명령은 기존 이력을 보존하고 최신 항목을 맨 위에 추가한다.

```powershell
python ../GameHarness/run.py record --title "작업 제목" --summary "변경 내용과 이유" --evidence "통과한 검사와 결과 파일 경로, 미실행 항목" --next "다음 작업 또는 없음"
python ../GameHarness/run.py check wiki
```

교대 전에는 현재 담당과 다음 행동을 HANDOFF.md에 적는다. `check wiki`는 프로젝트가 등록한 위키 빌드·검증을 실행한다. 아수라판은 변경 이력과 인수인계를 공용 오프라인 HTML에 함께 반영한다. Git에는 각 게임의 원본 Markdown과 이미 추적 중인 검증 요약을 기록한다.

OpenAI의 [저장소 중심 개발 사례](https://openai.com/index/harness-engineering/)에서 짧은 안내와 실행 가능한 검사를, Anthropic의 [장기 작업 사례](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)에서 완료 조건과 교대 기록을 가져왔다. 교대할 때 반복해서 찾게 되는 정보와 놓친 결함을 근거로 규칙을 보완한다.
