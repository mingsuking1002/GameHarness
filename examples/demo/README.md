# 주사위 이동 회귀 검증 데모

Python 3.10 이상으로 GameHarness 루트에서 실행한다. 데모는 아수라판의 주사위 이동과 돌발 카드 구분을 보여주기 위해 만든 작은 예제다.

~~~powershell
python run.py --project examples/demo doctor
python run.py --project examples/demo check repro-before
python run.py --project examples/demo impact movement
python run.py --project examples/demo verify movement
python run.py --project examples/demo record --title "주사위 12 회귀" --summary "주사위와 돌발 카드 이동을 따로 기록한다" --repro "24번 칸에서 12가 나오면 수정 전 13걸음, 기대값은 12걸음" --evidence "movement 및 replay 검사 통과" --next "없음"
python run.py --project examples/demo check wiki
~~~

두 번째 명령은 의도적으로 실패한다. 해당 결과 폴더의 run.log에 12걸음이 기대됐고 13걸음이 관찰됐다고 표시한다. verify에서는 수정된 이동과 기존 리플레이를 모두 확인한다. 위키 검사 결과 폴더의 wiki.html에서 기록과 인수인계를 확인할 수 있다. record는 history.md를 갱신한다.
