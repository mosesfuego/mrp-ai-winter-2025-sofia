from openai import OpenAI
import os
import traceback
# NVIDIA NIM (OpenAI-compatible)
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("NIM_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)

AVAILABLE_PLANNERS = ["bfs", "dijkstra", "astar", "greedy"]

# ---------------------------
# SYSTEM PROMPT (STATIC)
# ---------------------------
SYSTEM_PROMPT = """
You are an AI system that selects a pathfinding algorithm.

Choose ONE from:
bfs, dijkstra, astar, greedy

Respond with ONLY the algorithm name.
Do not explain.
Do not think step by step.
Output immediately.
"""


def build_user_prompt(env_features):
    return f"""
Environment features:
{env_features}

Choose the best algorithm.
"""


def choose_planner_with_llm(env_features):

    try:
        response = client.chat.completions.create(
            model="moonshotai/kimi-k2.5",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": build_user_prompt(env_features)}
            ],
            max_tokens=200,   # slightly higher
            temperature=0
        )

        # ---------------------------
        # SAFE EXTRACTION
        # ---------------------------
        if not response or not response.choices:
            print("\n[LLM ERROR]: Empty response")
            return None

        message = response.choices[0].message

        if not message or not message.content:
            print("\n[LLM ERROR]: No content in response")
            print("[RAW RESPONSE]:", response)
            return None

        answer = message.content.strip().lower()
        answer = answer.replace("\n", " ").split()[0]

        if answer in AVAILABLE_PLANNERS:
            return answer

        print("\n[LLM WARNING]: Unexpected output:", answer)
        return None

    except Exception as e:
        import traceback
        traceback.print_exc()
        return None
