# O1 LLM Solutions for Advent of Code

This repository demonstrates using OpenAI's O1 LLM capabilities (via ChatGPT) to solve Advent of Code challenges. For each solution, you can find:

- The original prompt used
- The public ChatGPT conversation
- Number of prompt iterations required
- Time taken to reach a solution

## Solution Stats

| Day | Solved (Silver/Gold) | Iterations | Time Taken | One-Shot Success | Chat Link |
|-----|---------------------|------------|------------|------------------|-----------|
| 1   | ✅/✅               | 1          | 20s        | ✅               | [Chat](https://chatgpt.com/share/674c9de5-1d4c-8005-8b67-2bb1029cb4b9) |
| 2   | ✅/✅               | 1          | 30s        | ✅               | [Chat](https://chatgpt.com/share/674d42f4-1424-8005-826b-453db70d2645) |
| 3   | ✅/✅               | 1          | 60s        | ✅               | [Chat](https://chatgpt.com/share/674ea076-a0f4-8005-944d-2653f0991c5c) |
| 4   | ✅/✅               | 1          | 33s        | ✅               | [Chat](https://chatgpt.com/share/67504736-fc5c-8005-a5b7-b4e8ddb0c854) |

## Approach

Each puzzle solution includes:
1. Initial prompt to ChatGPT
2. Run code locally to validate the solution
3. Iterate

The goal is to showcase both the potential and limitations of using LLMs for algorithmic problem solving.

## Running the Code

```
python3 1/gold.py < 1/input.txt
python3 1/silver.py < 1/input.txt
```

## Original Puzzles & Answers

Each puzzle includes:
- Original puzzle text
- Example inputs
- Correct answers for both parts

This allows for:
- Testing other LLMs against same problems
- Validating solutions
- Benchmarking different approaches
