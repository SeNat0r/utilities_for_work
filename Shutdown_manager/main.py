from manager import storage

conn = storage.connect('base.db')
storage.initialize(conn)