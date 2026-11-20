# Antigravity에 전달할 메시지

아수라판 Unity 프로젝트를 이어받아 줘. 작업 폴더는 C:\Users\ksh00\project\ModooMarbleUnity야. 먼저 AGENTS.md와 HANDOFF.md에서 담당, 완료 조건, 마지막 검사와 다음 행동을 확인해. 현재는 하네스 설치가 끝나서 교대 가능한 상태야.

프로젝트 루트에서 다음 두 명령으로 인수인계와 환경을 확인해.

~~~powershell
python ../GameHarness/run.py status
python ../GameHarness/run.py doctor
~~~

새 작업을 받으면 어떤 동작을 보면 완료인지 먼저 기록해. 소스 변경은 check source, 화면은 check front, 주사위는 check dice, 경기·로비 복귀는 check loop로 검증해. 실행 검사는 변경분이 들어간 빌드를 대상으로 해. 기능 하나가 끝나거나 교대하기 전에 변경 파일, 검사 결과 폴더, 미실행 항목, 다음 행동을 HANDOFF.md에 남겨 줘. 다른 사람이 작성 중인 같은 파일은 리뷰만 진행해.
