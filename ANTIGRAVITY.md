# 프로젝트 교대 절차

게임 폴더를 작업 루트로 열고 AGENTS.md와 HANDOFF.md에서 담당, 완료 조건, 최근 검사와 다음 행동을 확인한다.

프로젝트 루트에서 인수인계와 실행 환경을 확인한다.

~~~powershell
python ../GameHarness/run.py status
python ../GameHarness/run.py doctor
~~~

버그는 수정 전 시드, 입력, 실제 결과, 기대 결과를 고정해서 재현한다. `impact 기능명`으로 영향 범위를 확인하고 호출부와 저장·온라인 상태를 대조한다. 새 관계는 harness.json의 features에 추가한다. 수정 뒤 `verify 기능명`으로 관련 기능을 검사한다. 실행 검사는 변경 사항이 포함된 빌드를 사용한다.

교대할 때 HANDOFF.md에 변경 파일, 결과 경로, 미확인 항목과 다음 행동을 기록한다. `record --repro`로 재현 조건과 증거를 이력에 추가하고 `check wiki`로 반영한다.
