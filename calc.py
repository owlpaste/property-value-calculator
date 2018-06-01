# -*- coding: utf8 -*-

import argparse
import pandas as pd
import numpy as np
from tabulate import tabulate


HOUSE_VALUES = range(50000, 1050000, 50000)
HEADERS = ['Property value', 'Mortgage', 'Mortgage deposit', 'Salary deposit', 'Total deposit', 'Savings per year', 'Savings per month']
COLUMNS = ['property_value', 'mortgage', 'mortgage_deposit', 'salary_deposit', 'total_deposit', 'per_year', 'per_month']


def main():
    parser = argparse.ArgumentParser(description='Calculate mortgage and savings required based on property values.')
    parser.add_argument('salary', type=int, help='Salary.')
    parser.add_argument('--deposit_percent', type=int, default=15, help='LTV %%.')
    parser.add_argument('--deposit', type=int, default=0, help='Deposit saved.')
    parser.add_argument('--years', type=int, default=10, help='Years before buying.')
    parser.add_argument('--multiplier', type=float, default=4.5, help='Salary multiplier.')

    args = parser.parse_args()

    df = calculate(args)
    table = tabulate(df, headers=HEADERS, tablefmt='psql', showindex=False, floatfmt="3,.0f")

    print "Deposit £{:,.0f}".format(args.deposit)
    print "LTV %{}".format(args.deposit_percent)
    print "Saving over {} years".format(args.years)
    print "Salary multiplier x{}".format(args.multiplier)
    print "Salary: £{:,.0f}".format(args.salary)
    print table


def prepare_table():
    data = {}
    for column in COLUMNS:
        data[column] = 0

    data['property_value'] = HOUSE_VALUES
    return data


def calculate(args):
    data = prepare_table()
    df = pd.DataFrame(data=data, columns=COLUMNS)

    df['mortgage'] = df['property_value'] * (1 - float(args.deposit_percent) / 100)

    # Extra deposit required due to salary x multiplier not being enough to reach mortgage amount
    df['salary_deposit'] = np.where(df['mortgage'] - args.salary * args.multiplier > 0,
                                    df['mortgage'] - args.salary * args.multiplier, 0)
    df['mortgage_deposit'] = df['property_value'] - df['mortgage']

    # Total deposit is mortgage + salary deposit - any deposit that already exists
    df['total_deposit'] = np.where(df['salary_deposit'] + df['mortgage_deposit'] - args.deposit > 0,
                                   df['salary_deposit'] + df['mortgage_deposit'] - args.deposit, 0)

    df['per_year'] = df['total_deposit'] / args.years
    df['per_month'] = df['per_year'] / 12
    return df


if __name__ == '__main__':
    main()
