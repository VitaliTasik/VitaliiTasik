import sqlite3

def initialize_database():
    conn = sqlite3.connect(r'C://Users/pozna/furry-waddle/VitaliiTasik' + r'/become_qa_auto.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        city TEXT,
        postalCode TEXT,
        country TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        quantity INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        order_date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    );
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO customers (id, name, address, city, postalCode, country) VALUES
    (1, 'Sergii', 'Maydan Nezalezhnosti 1', 'Kyiv', '3127', 'Ukraine'),
    (2, 'Stepan', 'Stepana Bandery str, 2', 'Kyiv', '3128', 'Ukraine');
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO products (id, name, description, quantity) VALUES
    (1, 'солодка вода', 'з цукром', 25),
    (2, 'молоко', 'без цукру', 10);
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO orders (id, customer_id, product_id, order_date) VALUES
    (1, 1, 1, '2023-06-08');
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
