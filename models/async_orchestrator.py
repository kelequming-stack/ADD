import asyncio
import json
from models.schemas import DronePerceptionData, ProgressControlOutput, QualityControlOutput, SafetyAlertOutput

async def progress_control_agent(perception: DronePerceptionData) -> ProgressControlOutput:
    print("[Agent-进度] 正在载入 3D 点云与 BIM 模型...")
    await asyncio.sleep(1.5) # 模拟消耗大量计算资源的土方量体积比对
    print("[Agent-进度] 长链推理：核算基坑开挖体量，评估关键路径...")
    return ProgressControlOutput(
        planned_volume_m3=15000.0,
        actual_volume_m3=12500.0,
        schedule_deviation_days=-2.5,
        critical_path_impact=True
    )

async def quality_control_agent(perception: DronePerceptionData) -> QualityControlOutput:
    print("[Agent-质量] 正在解析高分辨率外墙影像...")
    await asyncio.sleep(2.0) # 模拟高并发视觉缺陷检测
    print("[Agent-质量] 长链推理：调取国家混凝土施工验收规范进行交叉验证...")
    return QualityControlOutput(
        inspection_item="基坑支护锚杆间距",
        is_compliant=False,
        defect_type="间距超差 > 5cm",
        rework_required=True
    )

async def safety_control_agent(perception: DronePerceptionData) -> SafetyAlertOutput:
    print("[Agent-安全] 正在分析红外热力图与作业人员轨迹...")
    await asyncio.sleep(1.0) # 模拟毫秒级延迟要求的边缘安全推理
    print("[Agent-安全] 紧急链路：检测到临边防护缺失及人员违章行为！")
    return SafetyAlertOutput(
        hazard_level="CRITICAL",
        violation_type="临边作业未挂安全带 & 防护栏杆断裂",
        location_coordinates=[104.06, 30.67, -12.5],
        immediate_action="触发声光报警，停工整改"
    )

async def main():
    print("=== 启动 AEC 多 Agent 异步三控合一 (Progress/Quality/Safety) ===")
    
    # 模拟无人机传输回来的多源异构数据包
    mock_payload = DronePerceptionData(
        drone_id="Drone_Matrix_01",
        data_type="multi_modal_fusion",
        raw_payload={"point_cloud": "...", "rgb_img": "...", "thermal": "..."}
    )
    
    # 核心：展示高并发能力，同时拉起三个重度消耗计算资源的 Agent 推理流
    print("\n>>> 发起并发推理任务 (Gathering Agents)...\n")
    results = await asyncio.gather(
        progress_control_agent(mock_payload),
        quality_control_agent(mock_payload),
        safety_control_agent(mock_payload)
    )
    
    progress_result, quality_result, safety_result = results
    
    print("\n=== 推理输出 (Pydantic 严格校验通过) ===")
    print("\n📊 施工进度报告:")
    print(progress_result.json(indent=2))
    print("\n✅ 施工质量报告:")
    print(quality_result.json(indent=2))
    print("\n⚠️ 施工安全告警:")
    print(safety_result.json(indent=2))

if __name__ == "__main__":
    asyncio.run(main())
