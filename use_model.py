import replicate
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])
def sms():
    resp = MessagingResponse()
    inb_msg = request.form['Body'].lower().strip()

    output = replicate.run(
    "elizabethsiegle/klaybot:a97cfcb4216622e04d714198b00adff9b1fe5d32cdce1e7ee8e6da7ae8ec35fc",
    input={"prompt": inb_msg}) #"max_new_tokens":200
    resp_msg = ''.join(list(output))
    print(resp_msg)
    resp.message(resp_msg)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

# The elizabethsiegle/klaybot model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
# for item in output:
#     # https://replicate.com/elizabethsiegle/klaybot/versions/609d065d29d0948c1678b49a3a78b5391f865d50f2c393336427330b5c853532/api#output-schema
#     print(item)