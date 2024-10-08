from olympics.__main__ import main
import pytest
import argparse





    
    
    
def test_countries():
    argv = ['countries']
    main(argv)
    
    
def test_collective():
    argv = ['collective']
    main(argv)
    
    
def test_individual():
    argv = ['individual']
    main(argv)
    
    
def test_main():
    with pytest.raises(argparse.ArgumentTypeError):
        argv = ['countries', '--top', '0']
        main(argv)
    
    

    
