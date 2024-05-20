from llmware.models import ModelCatalog
import sys
import json

# Load the model
model = ModelCatalog().load_model(
    selected_model="slim-boolean-tool", sample=False, temperature=0.0, max_output=200
)

# Read the research paper text
with open("../media/paper.txt", "r") as file:
    script = file.read()

# Ensure a question is provided
if len(sys.argv) > 1:
    question = sys.argv[1] + " (explain)"
else:
    raise ValueError("No question provided as a command line argument.")

# Call the model function
response = model.function_call(script, function="boolean", params=[question])
# analysis is loaded but not used in this snippet
# analysis = ModelCatalog().get_fx_scores(response, model.hf_tokenizer_name)

# Extract the answer and explanation from the response
llm_response = response["llm_response"]
answer = llm_response["answer"][0]
explanation = llm_response["explanation"][0]

# Create a single response object
response_object = {"question": question, "answer": answer, "explanation": explanation}

# Print the JSON response
print(json.dumps(response_object, indent=2))
