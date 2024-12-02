from typing import List 
from app.models.user_model  import User
from app.models.todo_model import Todo
from app.schemas.todo_schema import TodoCreate, TodoUpdate
from uuid import UUID


class TodoService:
    @staticmethod 
    async def list_todos(user: User) -> List[Todo]:
        todos = await Todo.find(Todo.owner.id == user.id).to_list()
        return todos
    
    @staticmethod
    async def create( user: User, data: TodoCreate) -> Todo:
        todo = Todo(**data.dict(), owner = user)
        return await todo.insert()
    
    @staticmethod
    async def retrieve( user: User, todi_id: UUID):
        todo = Todo.find_one(Todo.todo_id == todi_id, Todo.owner.id == user.id)
        print(todo)
        return todo
    
    @staticmethod
    async def update_todo( user: User, todo_id: UUID, data: TodoUpdate) -> Todo:
        todo = await TodoService.retrieve(user, todo_id)
        await todo.update({"$set": data.dict(exclude_unset = True)})
        await todo.save()
        return todo
    
    @staticmethod
    async def delete_todo( user: User, todo_id: UUID) -> Todo:
        todo = await TodoService.retrieve(user, todo_id)
        if todo:
            await todo.delete()
        return None
        