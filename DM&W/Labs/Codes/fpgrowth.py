from collections import defaultdict

#we are taking tree structure for FP growth algorithm tree
#class for FP-Tree Node
class Node:
    def __init__(self, item, count, parent):
        self.item = item  
        self.count = count  
        self.parent = parent  
        self.children = {}  
        self.next = None  

#Class for FP-Tree structure
class FPTree:
    def __init__(self, transactions, min_support):
        self.min_support = min_support  
        self.header = {}  
        self.root = Node(None, 1, None)  
        self.support_count = defaultdict(int)  
        self.build_tree(transactions)  

    #counting frequency of items to filter low support ones
    def get_frequent_items(self, transactions):
        item_counts = defaultdict(int)
        for transaction in transactions:
            for item in transaction:
                item_counts[item] += 1  
        return {k: v for k, v in item_counts.items() if v >= self.min_support}  

    #FP-Tree construction
    def build_tree(self, transactions):
        freq_items = self.get_frequent_items(transactions)

        # Reordering transactions based on item frequency
        ordered_transactions = []
        for transaction in transactions:
            sorted_transaction = [item for item in transaction if item in freq_items]
            sorted_transaction.sort(key=lambda x: freq_items[x], reverse=True)
            ordered_transactions.append(sorted_transaction)

        #insert them into the FP-tree
        for transaction in ordered_transactions:
            self.insert_node(transaction, self.root)

    #insert transactions into the FP-Tree
    def insert_node(self, transaction, node):
        if not transaction:
            return  

        first_item = transaction[0]  
        if first_item in node.children:
            node.children[first_item].count += 1  
        else:
            node.children[first_item] = Node(first_item, 1, node)  
            if first_item in self.header:
                self.link_nodes(first_item, node.children[first_item])  
            else:
                self.header[first_item] = node.children[first_item]  

        self.insert_node(transaction[1:], node.children[first_item])  

    #link nodes of same item in different paths
    def link_nodes(self, item, new_node):
        current = self.header[item]
        while current.next:
            current = current.next  
        current.next = new_node  

    #find conditional pattern bases
    def get_pattern_base(self, item):
        patterns = []  
        node = self.header[item]  
        while node:
            path = []  
            parent = node.parent  
            while parent and parent.item:
                path.append(parent.item)  
                parent = parent.parent  
            for _ in range(node.count):
                patterns.append(path)  
            node = node.next  
        return patterns  

    # min tree recursively
    def mine_patterns(self, prefix, freq_patterns):
        for item in sorted(self.header, key=lambda x: self.header[x].count):
            new_prefix = prefix.copy()  
            new_prefix.append(item)  
            support = self.header[item].count  
            freq_patterns.append((new_prefix, support))  
            self.support_count[tuple(new_prefix)] = support  

            # conditional tree construction 
            conditional_base = self.get_pattern_base(item)  
            conditional_tree = FPTree(conditional_base, self.min_support)  
            conditional_tree.mine_patterns(new_prefix, freq_patterns)  

#start FP-Growth process
def fp_growth(transactions, min_support):
    tree = FPTree(transactions, min_support)  
    freq_patterns = []  
    tree.mine_patterns([], freq_patterns)  
    return freq_patterns  

#print the final frequent patterns
def show_patterns(freq_patterns):
    print("\nFrequent Itemsets with Support:")
    for pattern, support in freq_patterns:
        print(f"{pattern} -> Support: {support}")  

# dataset for sample
transactions = [
    ['milk', 'bread', 'butter'],
    ['milk', 'chocolate', 'energy drink', 'bread'],
    ['milk', 'bread', 'chocolate', 'coke'],
    ['milk', 'bread', 'butter', 'eggs'],
    ['chocolate', 'energy drink', 'coke'],
    ['milk', 'bread', 'butter', 'cereal'],
    ['bread', 'butter', 'jam', 'tea'],
    ['bread', 'chocolate', 'energy drink'],
    ['milk', 'bread', 'butter', 'coffee'],
    ['bread', 'eggs', 'butter'],
    ['milk', 'bread', 'butter', 'chocolate'],
    ['milk', 'bread', 'butter', 'jam'],
    ['milk', 'cereal', 'juice'],
    ['bread', 'butter', 'coffee'],
    ['bread', 'chocolate', 'energy drink', 'milk'],
    ['milk', 'bread', 'butter', 'jam'],
    ['chocolate', 'energy drink', 'coke', 'chips'],
    ['milk', 'bread', 'butter', 'eggs'],
    ['bread', 'butter', 'coffee'],
    ['chocolate', 'energy drink', 'chips', 'soda'],
    ['milk', 'cereal', 'juice'],
    ['bread', 'butter', 'eggs'],
    ['milk', 'chocolate', 'energy drink', 'bread'],
    ['milk', 'bread', 'butter', 'jam'],
    ['chocolate', 'energy drink', 'coke', 'chips'],
    ['milk', 'bread', 'butter', 'eggs'],
    ['milk', 'bread', 'butter', 'jam'],
    ['chocolate', 'energy drink', 'coke', 'chips'],
    ['bread', 'butter', 'tea'],
    ['milk', 'bread', 'butter', 'eggs'],
    ['bread', 'butter', 'jam'],
    ['chocolate', 'energy drink', 'coke'],
    ['bread', 'butter', 'eggs'],
    ['milk', 'bread', 'butter'],
    ['chocolate', 'energy drink', 'chips'],
    ['milk', 'bread', 'butter', 'jam'],
    ['chocolate', 'energy drink', 'coke', 'chips'],
    ['milk', 'bread', 'butter', 'eggs'],
    ['bread', 'butter', 'coffee'],
    ['milk', 'bread', 'butter', 'jam'],
    ['chocolate', 'energy drink', 'coke', 'chips'],
    ['milk', 'bread', 'butter', 'cereal'],
    ['bread', 'butter', 'jam', 'tea'],
    ['bread', 'chocolate', 'energy drink'],
    ['milk', 'bread', 'butter', 'coffee'],
    ['bread', 'eggs', 'butter'],
    ['milk', 'bread', 'butter', 'chocolate'],
    ['milk', 'bread', 'butter', 'jam'],
    ['milk', 'cereal', 'juice'],
    ['bread', 'butter', 'coffee'],
]

# minimum support threshold
min_support = 5  

# FP-Growth algorithm
frequent_itemsets = fp_growth(transactions, min_support)

# results
show_patterns(frequent_itemsets)
