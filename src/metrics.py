from prometheus_client import Counter

cart_addition_total = Counter('eccomerce_cart_addition_total',
                               'Total de adições ao carrinho por produto',
                               ['product_id'])

errors_total = Counter(
    'eccomerce_errors_total',
    'Total de erros',
    ['error_type', 'endpoint', 'status_code']
)