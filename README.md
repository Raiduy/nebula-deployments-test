# Nebula Deployments Test

This is the testbed for different deployments of the OpenWebUI interface along with different peripheral containers.

### Goal
The goal of these experiments is to find the optimal setup for OpenWebUI.

### Method
We are going to compare three different cases.

| Setup                                   | Database   | VectorDB                     | LLMs                                    | Knowledge Bases                                |
|-----------------------------------------|------------|------------------------------|-----------------------------------------|------------------------------------------------|
| **Baseline**                            | SQLite     | Chroma (builtin)             | DeepSeek‑R1:1.5b (remote), Gemma3:12b (local) | small (5 documents), large (entire OpenWebUI documentation) |
| **Setup 1: PostgreSQL**                 | PostgreSQL | Chroma (builtin)             | DeepSeek‑R1:1.5b (remote), Gemma3:12b (local) | small (5 documents), large (entire OpenWebUI documentation) |
| **Setup 2: Chroma deployed separately** | SQLite     | Chroma (deployed separately) | DeepSeek‑R1:1.5b (remote), Gemma3:12b (local) | small (5 documents), large (entire OpenWebUI documentation) |

### Experiment Setup
Two instances:
1. Main WebUI + Ollama instance running Gemma3:12b
2. Peripheral Ollama instance running DeepSeek-r1:1.5b

### What we're measuring
* Speed
* Answer quality

### Running
1. Create a set of 5 questions for each Knowledge Base (KB), that differ in terms of difficulty and information placement in the individual Knowledge base files
2. Ask these questions sequentially, via the API to each of the LLMs, therefore having Deepseek + small KB, Deepseek + large KB, Gemma + small KB, Gemma + large KB. Each question is going to be asked 30 times, and randomized.
Measure the performance in terms of inference, and quality of the answer
3. Based on the results, decide whether to upgrade the setup of our current Nebula instance
4. If Setup 1 and Setup 2 both show improvements, then create and test Setup 3 that runs both PostgreSQL and Chroma deployed separately

### Future tests
* Keep PostgreSQL, and test performance with an LLM proxy.
* Keep PostgreSQL, and test different vectorDBs: OpenSearch, Milvus, PGvector, Qdrant.

