class Expense:
    def __init__(self,name,category,amount):
        self.name=name
        self.category=category
        self.amount=amount
    def __repr__(self):
        return f'<repr fun> name={self.name},category={self.category},amount={self.amount:.2f}' #2f only return 2 decemal part


