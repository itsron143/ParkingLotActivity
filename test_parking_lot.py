import sys
import input_parser


def test_input_txt(capsys):
    input_parser.readFile("input.txt")
    out, err = capsys.readouterr()
    with open("output.txt") as file:
        commands = file.read()
    assert out == commands
