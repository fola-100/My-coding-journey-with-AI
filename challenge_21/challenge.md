Your Expense Manager v1
Challenge 1 — Expense Tracker (Design Phase)
Product Story

Your friend Yemi has a problem.

Yemi spends money every day but never knows where his money goes. At the end of the month he is always surprised by how much he spent.

He wants a simple command-line application that helps him track his expenses.

He wants to be able to:

Add a new expense

See all recorded expenses

See the total amount spent

Filter expenses by category (e.g., Food, Transport, Bills)

Save expenses so they are not lost when the program closes

He will run the program from the terminal like this:

python tracker.py

And interact with it using menu options.

Example:

1. Add expense
2. View expenses
3. Show total
4. Filter by category
5. Exit

SECOND CODING CHALLENGES
Project 2 — Expense Manager v2

We will extend your existing program with real product features.

New Features

1️⃣ Delete an expense

User can remove a saved expense.

Example:

1 | food | 500 | lunch | 2026-03-17
2 | transport | 200 | taxi | 2026-03-17

User enters:

Delete expense #: 2

Expense gets removed from JSON.

2️⃣ Edit an expense

User can modify a saved record.

Example:

Edit expense #: 1

User chooses field to change.

3️⃣ Monthly summary

Example:

Month: 2026-03
Total spent: 4500

Optional advanced version:

Food: 2000
Transport: 1500
Bills: 1000

4️⃣ Pretty printing expenses

Instead of this:

[{'expense_amount': 500, ...}]

You show:

ID | CATEGORY | AMOUNT | DATE | DESCRIPTION
------------------------------------------------
1  | food     | 500    | 2026-03-17 | lunch
2  | transport| 200    | 2026-03-17 | taxi

5️⃣ Expense IDs

Instead of relying on list position implicitly, we show the index as ID.


