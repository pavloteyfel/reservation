from fastapi import APIRouter
from hotel.operations.customers import (
    CustomerCreateData,
    CustomerUpdateData,
    read_all_customers,
    update_customer,
    read_customer,
    create_customer,
    update_customer,
)

router = APIRouter()


@router.get("/customers")
def api_read_all_customers():
    return read_all_customers()


@router.get("/customers/{customer_id}")
def api_read_customers(customer_id: int):
    return read_customer(customer_id)


@router.post("/customers")
def api_create_customer(customer: CustomerCreateData):
    return create_customer(customer)


@router.patch("/customers/{customer_id}")
def api_update_customer(customer_id: int, customer: CustomerUpdateData):
    return update_customer(customer_id, customer)
