import json
from llmware.models import ModelCatalog

with open("../media/paper.txt", "r") as file:
    script = file.readlines()

model = ModelCatalog().load_model(
    selected_model="slim-summary-tool", sample=False, temperature=0.0, max_output=200
)

paragraphs = "".join(script).split("\n\n")

response_dict = {}

for i, paragraph in enumerate(paragraphs):
    response = model.function_call(
        paragraph, function="summarize", params=["summary points(5)"]
    )

    section = "Abstract" if i == 0 else "Discussion and Conclusion"

    response_dict[section] = response["llm_response"]

with open("../media/response.json", "w") as json_file:
    json.dump(response_dict, json_file)
