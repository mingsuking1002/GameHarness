# 여러 게임의 개발 하네스

게임 기능을 고칠 때 변경이 영향을 주는 검사까지 실행하고, 다음 작업자가 같은 조건으로 결과를 재현할 수 있도록 기록한다. Codex와 Antigravity를 교대할 때 동일한 프로젝트 설정과 검증 명령을 사용한다.

**포트폴리오 빠른 실행** · [주사위 12칸 오류 재현부터 위키 인수인계까지](examples/demo/README.md). Python 3.10 이상으로 실행할 수 있다. Unity 설치가 필요한 실제 적용 사례는 아래에 설명한다.

첫 적용 프로젝트는 ModooMarbleUnity다. [프로젝트 교대 절차](ANTIGRAVITY.md)에는 작업 상태와 검사 결과를 넘기는 방법을 기록한다. 게임 루트의 hooks.json은 각 클라이언트에서 인수인계 문서를 안내한다. Unity 설치 경로는 VerifySource.ps1과 검사용 컴파일 인자 파일에서 확인한다.

각 게임 폴더를 독립된 작업공간으로 연다. 작업 카드와 검증 결과는 기능 단위로 기록하고 교대할 때 같은 프로젝트에서 읽는다.

프로젝트 루트에서 `python ../GameHarness/run.py status`, `doctor`, `check 검사명`을 사용한다. 중첩된 프로젝트는 이 파일 옆 run.py의 경로와 `--project 게임폴더`를 지정한다. doctor는 등록된 파일과 도구의 존재를 확인한다. check는 프로젝트가 등록한 명령을 실행하고 매번 새 결과 폴더에 실행 명령, 시간, 종료 상태, 로그를 남긴다.

새 게임 연결 시 harness.json에 requiredFiles, tools, reports, checks를 정의한다. checks의 각 항목은 command 인자 배열과 선택적인 timeout(초), identify(해시를 기록할 파일), result(결과 폴더 아래 status 필드가 있는 JSON)로 구성한다. {out}은 이번 결과 경로다. 아수라판의 harness.json을 예제로 삼고 해당 게임의 실제 검사만 등록한다. 기존 AGENTS.md에는 게임별 절차를 병합한다. 조사 프로젝트는 기록만 사용해도 된다.

## 위키 작업 기록

### 코딩 작업과 회귀 검증

1. 버그라면 빌드·시드·초기 상태·입력·실제 결과·기대 결과를 적고, 가능한 경우 수정 전에 테스트의 실패를 확인한다.
2. `python ../GameHarness/run.py impact 기능명`으로 변경 기능에 의존하는 기능을 확인한다. 실제 코드 호출부, 공유 상태, 저장·온라인 소비자를 읽은 후 빠진 의존성과 검사 이름을 프로젝트의 harness.json에 추가한다.
3. `python ../GameHarness/run.py verify 기능명`으로 변경 기능과 영향을 받는 기능의 검사를 순서대로 실행한다. 같은 검사는 한 번 실행하며 실패해도 다른 검사를 끝까지 실행한다. 실행마다 기존 report.json과 로그를 남긴다.
4. 위키에 재현 조건과 결과를 남길 때는 아래 `record` 명령에 `--repro "초기 상태, 입력, 관찰한 실패, 기대 결과"`를 붙인다. 검증하지 못한 항목은 evidence에 이유와 함께 적는다.

`features`는 프로젝트별 객체다. 각 기능은 등록된 `checks` 이름 배열과 선택적인 `dependsOn` 배열을 갖는다. 예를 들어 `replay`가 `movement`에 의존하면 movement를 수정할 때 replay 검사도 실행한다. 의존 관계는 실제 코드와 함께 관리한다. 아수라판은 Windows 실행 검사 전에 변경 소스를 빌드해야 한다.

[Python만 필요한 회귀 검증 예제](examples/demo/README.md)

### 빌드와 데이터 검사

프로젝트가 빌드 출처 파일을 만들면 harness.json에 `buildGuard`로 검사 스크립트, `buildIdentity`로 출처 파일을 등록한다. 실행 검사의 `requiresCurrentBuild`를 true로 두면 검사 전에 가드가 소스와 실행 산출물을 대조한다. 불일치 시 게임 실행 없이 `not_run`과 이유를 남긴다. 통과하면 실행 리포트에 출처 파일의 SHA-256도 기록한다.

아수라판에서 `check data`는 Steam 설정과 업적 등록 문서를 코드와 대조한다. `verify content`는 해당 데이터와 기존 게임 규칙을 검사한다. `verify replay-online`은 새 Windows 빌드의 저장 호환 검사와 소스의 모의 멀티플레이 검사를 실행한다.

각 게임의 harness.json에 `wikiHistory`로 게임 폴더 안의 Markdown 이력 파일을 지정한다. 파일의 첫 줄은 제목으로 둔다. 해당 게임의 작업자가 구현과 관련 검증을 마친 뒤 변경 이유, 결과나 증거 경로, 남은 일을 입력한다. 명령은 기존 이력을 보존하고 최신 항목을 맨 위에 추가한다.

```powershell
python ../GameHarness/run.py record --title "작업 제목" --summary "변경 내용과 이유" --evidence "통과한 검사와 결과 파일 경로, 미실행 항목" --next "다음 작업 또는 없음"
python ../GameHarness/run.py check wiki
```

교대 전에는 현재 담당과 다음 행동을 HANDOFF.md에 적는다. `check wiki`는 프로젝트가 등록한 위키 빌드·검증을 실행한다. 아수라판은 변경 이력과 인수인계를 공용 오프라인 HTML에 함께 반영한다. Git에는 각 게임의 원본 Markdown과 이미 추적 중인 검증 요약을 기록한다.

OpenAI의 [저장소 중심 개발 사례](https://openai.com/index/harness-engineering/)에서 짧은 안내와 실행 가능한 검사를, Anthropic의 [장기 작업 사례](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)에서 완료 조건과 교대 기록을 가져왔다. 교대할 때 반복해서 찾게 되는 정보와 놓친 결함을 근거로 규칙을 보완한다.
