class URLDataStore(object):
  # Singleton Data Store
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(URLDataStore, cls).__new__(cls)
      cls.redis = None
      cls.mongoDb = None
    return cls.instance