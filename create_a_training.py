import replicate

training = replicate.trainings.create(
  version="a16z-infra/llama-2-7b-chat:d24902e3fa9b698cc208b5e63136c4e26e828659a9f09827ca6ec5bb83014381",
  input={
    "train_data": "https://replicate.delivery/pbxt/JQCHG9rbM81pfOTQeK4cpj7RtX4Cz2pHVh7IuF3kb7TRntg7/data.jsonl", 
  },
  destination="elizabethsiegle/klaybot"
)

print(training)
"""
RESPONSE=$(curl -s -X POST -H "Authorization: Token $REPLICATE_API_TOKEN" https://dreambooth-api-experimental.replicate.com/v1/upload/data.jsonl)

curl -X PUT -H "Content-Type: application/jsonl" --upload-file data.jsonl "$(jq -r ".upload_url" <<< "$RESPONSE")"

SERVING_URL=$(jq -r ".serving_url" <<< $RESPONSE)
echo $SERVING_URL
"""