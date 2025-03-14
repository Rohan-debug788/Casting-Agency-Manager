from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# Role model
class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Relationship with Auditions
    auditions = relationship('Audition', back_populates='role')

# Audition model
class Audition(Base):
    __tablename__ = 'auditions'
    
    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    
    # Relationship back to Role
    role = relationship('Role', back_populates='auditions')
