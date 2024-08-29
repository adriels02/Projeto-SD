from django.http import JsonResponse
from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.db.utils import OperationalError

def status_check(request):
    status = {
        "database": "Unknown",
        "migrations_pending": "Unknown",
        "status": "OK"
    }

    # Verificação da Conexão com o Banco de Dados
    try:
        connection.ensure_connection()
        status["database"] = "Connected"
    except OperationalError:
        status["database"] = "Not Connected"
        status["status"] = "ERROR"

    # Verificação de Migrações Pendentes
    try:
        executor = MigrationExecutor(connection)
        targets = executor.loader.graph.leaf_nodes()
        status["migrations_pending"] = "No Pending Migrations" if not executor.migration_plan(targets) else "Pending Migrations"
    except Exception as e:
        status["migrations_pending"] = f"Error: {str(e)}"
        status["status"] = "ERROR"

    return JsonResponse(status)