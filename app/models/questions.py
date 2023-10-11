from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.db.base_class import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    answer = Column(String)
    created_at = Column(DateTime)
    add_date = Column(DateTime, default=datetime.now)
    pull_questions_id = Column(ForeignKey("pullquestions.id"))
    pull_questions = relationship("PullQuestions", backref="questions")

    def __repr__(self):
        return f'{self.__class__.__name__}(id: {self.id} pull_questions: {self.pull_questions_id})'


class PullQuestions(Base):
    __tablename__ = "pullquestions"

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f'{self.__class__.__name__}(id: {self.id})'

