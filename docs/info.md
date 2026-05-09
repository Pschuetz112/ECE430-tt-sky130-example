<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a 32x32 serial-parallel multiplier in Verilog using the PM32 architecture. Inputs are mapped through the Tiny Tapeout wrapper module and multiplied over several clock cycles. The low 8 bits of the product are displayed on the output pins.


## How to test

Apply a start pulse on ui_in[0].

Set:
- ui_in[4:1] = multiplicand
- uio_in[3:0] = multiplier

After several clock cycles, the low 8 bits of the product appear on uo_out[7:0].

Example:
- multiplicand = 3
- multiplier = 2
- output = 12
Explain how to use your project

## External hardware

N/A
