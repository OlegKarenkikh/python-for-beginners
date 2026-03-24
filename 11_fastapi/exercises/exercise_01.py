# Глава 11 — Упражнение
# Добавьте в API эндпоинт DELETE /clients/{client_id}
# который удаляет клиента из clients_db и возвращает:
# {"deleted": true, "id": <id>}  — если нашёл
# HTTP 404 — если не нашёл

# ПОДСКАЗКА:
# from fastapi import FastAPI, HTTPException
# @app.delete("/clients/{client_id}")
# def delete_client(client_id: int):
#     for i, c in enumerate(clients_db):
#         if c["id"] == client_id:
#             clients_db.pop(i)
#             return {"deleted": True, "id": client_id}
#     raise HTTPException(status_code=404, detail="Клиент не найден")

# Ваш код — допишите в 01_minimal_api.py:
