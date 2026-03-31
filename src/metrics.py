from prometheus_client import Counter, Gauge, Histogram
import psutil

cart_addition_total = Counter('eccomerce_cart_addition_total',
                               'Total de adições ao carrinho por produto',
                               ['product_id'])

errors_total = Counter(
    'eccomerce_errors_total',
    'Total de erros',
    ['error_type', 'endpoint', 'status_code']
)

active_sessions_gauge = Gauge('eccomerce_active_sessions', 'Número atual de sessões com carrinho ativo')

cpu_usage_gauge = Gauge('ecommerce_cpu_usage_percent', 'Percentual atual de uso de CPU do sistema')

def update_cpu_usage():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu_usage_gauge.set(cpu_usage)
        print(f"Atualização de uso de CPU: {cpu_usage}%")
    except Exception as e:
        print(f"Erro ao atualizar uso de CPU: {str(e)}")

def update_active_sessions():
    try:
        from models.order import Order
        active_count = Order.query.filter_by(is_open=True).count()
        active_sessions_gauge.set(active_count)
        print(f"Atualização de sessões: {active_count} sessões ativas")
    except Exception as e:
        print(f"Erro ao atualizar sessões ativas: {str(e)}")


request_duration_histogram = Histogram(
    'ecommerce_request_duration_seconds',
    'Tempo de resposta das requisições HTTP em segundos',
    ['method', 'endpoint', 'status_code'],
    buckets=(0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0)
)

