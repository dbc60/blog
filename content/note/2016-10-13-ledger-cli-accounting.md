---
title: Ledger Command-line Accounting
date: 2016-10-13
draft: true
categories: financial
tags:
  - accounting
  - finances
---

Better budgeting through automated transactions and virtual accounts.
<!--more-->

## Virtual Accounts are Budgets

Really!

## Ledger Format

The initial character of each line determines what the line means and how it should be interpreted. Allowable initial characters are:

- Number: denotes a transaction. See below for a description.
- `P`: an historical price for a commodity (`P DATE SYMBOL PRICE`).
- `=`: an automated transaction.
- `~`: a periodic transaction.
- `; # % | *`: indicates a comment.
- indented `;`: an indented semicolon inside a transaction is parsed as a persistent note for its preceding category. These notes or tags can be used to augment the reporting and filtering capabilities of Ledger.

A line beginning with a number denotes a transaction. It may be followed by any number of lines, each beginning with white-space, to denote the transaction's account posting. The format of the first line is `DATE[=EDATE] [*|!] [(CODE)] DESC`.

- `DATE`: the date of the transaction. It may be _cleared_ or _pending_.
- `EDATE`: the effective date of the transaction if it is _cleared_.
- `*`: indicates the transaction is _cleared_.
- `!`: indicates the tranaction is _pending_.
- `(CODE)`: this can indicate anything the user wants, such as a check number or the type of posting. For example, one might use `(ATM)` to mean that the posting involved a withdrawl or deposit using an ATM.
- `DESC`: the name of the payee or a description of the transaction.

The format of the lines that make up the body of the transaction is `ACCOUNT  AMOUNT  [; NOTE]`.

- The `ACCOUNT` may be surrounded by parentheses if it is a virtual posting, or square brackets if it is a virtual posting that must balance.
- The `AMOUNT`can be followd by a per-unit posting cost by specifying `@ AMOUNT` or by a complete posting cost with `@@ AMOUNT`.
- The `NOTE` may specify an actual and/or effective date for the posting by using the syntax `[ACTUAL_DATE]` or `[=EFFECTIVE_DATE]` or `[ACTUAL_DATE=EFFECTIVE_DATE]`.

## Tips for Using Ledger in a Business

The general format for a ledger is usually Assets, Liabilities, Equity, Income and Expenses. Customer invoices would typically be under Assets:Accounts Receivable and supplier invoices would be under Liabilities:Accounts Payable.

Assuming you're using ledger for a U.S. business, take a look at Schedule C, since that's likely what you're going to have to fill out on a regular basis from your ledger. My expense categories, for example, match the categories on lines 18-27. My revenue categories come from lines 1-4.

As a structure, I have a top level "BusinessName" category for the business, as well as top level "Customers" and "Suppliers" categories.

Someone paying for work performed service would look like this:

```ledger
2015-01-01 Fixed Widget
    BusinessName:Assets:AccountsReceivable:Labor   $100
    Customers:CustomerName:AccountsPayable   -$100
```

Them paying the bill would look like this - it's a 4-part transaction
so that everything balances on both ends - I wrote about this
"Transfer pattern" from a while ago:
https://groups.google.com/d/msg/ledger-cli/K7EgJQuEQ_M/WGzdFhtuqwIJ

```ledger
2015-01-02 Payment for Work Performed, Check #1234
    BusinessName:Transfer:ChecksUncashed          $100
    BusinessName:Assets:AccountsReceivable:Labor  -$100
    Customers:CustomerName:Equity                 -$100
    Customers:CustomerName:AccountsPayable        $100
```

Then when the check gets deposited:

```ledger
2015-01-03 Deposit to Checking
    BusinessName:Assets:CheckingAccount    $100
    BusinessName:Transfer:ChecksUncashed   -$100
```

This way, at the end, the customer's balance should be zero, and you
can reconcile your deposits easily.

## Generating Reports

- Find the balance of all your accounts: `ledger balance`
- Get your checking account balance:
    - Consider budgets (virtual accounts): `ledger reg checking`
    - Consider only real accounts: `ledger reg checking --real`

### Reporting over a Given Period

The `--period` (`-p`) command-line option will generate reports over a specific period of time, rather than the entire time encompassed by your journal. For a **register** report, only the transactions that satisfy the period expression will be displayed. For **balance** reports, only those transactions will be accounted for in the final balances.

A period expression is writting as `[INTERVAL] [BEGIN] [END]`, meaning it has three optional parts. The *INTERVAL* part may be any one of:

- every day
- every week
- every month
- every quarter
- every year
- every `N` days (where `N` is an integer)
- every `N` weeks
- every `N` months
- every `N` quarters
- every `N` years
- daily
- weekly
- biweekly (every two weeks)
- monthly
- bimonthly (every two months - irritatingly, there is no semi-monthly interval)
- quarterly
- yearly

After the interval, a *BEGIN* time, *END* time, both or neither may be specified. the *BEGIN* time may be one of:

- from `<SPEC>`
- since `<SPEC>`

The *END* time may be one of:

- to `<SPEC>`
- until `<SPEC>`

The `<SPEC>` part may be any one of the following:

- an explicit year like: `2016`
- a year and month: `2016/10`
- a year, month and day: `2016/10/1`
- a month and day (I think this assumes the current year): `10/1`
- the full name of a month: `october`
- the three-letter abbreviation for a month: `oct`
- the phrase `this week` (or day, month, quarter or year)
- the phrase `next week` (or day, month, quarter or year)
- the phrase `last week` (or day, month, quarter or year)

The beginning and ending can be given at the same time, if it spans a single period. In that case just use `<SPEC>` by itself. For example, `oct` will cover all the days in October. You can write just the `<SPEC>` value alone, or precede it by 'in', as in `in oct`.

Here are a few examples of period expressions:

- monthly
- monthly in 2014
- weekly from oct
- weekly from last month
- from sep to oct
- from 10/1 to 10/5
- monthly until 2015
- from 10/1 to 10/5
- monthly until 2016
- from apr
- until nov
- last oct
- weekly last august

## Tips
