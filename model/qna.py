from llmware.models import ModelCatalog
import sys
import json

print("Starting Python script execution...")

model = ModelCatalog().load_model(
    selected_model="slim-boolean-tool", sample=False, temperature=0.0, max_output=200
)

with open("../media/paper.txt", "r") as file:
    script = file.read()


if len(sys.argv) > 1:
    question = sys.argv[1] + " (explain)"
else:
    raise ValueError("No question provided as a command line argument.")

responses = []

response = model.function_call(script, function="boolean", params=[question])
analysis = ModelCatalog().get_fx_scores(response, model.hf_tokenizer_name)
responses.append(
    {
            "question": question,
            "llm_response": response["llm_response"],
    }
)
print(f"{response['llm_response']}")

json_responses = json.dumps(responses)
print(json_responses)
