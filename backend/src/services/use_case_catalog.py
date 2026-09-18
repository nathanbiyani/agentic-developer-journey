from models.schemas import UseCaseRecord


_USE_CASES = {
    "AI-2026-0118": UseCaseRecord.model_validate(
        {
            "id": "AI-2026-0118",
            "name": "Quality Event Summarizer",
            "sourceSystem": "J&J Governance Portal",
            "sourceUpdatedAt": "2026-09-17T19:45:00Z",
            "status": "Approved",
            "currentStage": "data-knowledge",
            "riskLevel": "High",
            "dataClassification": "Confidential",
            "businessUnit": "MedTech Quality",
            "summary": "Summarize quality event records and surface relevant patterns for review by quality specialists.",
            "approvedAt": "2026-09-08T16:05:00Z",
            "approvedDefinition": [
                {"key": "identity", "title": "Project identification", "facts": [{"label": "Approved use case", "value": "Quality Event Summarizer"}, {"label": "Audience", "value": "J&J employees and contractors"}, {"label": "Business unit", "value": "MedTech Quality"}, {"label": "Region", "value": "United States"}]},
                {"key": "business", "title": "Business context", "facts": [{"label": "Business need", "value": "Summarize quality event records and surface relevant patterns for review by quality specialists."}, {"label": "Problem", "value": "Manual review of quality-event narratives delays signal identification and consumes specialist capacity."}, {"label": "Goal", "value": "Reduce review cycle time while preserving specialist accountability."}, {"label": "Success measure", "value": "Time to first review: 3.8 hours baseline to 1.5 hours target"}]},
                {"key": "technical", "title": "Approved technical design", "facts": [{"label": "Pattern", "value": "Retrieval-augmented generation over approved quality records"}, {"label": "Capabilities", "value": "Search and answer; summarize; content generation"}, {"label": "Evaluation", "value": "Held-out quality-event set with specialist review"}, {"label": "Quality threshold", "value": "At least 92% grounded-summary accuracy before production"}]},
                {"key": "risk", "title": "Risk and controls", "facts": [{"label": "Risk classification", "value": "High"}, {"label": "Primary risk", "value": "Unsupported or incomplete quality-event summary"}, {"label": "Required control", "value": "Human review before operational use"}, {"label": "Owner and SLA", "value": "MedTech Quality; review within 24 hours"}]},
                {"key": "compliance", "title": "Data and compliance", "facts": [{"label": "Information classification", "value": "Confidential J&J information"}, {"label": "Personal data", "value": "No direct PII approved"}, {"label": "Data boundary", "value": "J&J-controlled systems; United States"}, {"label": "Applicable controls", "value": "GxP evidence; source permissions; citations; audit retention"}]},
                {"key": "traceability", "title": "Governance and traceability", "facts": [{"label": "Output tracking", "value": "Prompt, retrieval evidence, model version, and reviewer decision logged"}, {"label": "Access control", "value": "Microsoft Entra ID with application roles"}, {"label": "Periodic review", "value": "Quarterly evaluation and annual access recertification"}, {"label": "Approvals", "value": "Business Owner; AI Governance; MedTech Quality; Information Security"}]},
            ],
            "lifecycle": [
                {"key": "submit", "label": "Submit", "status": "complete", "owner": "Requester", "completedAt": "2026-09-03T14:20:00Z"},
                {"key": "coe-review", "label": "COE Review", "status": "complete", "owner": "AI COE", "completedAt": "2026-09-05T12:00:00Z"},
                {"key": "governance", "label": "Governance", "status": "complete", "owner": "GenAI Council", "completedAt": "2026-09-08T16:05:00Z"},
                {"key": "approved", "label": "Approved", "status": "complete", "owner": "GenAI Council", "completedAt": "2026-09-08T16:05:00Z"},
                {"key": "data-knowledge", "label": "Data & Knowledge", "status": "current", "owner": "Developer"},
                {"key": "tools-agents", "label": "Tools & Agents", "status": "pending", "owner": "Developer"},
                {"key": "channels", "label": "Channels & Distribution", "status": "pending", "owner": "Developer"},
                {"key": "memory-state", "label": "Memory & State", "status": "pending", "owner": "Developer"},
                {"key": "architecture", "label": "Architecture", "status": "pending", "owner": "Developer"},
                {"key": "access-governance", "label": "Access & Governance", "status": "pending", "owner": "Developer and Security"},
                {"key": "model-capacity", "label": "Model & Capacity", "status": "pending", "owner": "Developer and Platform Engineering"},
                {"key": "region-readiness", "label": "Region Readiness", "status": "pending", "owner": "Platform Engineering"},
                {"key": "infrastructure-deploy", "label": "Infrastructure & Deploy", "status": "pending", "owner": "Platform Engineering"},
                {"key": "production", "label": "Production", "status": "pending", "owner": "Release Manager"},
            ],
        }
    ),
    "AI-2026-0142": UseCaseRecord.model_validate(
        {
            "id": "AI-2026-0142",
            "name": "Commercial Content Assistant",
            "sourceSystem": "J&J Governance Portal",
            "sourceUpdatedAt": "2026-09-17T20:15:00Z",
            "status": "Awaiting Review",
            "currentStage": "governance",
            "riskLevel": "Moderate",
            "dataClassification": "Internal",
            "businessUnit": "Commercial",
            "summary": "Help commercial teams draft and review content against approved claims and brand guidance.",
            "approvedAt": None,
            "approvedDefinition": [],
            "lifecycle": [
                {"key": "submit", "label": "Submitted", "status": "complete", "owner": "Requester", "completedAt": "2026-09-12T15:30:00Z"},
                {"key": "coe-review", "label": "AI COE review", "status": "complete", "owner": "AI COE", "completedAt": "2026-09-15T17:00:00Z"},
                {"key": "governance", "label": "GenAI Council review", "status": "current", "owner": "GenAI Council"},
                {"key": "approved", "label": "Council decision", "status": "pending", "owner": "GenAI Council"},
                {"key": "enablement", "label": "Architecture enablement", "status": "blocked", "owner": "Developer"},
            ],
        }
    ),
    "AI-2026-0106": UseCaseRecord.model_validate(
        {
            "id": "AI-2026-0106",
            "name": "Research Insights Agent",
            "sourceSystem": "J&J Governance Portal",
            "sourceUpdatedAt": "2026-09-11T13:10:00Z",
            "status": "Rejected",
            "currentStage": "decision",
            "riskLevel": "High",
            "dataClassification": "Restricted",
            "businessUnit": "Research",
            "summary": "Synthesize external and internal research evidence for early discovery teams.",
            "approvedAt": None,
            "approvedDefinition": [],
            "lifecycle": [
                {"key": "submit", "label": "Submitted", "status": "complete", "owner": "Requester", "completedAt": "2026-08-25T14:20:00Z"},
                {"key": "coe-review", "label": "AI COE Review", "status": "complete", "owner": "AI COE", "completedAt": "2026-08-28T16:00:00Z"},
                {"key": "governance", "label": "GenAI Council Review", "status": "complete", "owner": "GenAI Council", "completedAt": "2026-09-11T13:10:00Z"},
                {"key": "decision", "label": "Council Decision", "status": "current", "owner": "GenAI Council"},
                {"key": "enablement", "label": "Architecture & Infrastructure", "status": "blocked", "owner": "Developer"},
            ],
        }
    ),
    "AI-2026-0092": UseCaseRecord.model_validate(
        {
            "id": "AI-2026-0092",
            "name": "Supply Chain Copilot",
            "sourceSystem": "J&J Governance Portal",
            "sourceUpdatedAt": "2026-09-14T18:20:00Z",
            "status": "In Progress",
            "currentStage": "infrastructure-deploy",
            "riskLevel": "Moderate",
            "dataClassification": "Internal",
            "businessUnit": "Supply Chain",
            "summary": "Help planners investigate supply exceptions using governed operational data.",
            "approvedAt": "2026-08-30T11:00:00Z",
            "approvedDefinition": [],
            "lifecycle": [
                {"key": "governance", "label": "Governance Approval", "status": "complete", "owner": "GenAI Council", "completedAt": "2026-08-30T11:00:00Z"},
                {"key": "data-knowledge", "label": "Data & Knowledge", "status": "complete", "owner": "Developer", "completedAt": "2026-09-02T15:00:00Z"},
                {"key": "tools-agents", "label": "Tools & Agents", "status": "complete", "owner": "Developer", "completedAt": "2026-09-04T15:00:00Z"},
                {"key": "architecture", "label": "Architecture", "status": "complete", "owner": "Developer", "completedAt": "2026-09-08T15:00:00Z"},
                {"key": "model-capacity", "label": "Model & Capacity", "status": "complete", "owner": "Platform Engineering", "completedAt": "2026-09-10T15:00:00Z"},
                {"key": "region-readiness", "label": "Region Readiness", "status": "complete", "owner": "Platform Engineering", "completedAt": "2026-09-12T15:00:00Z"},
                {"key": "infrastructure-deploy", "label": "Infrastructure & Deploy", "status": "current", "owner": "Platform Engineering"},
                {"key": "production", "label": "Production", "status": "pending", "owner": "Release Manager"},
            ],
        }
    ),
    "AI-2026-0074": UseCaseRecord.model_validate(
        {
            "id": "AI-2026-0074",
            "name": "Medical Knowledge Agent",
            "sourceSystem": "J&J Governance Portal",
            "sourceUpdatedAt": "2026-09-02T16:45:00Z",
            "status": "Completed",
            "currentStage": "production",
            "riskLevel": "High",
            "dataClassification": "Confidential",
            "businessUnit": "MedTech Quality",
            "summary": "Provide cited answers from approved medical affairs knowledge.",
            "approvedAt": "2026-07-21T14:00:00Z",
            "approvedDefinition": [],
            "lifecycle": [
                {"key": "governance", "label": "Governance Approval", "status": "complete", "owner": "GenAI Council", "completedAt": "2026-07-21T14:00:00Z"},
                {"key": "architecture", "label": "Architecture Questionnaire", "status": "complete", "owner": "Developer", "completedAt": "2026-08-01T14:00:00Z"},
                {"key": "infrastructure-deploy", "label": "Infrastructure & Deploy", "status": "complete", "owner": "Platform Engineering", "completedAt": "2026-08-18T14:00:00Z"},
                {"key": "production", "label": "Production", "status": "complete", "owner": "Release Manager", "completedAt": "2026-09-02T16:45:00Z"},
            ],
        }
    ),
}


def get_use_case(use_case_id: str) -> UseCaseRecord | None:
    return _USE_CASES.get(use_case_id)


def list_use_cases() -> list[UseCaseRecord]:
    return sorted(_USE_CASES.values(), key=lambda record: record.source_updated_at, reverse=True)