/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_pschuetz_pm32 (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    wire rst;
    wire start;
    wire [31:0] mc;
    wire [31:0] mp;
    wire [63:0] product;
    wire done;

    assign rst = ~rst_n;
    assign start = ui_in[0];


    assign mc = {28'b0, ui_in[4:1]};
    assign mp = {28'b0, uio_in[3:0]};

    pm32 pm32_inst (
        .clk(clk),
        .rst(rst),
        .start(start),
        .mc(mc),
        .mp(mp),
        .p(product),
        .done(done)
    );


    assign uo_out = product[7:0];


    assign uio_out = {7'b0, done};
    assign uio_oe  = 8'b00000001;

    wire _unused = &{ena, ui_in[7:5], uio_in[7:4], product[63:8], 1'b0};

endmodule
