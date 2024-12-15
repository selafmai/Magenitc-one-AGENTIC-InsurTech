import asyncio
from src.utils.helper import setup_logging, load_environment
from src.utils.insurance_utils import PolicyGenerator
from PIL import Image

async def test_workflow():
    # Nastavitev okolja
    setup_logging("logs")
    load_environment()
    
    # Pripravite testne podatke
    test_image_path = "pot/do/testne/slike.jpg"
    test_data = {
        "image_path": test_image_path,
        "location": "Ljubljana, Slovenia",
        "coverage_type": "property"
    }
    
    # Zagon glavne aplikacije
    from src.main import main
    await main("logs")

if __name__ == "__main__":
    asyncio.run(test_workflow()) 