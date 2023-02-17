import asyncio
from mavsdk import System


# Example taken and modified from https://github.com/mavlink/MAVSDK-Python/blob/main/examples/takeoff_and_land.py
# TODO: detect radio signals using MavSDK (or another library if you can't find a way)
# use `async cube.action.kill()` when the kill switch is detected to have been flipped

path = "/dev/ttyACM0"
baud = 57600

async def main():
    cube = System()
    print("Waiting for drone to connect...")
    await cube.connect(f'serial://{path}:{baud}')

    # maybe you might have to create an async task to detect radio inputs and kill boat then?
    status_text_task = asyncio.ensure_future(print_status_text(cube))
    check_kill_switch_task = asyncio.ensure_future(check_kill_switch(cube))

    async for state in cube.core.connection_state():
        if state.is_connected:
            print(f"...Connection established!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in cube.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    print("-- Arming")
    await cube.action.arm()

    status_text_task.cancel()
    check_kill_switch_task.cancel()


async def print_status_text(cube: System):
    try:
        async for status_text in cube.telemetry.status_text():
            print(f"Status: {status_text.type}: {status_text.text}")
    except asyncio.CancelledError:
        return


async def check_kill_switch(cube: System):
    try:
        async for rc_channels in cube.telemetry.rc_channels():
            kill_switch = rc_channels.chan6_raw
            if kill_switch == 100:
                cube.action.kill()

    except asyncio.CancelledError:
        return


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(main())


