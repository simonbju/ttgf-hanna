# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Test of 21*1

    # 2 first bits sets operator, 6 last is number
    dut.ui_in.value = 0b10010101
    # 6 last is number
    dut.uio_in.value = 0b00000001

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 0b00010101

   # Test of 21+1

    # 2 first bits sets operator, 6 last is number
    dut.ui_in.value = 0b00010101
    # 6 last is number
    dut.uio_in.value = 0b00000001

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 0b00010110

    # Test of 21-1
    
    # 2 first bits sets operator, 6 last is number
    dut.ui_in.value = 0b01010101
    # 6 last is number
    dut.uio_in.value = 0b00000001

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 0b00010100

