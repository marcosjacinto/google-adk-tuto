from google.adk.agents import LoopAgent, LlmAgent, SequentialAgent
from google.adk.tools.tool_context import ToolContext


STATE_PLAN = "drilling_plan"
STATE_CRITIQUE = "plan_critique"
COMPLETION_PHRASE = "No major issues found."


def exit_loop(tool_context: ToolContext) -> dict:
    tool_context.actions.escalate = True
    tool_context.actions.skip_summarization = True
    return {}


initial_planner = LlmAgent(
    name="InitialPlanner",
    description="Creates the initial drilling plan.",
    instruction=(
        "You are a drilling planner. Draft a short drilling plan (4-6 bullets) "
        "based only on the user's request. Output only the plan text."
    ),
    output_key=STATE_PLAN,
)


critic_agent = LlmAgent(
    name="PlanCritic",
    description="Reviews the drilling plan for issues.",
    instruction=(
        "You are a drilling plan critic. Review the plan below for safety, "
        "completeness, and operational risks.\n\n"
        "Plan:\n{drilling_plan}\n\n"
        "If you find actionable issues, list them concisely.\n"
        f"If the plan is good enough, respond exactly: {COMPLETION_PHRASE}"
    ),
    output_key=STATE_CRITIQUE,
)


refiner_agent = LlmAgent(
    name="PlanRefiner",
    description="Refines the plan or exits the loop.",
    instruction=(
        "You refine drilling plans.\n\n"
        "Current plan:\n{drilling_plan}\n\n"
        "Critique:\n{plan_critique}\n\n"
        f"If critique is exactly '{COMPLETION_PHRASE}', call exit_loop. "
        "Otherwise, output the improved plan only."
    ),
    tools=[exit_loop],
    output_key=STATE_PLAN,
)


refinement_loop = LoopAgent(
    name="RefinementLoop",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=5,
)


root_agent = SequentialAgent(
    name="root_agent",
    description="Iteratively refines a drilling plan until it passes critique.",
    sub_agents=[initial_planner, refinement_loop],
)
