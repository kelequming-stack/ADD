from pydantic import BaseModel, Field
from typing import List

# 统一输入模型
class DronePerceptionData(BaseModel):
    drone_id: str
    data_type: str = Field(description="例如: point_cloud, high_res_image, thermal")
    raw_payload: dict

# 进度控制输出模型
class ProgressControlOutput(BaseModel):
    planned_volume_m3: float
    actual_volume_m3: float
    schedule_deviation_days: float
    critical_path_impact: bool

# 质量控制输出模型
class QualityControlOutput(BaseModel):
    inspection_item: str
    is_compliant: bool
    defect_type: str = Field(default="None")
    rework_required: bool

# 安全控制输出模型
class SafetyAlertOutput(BaseModel):
    hazard_level: str = Field(description="LOW, MEDIUM, HIGH, CRITICAL")
    violation_type: str
    location_coordinates: List[float]
    immediate_action: str
