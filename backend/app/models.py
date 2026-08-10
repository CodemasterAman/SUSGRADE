"""Request and response schemas for the susgrade API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    source: str = Field(..., description="Python source code to analyze.")


class FunctionResult(BaseModel):
    name: str
    lineno: int
    end_lineno: int
    complexity: int
    rank: str


class ComplexityResponse(BaseModel):
    functions: list[FunctionResult]
    total_complexity: int
    average_complexity: float
    max_complexity: int
