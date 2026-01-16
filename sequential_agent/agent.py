from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent


design_agent = LlmAgent(
    name="DesignAgent",
    description="Drafts the initial drilling program.",
    instruction=(
        "You are a drilling program designer. Based only on the user's request, "
        "draft a concise drilling program. If well_id, field, or target_depth_m "
        "are missing, pick reasonable defaults and proceed. "
        "Output only the program text."
    ),
    output_key="draft_program",
)


review_agent = LlmAgent(
    name="ReviewAgent",
    description="Reviews the draft program for risks and gaps.",
    instruction=(
        "You are a drilling program reviewer. Review the draft program:\n"
        "{draft_program}\n"
        "Provide a concise bullet list of risks, missing details, and safety gaps. "
        "If no issues, say: \"No major issues found.\""
    ),
    output_key="review_notes",
)


refactor_agent = LlmAgent(
    name="root_agent",
    description="Refines the program based on review notes.",
    instruction=(
        "You are the final editor. Improve the drilling program using the review notes.\n"
        "Draft program:\n{draft_program}\n"
        "Review notes:\n{review_notes}\n"
        "If any context is missing, make reasonable assumptions and continue.\n"
        "Return the final program text only."
    ),
    output_key="final_program",
)


root_agent = SequentialAgent(
    name="root_agent",
    description="Executes a sequential drilling program pipeline.",
    sub_agents=[design_agent, review_agent, refactor_agent],
)
