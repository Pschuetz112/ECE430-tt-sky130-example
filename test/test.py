import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


async def run_mult_debug(dut, mc, mp):
    dut._log.info(f"Testing mc={mc}, mp={mp}")

    # Load inputs with start low
    dut.ui_in.value = mc << 1
    dut.uio_in.value = mp
    await ClockCycles(dut.clk, 2)

    # Pulse start for EXACTLY one clock
    dut.ui_in.value = (mc << 1) | 1
    await ClockCycles(dut.clk, 1)

    # Drop start
    dut.ui_in.value = mc << 1

    # Watch output while multiplier runs
    for cycle in range(80):
        await ClockCycles(dut.clk, 1)

        out_val = int(dut.uo_out.value)
        done_val = int(dut.uio_out.value) & 1

        dut._log.info(
            f"cycle={cycle:02d}, uo_out={out_val}, done={done_val}"
        )

        if done_val == 1:
            dut._log.info(f"DONE at cycle {cycle}, result={out_val}")
            return out_val

    raise AssertionError("PM32 never asserted done")


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start PM32 debug test")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)

    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 5)

    result = await run_mult_debug(dut, 3, 2)

    assert result == 6
