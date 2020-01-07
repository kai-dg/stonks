#!/usr/bin/env python3
"""Contains functions and classes that reads or writes to the
json database file.
"""
import ujson as json
import os
ABSPATH = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(ABSPATH, ".stocks.json")


class Price:
    __slots__ = ("name", "price",)
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class TickerSet:
    """Used for updating a single ticker with new data.
    """
    __slots__ = ("name", "date_bought", "pb", "amt",)
    def __init__(self, name: str, date_bought: str, pb: float, amt: int):
        self.name = name
        self.date_bought = date_bought
        self.pb = pb
        self.amt = amt

def read():
    if os.path.exists(DATABASE):
        with open(DATABASE, "r") as f:
            data = json.load(f)
    else:
        with open(DATABASE, "w+") as f:
            f.write("{}")
            data = {}
    return data

def update_all(data):
    """Args:
        data (dict): Full dict of json data.
    """
    with open(DATABASE, "w+") as f:
        json.dump(data, f)

def update(ticker):
    """Args:
        ticker (obj): Class of TickerSet or Price
    """
    data = read()
    if isinstance(ticker, TickerSet):
        new_data = {"pb": ticker.pb, "amt": ticker.amt}
        data[ticker.name]["date_bought"][ticker.date_bought] = new_data
    elif isinstance(ticker, Price):
        data[ticker.name]["price"] = ticker.price
        
    with open(DATABASE, "w+") as f:
        json.dump(data, f)
