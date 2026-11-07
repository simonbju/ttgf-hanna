library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tt_um_example is
    port (
        ui_in   : in  std_logic_vector(7 downto 0);
        uo_out  : out std_logic_vector(7 downto 0);
        uio_in  : in  std_logic_vector(7 downto 0);
        uio_out : out std_logic_vector(7 downto 0);
        uio_oe  : out std_logic_vector(7 downto 0);
        ena     : in  std_logic;
        clk     : in  std_logic;
        rst_n   : in  std_logic
    );
end tt_um_example;

architecture Behavioral of tt_um_example is
    signal tal1 : unsigned(5 downto 0);
    signal tal2 : unsigned(5 downto 0);
    signal op : unsigned(1 downto 0);
    signal res : unsigned(11 downto 0);
begin
    tal1 <= unsigned(ui_in(5 downto 0));
    tal2 <= unsigned(uio_in(5 downto 0));
    op <= unsigned(ui_in(7 downto 6));

    res <= "000000" & tal1 + tal2 when op = "00" 
    else "000000" & tal1 - tal2 when op = "01"
    else tal1 * tal2 when op = "10"
    else "111111111111";
    -- else tal1 / tal2;

    uo_out <= "00" & std_logic_vector(res(5 downto 0));

end Behavioral;