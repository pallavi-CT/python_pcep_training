from collections import defaultdict

raw_transactions = [
    {"date": "2024-01-15", "agent": "  ALICE  ",  "region": "north", "amount": "₹12500"},
    {"date": "2024-01-16", "agent": "BOB",       "region": "SOUTH", "amount": "₹8900"},
    {"date": "2024-01-16", "agent": "alice",     "region": "North", "amount": "N/A"},
    {"date": "2024-01-17", "agent": "  charlie", "region": "east",  "amount": "₹21000"},
    {"date": "2024-01-17", "agent": "BOB",       "region": "south", "amount": "₹15500"},
    {"date": "2024-01-18", "agent": "CHARLIE",   "region": "East",  "amount": "₹9800"},
]

# step 1: clean the data
clean_tranx = []
for txn in raw_transactions:
    amt_str = txn['amount'].strip()
    # amt = amt_str[1:]
    if amt_str == 'N/A':
        print(f"Skipping Invalid Record: {txn}")
    else:    
        clean_tranx.append(
            {
                'date': txn.get('date'),
                'agent': txn.get('agent').strip().title(),
                'region': txn.get('region').strip().title(),
                'amount': int(amt_str[1:])
            }
        )
    

#step 2: analyse the data
agent_sales = defaultdict(int)

for txn in clean_tranx:
    agent_sales[txn['agent']] += txn['amount']   # Bob: 34500

regions = {txn['region'] for txn in clean_tranx}
print(f"Active Regions: {regions}")

#step 3: report it
report = sorted(agent_sales.items(), key=lambda x:x[1], reverse=True)
total_sales = sum(agent_sales.values())

print("-" * 40)
print("Sales Report")
print("-" * 40)
print(f"{'Rank':<6}{'Agent':<12}{'Sales':>10}{'Share':>10}")
print("-" * 40)
for rank, (agent, sales) in enumerate(report, 1):
    amt = sales/total_sales
    pos = ["1st", "2nd", "3rd"][rank-1] if rank <= 3 else print(f"#{rank}")
    print(f"{pos:<6}{agent:<12}{sales:>8,}{amt:>9.1%}")

print("-" * 40)
print(f"Total Sales: {total_sales}")