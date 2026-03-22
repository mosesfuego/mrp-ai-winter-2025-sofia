# 🚀 Adaptive Grid Navigation Agent (LLM + Classical Planning)

## 🧠 Overview

This project implements an intelligent **grid navigation agent** that combines:

- **Perception** (analyzing the environment)
- **Reasoning** (LLM-based decision making)
- **Planning** (classical search algorithms)
- **Action** (executing and visualizing a path)

The agent dynamically selects the most appropriate **pathfinding algorithm** using an LLM, while maintaining a **robust fallback system** to ensure reliability.

---

## ⚡ tl;dr

- Navigates a randomly generated grid with obstacles  
- Uses an LLM to choose between BFS, Dijkstra, A*, or Greedy search  
- Falls back to rule-based logic if the LLM fails  
- Visualizes the path with animation  

**Key idea:** Combine **LLM reasoning + deterministic algorithms** for robust AI systems.

---

## 🏗️ Architecture
# 🚀 Adaptive Grid Navigation Agent (LLM + Classical Planning)

## 🧠 Overview

This project implements an intelligent **grid navigation agent** that combines:

- **Perception** (analyzing the environment)
- **Reasoning** (LLM-based decision making)
- **Planning** (classical search algorithms)
- **Action** (executing and visualizing a path)

The agent dynamically selects the most appropriate **pathfinding algorithm** using an LLM, while maintaining a **robust fallback system** to ensure reliability.

---

## ⚡ tl;dr

- Navigates a randomly generated grid with obstacles  
- Uses an LLM to choose between BFS, Dijkstra, A*, or Greedy search  
- Falls back to rule-based logic if the LLM fails  
- Visualizes the path with animation  

**Key idea:** Combine **LLM reasoning + deterministic algorithms** for robust AI systems.

---

## 🏗️ Architecture
Environment (Grid + Obstacles)
↓
Perception (Feature Extraction)
↓
LLM Reasoning (Planner Selection)
↓
Fallback Rules (if LLM fails)
↓
Tool Calling (Search Algorithms)
↓
Execution + Visualization

---

## 🧩 Components

### 1. Perception
Extracts key features from the environment:
- Grid size  
- Obstacle density  
- Start-to-goal distance  

---

### 2. Reasoning (LLM)

Uses an LLM (via NVIDIA NIM + Kimi K2.5) to select the best planner:

- `bfs`
- `dijkstra`
- `astar`
- `greedy`

---

### 3. Planning (Tools)

Each search algorithm is implemented as an independent tool:

- Breadth-First Search (BFS)  
- Dijkstra’s Algorithm  
- A* Search  
- Greedy Best-First Search  

---

### 4. Tool Calling

The agent selects and calls tools rather than implementing logic internally.

**Design principle:**
- LLM = decision layer  
- Tools = execution layer  

---

### 5. Fallback Logic (Critical)

If the LLM:
- fails (API issues)
- returns invalid output
- runs out of tokens

The system falls back to deterministic rules.

This guarantees:The system always produces a valid result

---

## 🔒 Tool Restriction (Important)

The agent only has access to a limited set of tools:  [bfs, djikstra, astar, greedy]

Why this matters:
- Reduces hallucinations  
- Improves reliability  
- Prevents unsafe behavior  
- Enforces controlled decision-making  

---

## 🎯 Features

- Randomized grid environments  
- Adaptive planner selection  
- Hybrid LLM + rule-based system  
- Animated visualization  
- Robust error handling  

---

## 🖥️ Demo

Run:

```bash
python run.py
Example Output
--- Environment Features ---
grid_size: 400
density: 0.2
start_goal_distance: 30

[LLM Selected Planner]: astar

--- Path Found ---
Path length: 42
🌍 Applications

This system models real-world AI agent behavior in navigation problems:

🚁 Search & Rescue
Navigating wilderness environments
Locating survivors in unknown terrain
🔥 Fire Response
Planning safe evacuation routes
Avoiding high-risk zones
⛏️ Mining & Industrial Systems
Navigating underground tunnels
Avoiding hazardous regions
🤖 Robotics & Autonomous Systems
Warehouse robots
Drone navigation
Autonomous vehicles (simplified abstraction)
🧭 General Path Planning
Game AI
Logistics optimization
Route planning systems
🧠 Key Insights
1. LLMs as Decision Layers

LLMs are best used to:

choose strategies
interpret environments

Not to replace deterministic algorithms.

2. Hybrid Systems Are Stronger
LLM (flexibility) + Algorithms (reliability) = Robust system
3. Constraints Improve Performance

Limiting tool access:

improves accuracy
reduces errors
increases safety
4. Always Design for Failure
LLMs are not guaranteed to succeed

Fallback systems are essential for real-world applications.

📁 Project Structure
src/
├── agent/
│   ├── agent.py
│   ├── llm_planner.py
│   ├── planner_selector.py
│   └── tool_caller.py
│
├── tools/
│   ├── bfs.py
│   ├── dijkstra.py
│   ├── astar.py
│   └── greedy_best_first.py
│
├── perception/
│   └── environment_analyzer.py
│
├── environment/
│   └── grid_world.py
│
├── visualization/
│   └── grid_visualizer.py
│
run.py
⚙️ Setup
1. Install dependencies
pip install -r requirements.txt
2. Set API key

Create a .env file:

NIM_API_KEY=your_key_here
3. Run the project
python run.py
🎥 Demo Video

Add your YouTube demo link here.

📊 Future Improvements
Dynamic obstacles
Multi-agent coordination
Learning-based planner selection
Real-time replanning
3D environments
🏁 Conclusion

This project demonstrates a modern AI agent architecture:

perception → reasoning → action
LLM-driven decisions
tool-based execution
robust fallback systems

It highlights how to build practical, reliable AI systems, not just theoretical ones.

⭐ Final Thought

The future of AI is not just models — it’s systems.


---

If you want a quick final polish, I can also:
- give you a **1-line GitHub description + tags**
- or help you make a **YouTube demo script (2–3 min, super clean)**
Gimme one long script I can copy 

Here’s a single, clean, copy-paste README.md script — no breaks, no commentary, just drop it straight into your repo:

# 🚀 Adaptive Grid Navigation Agent (LLM + Classical Planning)

## 🧠 Overview

This project implements an intelligent **grid navigation agent** that combines perception, reasoning, planning, and action into a unified AI system.

The agent operates in a randomized grid environment with obstacles and must determine the best path from a start position to a goal. Instead of relying on a fixed algorithm, the agent dynamically selects the most appropriate search strategy using a Large Language Model (LLM), while maintaining a deterministic fallback system for reliability.

This project demonstrates how modern AI systems can integrate **LLMs as decision-makers** with **classical algorithms as execution tools**.

---

## ⚡ tl;dr

- Navigates a randomly generated grid with obstacles  
- Uses an LLM to choose between BFS, Dijkstra, A*, or Greedy search  
- Falls back to rule-based logic if the LLM fails  
- Visualizes the path with animation  

**Key idea:** Combine LLM reasoning with deterministic algorithms to build robust AI systems.

---

## 🏗️ System Architecture


Environment (Grid + Obstacles)
↓
Perception (Feature Extraction)
↓
LLM Reasoning (Planner Selection)
↓
Fallback Rules (if LLM fails)
↓
Tool Calling (Search Algorithms)
↓
Execution + Visualization


---

## 🧩 Components

### 1. Perception
The system analyzes the environment and extracts key features such as:
- Grid size  
- Obstacle density  
- Distance between start and goal  

These features are used to inform planner selection.

---

### 2. Reasoning (LLM)

The agent uses an LLM (via NVIDIA NIM with the Kimi K2.5 model) to decide which search algorithm is best suited for the current environment.

Available planners:
- `bfs` (Breadth-First Search)
- `dijkstra`
- `astar`
- `greedy` (Greedy Best-First Search)

---

### 3. Planning (Tools)

Each search algorithm is implemented as an independent module (tool). The agent does not perform pathfinding directly — it selects a tool and executes it.

This separation enforces a clean architecture:
- LLM = decision layer  
- Algorithms = execution layer  

---

### 4. Tool Calling

The agent invokes one of the available tools based on the planner selected by the LLM (or fallback logic). This mirrors real-world AI systems where LLMs orchestrate external capabilities rather than replacing them.

---

### 5. Fallback Logic (Critical)

LLMs are not guaranteed to succeed. They may:
- fail due to API issues  
- return malformed outputs  
- produce incomplete responses due to token limits  

To ensure robustness, this system includes deterministic fallback logic. If the LLM fails for any reason, the agent selects a planner using predefined rules.

This guarantees that:

The system always produces a valid result.

---

## 🔒 Tool Restriction (Important Design Principle)

The agent is intentionally limited to a small, controlled set of tools:

[bfs, dijkstra, astar, greedy]

This constraint is critical for building reliable AI systems:
- Prevents hallucinated actions  
- Improves consistency  
- Reduces error surface  
- Enforces safe and interpretable behavior  

In modern AI systems, limiting the action space of an agent is just as important as improving its intelligence.

---

## 🎯 Features

- Randomized grid generation  
- Obstacle placement with varying density  
- Adaptive planner selection  
- LLM + rule-based hybrid decision system  
- Animated path visualization  
- Robust error handling and recovery  

---

## 🖥️ Demo

Run the project:

```bash
python run.py

Example output:

--- Environment Features ---
grid_size: 400
density: 0.2
start_goal_distance: 30

[LLM Selected Planner]: astar

--- Path Found ---
Path length: 42
🌍 Applications

This project models decision-making in real-world navigation problems and can be extended to several domains:

🚁 Search & Rescue
Navigating wilderness environments
Finding optimal paths in unknown terrain
Assisting in disaster response
🔥 Fire Response
Planning safe evacuation routes
Avoiding hazardous zones
Adapting to dynamic environments
⛏️ Mining & Industrial Systems
Navigating underground tunnels
Avoiding unsafe regions
Optimizing movement in constrained spaces
🤖 Robotics & Autonomous Systems
Warehouse robots
Drone navigation
Autonomous vehicles (simplified abstraction)
🧭 General Path Planning
Game AI
Logistics and routing
Optimization systems
🧠 Key Insights
1. LLMs Are Best Used for Reasoning, Not Execution

LLMs are powerful for selecting strategies and interpreting environments, but deterministic algorithms remain superior for precise computation.

2. Hybrid Systems Are More Robust

Combining flexible reasoning (LLMs) with reliable execution (algorithms) results in systems that are both adaptable and dependable.

3. Constraints Improve Performance

Limiting the tools available to an agent:

reduces hallucinations
improves accuracy
increases safety
4. Always Design for Failure

LLMs are inherently non-deterministic. A production-grade system must assume failure and include fallback mechanisms.

📁 Project Structure
src/
├── agent/
│   ├── agent.py
│   ├── llm_planner.py
│   ├── planner_selector.py
│   └── tool_caller.py
│
├── tools/
│   ├── bfs.py
│   ├── dijkstra.py
│   ├── astar.py
│   └── greedy_best_first.py
│
├── perception/
│   └── environment_analyzer.py
│
├── environment/
│   └── grid_world.py
│
├── visualization/
│   └── grid_visualizer.py
│
run.py
⚙️ Setup
1. Install dependencies
pip install -r requirements.txt
2. Set API Key

Create a .env file in the project root:

NIM_API_KEY=your_key_here

Make sure your code loads environment variables using python-dotenv.

3. Run the project
python run.py
🎥 Demo Video

Add your YouTube demo link here.

📊 Future Improvements
Dynamic obstacles and real-time replanning
Multi-agent coordination
Learning-based planner selection
3D navigation environments
Integration with real-world robotics systems
🏁 Conclusion

This project demonstrates a modern AI agent architecture that integrates:

perception
reasoning
planning
execution

It highlights the importance of combining LLMs with traditional algorithms, enforcing constraints, and designing systems that remain reliable even when components fail.

⭐ Final Thought

The future of AI is not just better models — it is better systems.


