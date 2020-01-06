#!/usr/bin/env python3
import database as db
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "update":
        name = args[1]
        date = args[2]
        price = float(args[3])
        amt = int(args[4])
        a = db.TickerSet(name, date, price, amt)
    elif args[0] == "price":
        name = args[1]
        price = float(args[2])
        a = db.Price(name, price)
    db.update(a)
