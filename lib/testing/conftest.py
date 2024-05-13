#!/usr/bin/env python3

def pytest_itemcollected(item):
    # Get the parent object (test class or module)
    par = item.parent.obj
    
    # Get the test function or method object
    node = item.obj
    
    # Extract the prefix (parent's docstring or class name) and suffix (test function or method name)
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    
    # Combine prefix and suffix to form the new test item name
    new_item_name = f"{pref} {suf}" if pref or suf else None
    
    # Update the nodeid with the new test item name
    if new_item_name:
        item._nodeid = new_item_name
