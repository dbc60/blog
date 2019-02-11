---
layout: post
title: Budgeting
categories: projects
tags:
    - budgeting
    - planning
excerpt: How to spend money without going broke
---

## Contents
{:.no_toc}

- TOC
{:toc}

## File Organization
I'm going to keep a journal for expenses and budgeting. The journal shall be in a text file using the format [Ledger CLI](http://www.ledger-cli.org) needs for generating reports. See the [Ledger 3 docs](http://www.ledger-cli.org/3.0/doc/ledger3.html) for details.

I'm going to use two files. The first one, `cuthbertson-stavis-budget.dat` will keep the journal of daily expenses. The second one, `cuthbertson-stavis-accounts.dat` will declare the names of the actual accounts in play. It's supposed to help [keep the journal consistent](http://www.ledger-cli.org/3.0/doc/ledger3.html#Keeping-it-Consistent).

## The Five Budget Categories
I've made spreadsheets for budgets, but I don't seem to have any notes on the categories I used. I'm so disappointed. I was hoping to add them to my text-based expense journal.

I'm starting to learn how to use the ledger tool to create reports from a well structured text journal. The documentation suggests five major categories of expenses:

1. **Expenses**: where money goes,
1. **Assets**: where money sits (bank accounts, stock, mutual funds, investments),
1. **Income**: where money comes from (wages, tips),
1. **Liabilities**: money you owe (mortgage, auto loan, credit cards),
1. **Equity**: the real value of your property.

That's a good start. I have several categories and subcategories for expenses, but they are caught up in a spreadsheet somewhere on my home desktop.

I found my notes and [added them here](/projects/budget-design)!

### Tips for Structuring Accounts
One person recommends the following hierarchy for **Assets**, **Liabilities** and **Income**:

    Type : Country : Institution : Account : SubAccount

I don't think I need the country code (as in `Assets:US:ETrade:MSFT` or `Assets:CA:RBC:Checking`), as all my assets are in the US. I'll use the following hierarchy:

    Type : Institution : Account : SubAccount

Examples:

- Assets:BofA:Savings      ; Bank of America "Savings" account
- Assets:MetroCU:Checking  ; Metropolitan Credit Union checking account
- Assets:ETrade:Cash       ; The cash contents of the account
- Assets:ETrade:FB         ; Shares of Facebook
- Assets:ETrade:AAPL       ; Shares of Apple
- Assets:Some Bank:Roth IRA:2015   ; Roth IRA contributions for 2015
- Income:Acme:Wages ; Salary from ACME Corp.
- Income:ETrade:Interest    ; Interest income from cash deposits
- Income:ETrade:Dividends   ; Dividends received from this account
- Income:MetroCU:Savings:Interest   ; Interest received from savings

For **Expenses** accounts, there are no institutions. In this case it makes more sense to treat them as categories and just have a simple hierarchy that corresponds to the kinds of expenses they count. For example:

- Expenses:Pet Care                ; stuff and care for critters.
- Expenses:Services                ; accounting, laundry, legal, rentals.
    - Expenses:Services:Accounting
    - Expenses:Services:Laundry
- Expenses:Subscriptions           ; newspapers, magazines, memberships, professional dues.
    - Expenses:Subscriptions:Boston Globe
    - Expenses:Subscriptions:IEEE
    - Expenses:Subscriptions:DPMA   ; Dragon Phoenix Martial Arts
- Expenses:Taxes                   ; federal, state, local, property.
    - Expenses:Taxes:Federal:Income
    - Expenses:Taxes:State:MA:Income
    - Expenses:Taxes:Chelmsford:Property
    - Expenses:Taxes:State:MA:Excise

It is worth noting that the institution does not have to be a “real” institution. For instance, if you owned a condo unit in a building, you could use the **Loft4530** “institution” for all its related accounts:

- Assets:CA:Loft4530:Property
- Assets:CA:Loft4530:Association
- Income:CA:Loft4530:Rental
- Expenses:Loft4530:Acquisition:Legal
- Expenses:Loft4530:Acquisition:SaleAgent
- Expenses:Loft4530:Loan-Interest
- Expenses:Loft4530:Electricity
- Expenses:Loft4530:Insurance
- Expenses:Loft4530:Taxes:Municipal
- Expenses:Loft4530:Taxes:School

### Notes on Equity Accounts
You don't normally define many **Equity** accounts. These are mostly created to report the net income and currency conversions from previous years or the current exercise period on a balance sheet. Typically you will need at least one, and it doesn't matter much what you name it:

    Equity:Opening-Balances     ; Balances used to open accounts

You can customize the name of the other Equity accounts that get automatically created for the balance sheet.

When you first start your ledger, you will likely already have money in some of your accounts. Let’s say there’s $100 in your checking account; then add a transaction to your ledger to reflect this amount. Where will the money come from? The answer: your equity.

```ledger
10/2  Opening Balance
    Assets:Checking                         $100.00
    Equity:Opening Balances
```

**Example Transactions**:

```ledger
2016/09/30 * Paycheck
  Income:Acme Corp:Paycheck           $1000.00   ; paycheck from Acme Corp.
  Expenses:Taxes:State                 $100.00
  Expenses:Taxes:Federal               $250.00
  Expenses:Taxes:FICA                  $100.00
  Assets:Metro Credit Union:Checking
```

### Guidelines for Choosing an Account Type
First, if the amounts to be posted to the account are only relevant to be reported for a _period of time_, they should be one of the income statement accounts: **Income** or **Expenses**. On the other hand, if the amount _always_ needs to be included in the total balance of an account, then it should be a balance sheet account: **Assets** or **Liabilities**

Second, if the amounts are generally[^] positive, or "good from your perspective", the account should be either an **Assets** or an **Expenses** account. If the amounts are generally negative, or "bad from your perspective," the account should be either a **Liabilities** or an **Income** account.

### Expenses

These are all personal expenses. I might want to prefix them with `Personal` and use the `apply account` directive (e.g., `apply account Personal`) in my ledger file. This way I could have multiple account trees; `Personal`, `Business`, `Lynn's Trust` and others as needed.

1. Expenses:Donations               ; Charitable contributions.
    - Charitable
    - Religious
1. Expenses:Education               ; tuition, fees, books.
    - Tuition
    - Books & Supplies
    - Fees
1. Expenses:Entertainment           ; fun stuff.
    - Books, Videos, DVDs and other Media
    - Rentals
    - Tickets & Events (including Movies, Theater, Concerts, Plays, Sports, Hobbies, Outdoor Recreation, Toys, Games, and Gadgets).
1. Expenses:Food                    ; food, meals in and out.
    - Groceries
    - Coffee Shops
    - Fast Food
    - Restaurants
1. Expenses:General Fund            ; money not allocated to any other budget/expense-group. The value here initially represents net income. To allocate money to another budget/expense-group, transfer money from here to a (sub)group.
1. Expenses:Gifts                   ; gifts to family and friends.
1. Expenses:Goods & Merchandise     ; clothes, toys, stuff.
    - Clothing & Accessories
    - Computers & Electronics
    - Health & Beauty
    - General Merchandise
1. Expenses:Health & Lifestyle      ; barbers, doctors, fitness.
    - Doctor & Dentist
    - Medicine & Prescriptions
    - Medical Emergency
    - Vision Care (glasses, contact lenses, etc.)
    - Clubs, Gyms, Fitness
    - Salon/Barber
1. Expenses:Home                    ; furniture, lawn, garden.
    - Furnishings & Appliances
    - Lawn & Garden Supplies & Tools
    - Home Supplies & Tools
    - Maintenance & Repairs
    - Renovations & Improvements
1. Expenses:Insurance               ; auto, home, life.
    - Auto
    - Health
    - Life
1. Expenses:Pet Care                ; stuff and care for critters.
1. Expenses:Services                ; accounting, laundry, legal, rentals.
1. Expenses:Subscriptions           ; newspapers, magazines, memberships, professional dues.
1. Expenses:Taxes                   ; federal, state, local, property.
1. Expenses:Travel & Transportation ; parking, subway, train, plane, car rental (other than vacation).
1. Expenses:Utilities               ; gas, electric, phone, internet, water, sewage.
1. Expenses:Vacation                ; travel, lodging, entertainment, recreation.

### Assets

- Assets:Savings                 ; to the future!
- Reimbursements

### Income

- Income:Wages
- Income:Interest
- Income:Dividends
- Income:Gifts Received
- Income:Refunds

### Liabilities

1. Liabilities:Loans & Debts        : mortgage, credit cards, student loans.
- Morgage
- Second Mortgage
- Visa:USAA
- Visa:Citicorp
- Visa:Amazon

- Liabilities:Mortgage
- Liabilities:Second Mortgage
- Liabilities:Visa:Citicorp
- Liabilities:Visa:Amazon
- Liabilities:Visa:USAA
- Liabilities:Amex
- Liabilities:RetailCC:Kohls
- Liabilities:RetailCC:Lord & Taylor
- Liabilities:RetailCC:Macy's

### Equity

## Using Ledger
Here are some highlights from the documentation.

### Comments
A comment may begin anywhere on a line starting with a semicolon, ';'. The comment ends at the end of the line. If a comment starts at the beginning of a line it can start with one of five characters: ';', '#', '|', '*' or '%'.

Block comments start with `comment` at the beginning of the line. The body of the block comment follows on additional lines of text and ends with a single line containing `end comment`.

Transactions can have several forms of comments, most of which have special meaning. The global comment can start with any of the five comment characters and has no special meaning. Generally, comments in transactions look like:

```ledger
2011/12/11  Something Sweet
    ; German Chocolate Cake
    ; :Broke Diet:
    Expenses:Food               $10.00 ; Friends: The gang
    Assets:Credit Union:Checking
```

The first is a global comment and carries no special meaning. The other comments must start with a semicolon. The colon, '`:`' indicate meta-data and tags.

## Example Ledger File

```ledger
; -*- ledger -*-

= /^Income/
  (Liabilities:Tithe)                    0.12

;~ Monthly
;  Assets:Checking                     $500.00
;  Income:Salary

;~ Monthly
;   Expenses:Food  $100
;   Assets

2010/12/01 * Checking balance
  Assets:Checking                   $1000.00
  Equity:Opening Balances

2010/12/20 * Organic Co-op
  Expenses:Food:Groceries             $ 37.50  ; [=2011/01/01]
  Expenses:Food:Groceries             $ 37.50  ; [=2011/02/01]
  Expenses:Food:Groceries             $ 37.50  ; [=2011/03/01]
  Expenses:Food:Groceries             $ 37.50  ; [=2011/04/01]
  Expenses:Food:Groceries             $ 37.50  ; [=2011/05/01]
  Expenses:Food:Groceries             $ 37.50  ; [=2011/06/01]
  Assets:Checking                   $ -225.00

2010/12/28=2011/01/01 Acme Mortgage
  Liabilities:Mortgage:Principal    $  200.00
  Expenses:Interest:Mortgage        $  500.00
  Expenses:Escrow                   $  300.00
  Assets:Checking                  $ -1000.00

2011/01/02 Grocery Store
  Expenses:Food:Groceries             $ 65.00
  Assets:Checking

2011/01/05 Employer
  Assets:Checking                   $ 2000.00
  Income:Salary

2011/01/14 Bank
  ; Regular monthly savings transfer
  Assets:Savings                     $ 300.00
  Assets:Checking

2011/01/19 Grocery Store
  Expenses:Food:Groceries             $ 44.00 ; hastag: not block
  Assets:Checking

2011/01/25 Bank
  ; Transfer to cover car purchase
  Assets:Checking                  $ 5,500.00
  Assets:Savings
  ; :nobudget:

apply tag hastag: true
apply tag nestedtag: true
2011/01/25 Tom's Used Cars
  Expenses:Auto                    $ 5,500.00
  ; :nobudget:
  Assets:Checking

2011/01/27 Book Store
  Expenses:Books                       $20.00
  Liabilities:MasterCard
end tag
2011/12/01 Sale
  Assets:Checking:Business            $ 30.00
  Income:Sales
end tag
```
