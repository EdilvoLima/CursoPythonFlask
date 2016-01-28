from app import db

class Produto(db.Model):
    __tablename__ = 'produto'
    IdProduto = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    value = db.Column(db.Float)

    Produto_vendas = db.relationship('ProdutoVenda', backref='produto')
    Produto_compras = db.relationship('ProdutoCompra', backref='produto')

    def __repr__(self):
        return '<Produto %r>' % self.name

    def __init__(self, name, value):
        self.name = name
        self.value = value

class Compra(db.Model):
    __tablename__ = 'compra'
    IdCompra = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)

    Compra_compras = db.relationship('ProdutoCompra', backref='compra')

    def __repr__(self):
        return '<Compra %r>' % self.IdCompra

    def __init__(self, date):
        self.date = date

class Venda(db.Model):
    __tablename__ = 'venda'
    IdVenda = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)

    Venda_vendas = db.relationship('ProdutoVenda', backref='venda')

    def __repr__(self):
        return '<Venda %r>' % self.IdVenda

    def __init__(self, date):
        self.date = date

class ProdutoVenda(db.Model):
    __tablename__ = 'produtoVenda'
    IdProdutoVenda = db.Column(db.Integer, primary_key=True)
    ProdutoVenda_IdProduto = db.Column(db.Integer, db.ForeignKey('produto.IdProduto'))
    ProdutoVenda_IdVenda = db.Column(db.Integer, db.ForeignKey('venda.IdVenda'))
    amount = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<ProdutoVenda %r>' % self.ProdutoVenda_IdVenda

    def __init__(self, ProdutoVenda_IdProduto, ProdutoVenda_IdVenda, amount):
        self.ProdutoVenda_IdProduto = ProdutoVenda_IdProduto
        self.ProdutoVenda_IdVenda = ProdutoVenda_IdVenda
        self.amount = amount

class ProdutoCompra(db.Model):
    __tablename__ = 'produtoCompra'
    IdProdutoCompra = db.Column(db.Integer, primary_key=True)
    ProdutoCompra_IdProduto = db.Column(db.Integer, db.ForeignKey('produto.IdProduto'))
    ProdutoCompra_IdCompra = db.Column(db.Integer, db.ForeignKey('compra.IdCompra'))
    amount = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<ProdutoCompra %r>' % self.ProdutoCompra_IdCompra

    def __init__(self, ProdutoCompra_IdProduto, ProdutoCompra_IdCompra, amount):
        self.ProdutoCompra_IdProduto = ProdutoCompra_IdProduto
        self.ProdutoCompra_IdCompra = ProdutoCompra_IdCompra
        self.amount = amount
