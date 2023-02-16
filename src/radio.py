import asyncio
from mavsdk import System


# Example taken and modified from https://github.com/mavlink/MAVSDK-Python/blob/main/examples/takeoff_and_land.py
# TODO: detect radio signals using MavSDK (or another library if you can't find a way)
# use `async cube.action.kill()` when the kill switch is detected to have been flipped

path = "dev/ttyACM0"
baud = 57600
async def main():

    cube = System()
    await cube.connect(system_address=f'serial://{path}:{baud}')

    # maybe you might have to create an async task to detect radio inputs and kill boat then?
    status_text_task = asyncio.ensure_future(print_status_text(cube))

    print("Waiting for drone to connect...")
    async for state in cube.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in cube.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    print("-- Arming")
    await cube.action.arm()

    # use this somewhere
    await cube.action.kill()

    status_text_task.cancel()



async def print_status_text(drone):
    try:
        async for status_text in drone.telemetry.status_text():
            print(f"Status: {status_text.type}: {status_text.text}")
    except asyncio.CancelledError:
        return


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(main())


