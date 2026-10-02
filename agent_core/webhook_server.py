import argparse
import json
from flask import Flask, request

# 1. parser 를 만들고, --port 인자(정수, 기본값 5000)를 받고, args 에 parse_args() 결과를 담으세요
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=5000, help="열어 둘 포트 번호")
args = parser.parse_args()


app = Flask(__name__)
received = []


@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.get_json()
    received.append(event)
    with open("received_alerts.json", "w", encoding="utf-8") as f:
        json.dump(received, f, ensure_ascii=False, indent=2)
    if "rule" in event:
        print("[수신]", event["rule"])
    # 2. {"status": "ok", "count": received 의 길이} 와 200 을 return 하세요
    # [2번 빈칸] 상대방에게 "잘 받았어! 지금 총 몇 건 쌓였어"라고 답장 보내기
    return {"status": "ok", "count": len(received)}
    return 200




# 3. args 로 받은 포트로 app 을 실행하세요
# [3번 빈칸] 파일 안에 고정된 포트가 아니라, 위에서 사용자가 던져준 포트로 서버 열기!
app.run(port=args.port)
