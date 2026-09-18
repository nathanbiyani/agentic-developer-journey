from fastapi import APIRouter, HTTPException

from models.schemas import UseCaseRecord
from services.use_case_catalog import get_use_case, list_use_cases

router = APIRouter(prefix="/api/use-cases", tags=["use-cases"])


@router.get("", response_model=list[UseCaseRecord], response_model_by_alias=True)
def read_use_cases() -> list[UseCaseRecord]:
    return list_use_cases()


@router.get("/{use_case_id}", response_model=UseCaseRecord, response_model_by_alias=True)
def read_use_case(use_case_id: str) -> UseCaseRecord:
    record = get_use_case(use_case_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Use case not found.")
    return record