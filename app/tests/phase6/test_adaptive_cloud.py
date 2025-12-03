import asyncio
from app.core.agents.namo_agent import NamoAgent
from app.core.cloud.adaptive_memory import AdaptiveCloudMemory

async def test_collective_memory():
    agent1 = NamoAgent("A1")
    agent2 = NamoAgent("A2")

    await agent1.reflect("The calm within connects to all minds.")
    await agent2.reflect("The compassion spreads like waves of light.")

    memory = AdaptiveCloudMemory()
    status = await memory.get_collective_reflection()
    print("Collective Memory Status:", status)

if __name__ == "__main__":
    asyncio.run(test_collective_memory())
