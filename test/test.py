# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start PM32 test")

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 2)

    # PM32 wrapper mapping:
    # ui_in[0] = start
    # ui_in[4:1] = mc
    # uio_in[3:0] = mp
    #
    # Test 3 * 2 = 6
    dut.ui_in.value = 0b00000111
    dut.uio_in.value = 0b00000010

    await ClockCycles(dut.clk, 70)

    assert int(dut.uo_out.value) == 6
