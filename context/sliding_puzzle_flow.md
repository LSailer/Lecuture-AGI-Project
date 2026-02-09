# Sliding Puzzle Solver Flow

This diagram illustrates the execution flow of the MAKER framework for the Sliding Puzzle, highlighting the voting process and the fallback mechanism.

```mermaid
graph TD
    Start([Start Solver]) --> Init[Initialize Game, Agent, and Fallback]
    Init --> Loop{is_solved or max_steps?}
    
    Loop -- No --> GetState[Get Current State]
    GetState --> BatchRun[Run Voting Batch <br/>run_voting_batch]
    
    subgraph VotingProcess [Voting & Consensus]
        BatchRun --> BuildPrompts[Build Prompts <br/>agent.build_prompt]
        BuildPrompts --> LLMGen[Batch LLM Generation <br/>llm.generate_batch]
        LLMGen --> Parse[Parse Responses <br/>agent.parse_response]
        Parse --> Tally[Tally Votes]
        Tally --> MarginCheck{Margin K met?}
        MarginCheck -- No --> ExtraAgents[Run Additional Agents]
        ExtraAgents --> Tally
        MarginCheck -- Yes --> Consensus[Return Best Action]
    end
    
    Consensus --> ActionCheck{Valid Action Found?}
    
    ActionCheck -- Yes --> ApplyMove[Apply Move to Game]
    ApplyMove --> Loop
    
    ActionCheck -- No --> Fallback[Engage Fallback <br/>MASTER FALLBACK]
    
    subgraph FallbackMechanism [Fallback Mechanism]
        Fallback --> MetaPrompt[Build Meta-Prompt <br/>with Failed Predictions]
        MetaPrompt --> MetaModel[Call Fallback Model <br/>Gemini/Local]
        MetaModel --> NewPrompts[Generate Improved <br/>System & User Prompts]
        NewPrompts --> RetryVoting[Retry Voting Batch <br/>with Overridden Prompts]
    end
    
    RetryVoting --> RetryCheck{Action Found?}
    RetryCheck -- Yes --> ApplyMove
    RetryCheck -- No --> RetryLimit{Retry Limit Reached?}
    RetryLimit -- No --> Fallback
    RetryLimit -- Yes --> Fail([Fail: No Valid Move])
    
    Loop -- Yes --> End([End: Success/Max Steps])
```

## Flow Description

### 1. Voting & Consensus
- **Batch Generation**: The `run_voting_batch` function triggers multiple agent instances in parallel.
- **Parsing**: `agent.parse_response` extracts the predicted move and the expected resulting state. If parsing fails (regex mismatch or invalid move), it records a `FailedPrediction`.
- **Margin K**: The system ensures the winning move has at least `k` more votes than the runner-up to ensure high-confidence steps.

### 2. Fallback Mechanism
- **Trigger**: Activated only when the voting batch returns no valid `best_action` (typically because all agents failed to provide a valid parse).
- **Meta-Reasoning**: The `FallbackModel` takes the original prompts and the specific failure reasons (e.g., "Invalid move [2, 0] for current state") and asks a stronger model to rewrite the instructions.
- **Prompt Overrides**: The `run_voting_batch` function is called again, but this time using `system_prompt_override` and `user_prompt_override` provided by the fallback model.
