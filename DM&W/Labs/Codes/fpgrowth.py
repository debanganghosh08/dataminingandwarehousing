from collections import defaultdict

# FP-Tree Node class
class FPNode:
    def __init__(self, item, count, parent):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = {}
        self.next_node = None

# FP-Tree Class
class FPTree:
    def __init__(self, transactions, min_support):
        self.min_support = min_support
        self.header_table = {}
        self.root = FPNode(None, 1, None)
        self.build_tree(transactions)

    # Step 1: Count item frequencies and remove infrequent items
    def find_frequent_items(self, transactions):
        item_counts = defaultdict(int)
        for transaction in transactions:
            for item in transaction:
                item_counts[item] += 1
        return {k: v for k, v in item_counts.items() if v >= self.min_support}

    # Step 2: Build FP-Tree
    def build_tree(self, transactions):
        frequent_items = self.find_frequent_items(transactions)

        # Sort transactions by frequency order
        ordered_transactions = []
        for transaction in transactions:
            ordered_transaction = [item for item in transaction if item in frequent_items]
            ordered_transaction.sort(key=lambda x: frequent_items[x], reverse=True)
            ordered_transactions.append(ordered_transaction)

        # Insert transactions into FP-tree
        for transaction in ordered_transactions:
            self.insert_transaction(transaction, self.root)

    # Step 3: Insert transaction into tree
    def insert_transaction(self, transaction, node):
        if len(transaction) == 0:
            return
        first_item = transaction[0]
        if first_item in node.children:
            node.children[first_item].count += 1
        else:
            node.children[first_item] = FPNode(first_item, 1, node)
            if first_item in self.header_table:
                self.link_nodes(first_item, node.children[first_item])
            else:
                self.header_table[first_item] = node.children[first_item]

        self.insert_transaction(transaction[1:], node.children[first_item])

    # Step 4: Link nodes in the header table
    def link_nodes(self, item, new_node):
        current_node = self.header_table[item]
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node

    # Step 5: Extract conditional pattern base
    def find_conditional_pattern_base(self, item):
        base_patterns = []
        node = self.header_table[item]
        while node:
            path = []
            parent = node.parent
            while parent and parent.item:
                path.append(parent.item)
                parent = parent.parent
            for _ in range(node.count):
                base_patterns.append(path)
            node = node.next_node
        return base_patterns

    # Step 6: Extract frequent itemsets recursively
    def mine_tree(self, prefix, frequent_patterns):
        for item in sorted(self.header_table, key=lambda x: self.header_table[x].count):
            new_prefix = prefix.copy()
            new_prefix.append(item)
            frequent_patterns.append(new_prefix)

            # Find conditional pattern base
            conditional_pattern_base = self.find_conditional_pattern_base(item)
            conditional_tree = FPTree(conditional_pattern_base, self.min_support)
            conditional_tree.mine_tree(new_prefix, frequent_patterns)

# Step 7: FP-Growth Algorithm function
def fp_growth(transactions, min_support):
    fp_tree = FPTree(transactions, min_support)
    frequent_patterns = []
    fp_tree.mine_tree([], frequent_patterns)
    return frequent_patterns

# Example Dataset (List of Transactions)
transactions = [
    ['bread', 'milk'],
    ['bread', 'diaper', 'beer', 'eggs'],
    ['milk', 'diaper', 'beer', 'coke'],
    ['bread', 'milk', 'diaper', 'beer'],
    ['bread', 'milk', 'diaper', 'coke']
]

# Set Minimum Support Threshold
min_support = 2

# Run FP-Growth Algorithm
frequent_itemsets = fp_growth(transactions, min_support)

# Print Frequent Itemsets
print("Frequent Itemsets:")
for itemset in frequent_itemsets:
    print(itemset)
