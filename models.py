from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Resource(Base):
  __tablename__ = "friendly_giggle_resources"


  id = Column(Integer, primary_key=True)
  title = Column(String)
  description = Column(String)
  category = Column(String)

  def __str__(self):
    return f"{self.title} ({self.category})"

