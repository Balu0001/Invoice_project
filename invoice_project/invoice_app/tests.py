
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        data = {
            'date': '2023-09-24',
            'customer_name': 'Palthya Balu'
        }
        response = self.client.post('/api/invoices/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invoice_detail(self):
        invoice = Invoice.objects.create(date='2023-09-24', customer_name='Palthya Balu')
        data = {
            'invoice': invoice.id,
            'description': 'Invoice Description',
            'quantity': 2,
            'unit_price': '10.00',
            'price': '20.00'
        }
        response = self.client.post('/api/invoice-details/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


def test_update_invoice(self):
    invoice = Invoice.objects.create(date='2023-09-24', customer_name='Palthya Balu')
    new_data = {
        'date': '2023-09-25',
        'customer_name': 'Balu ',
    }
    response = self.client.put(f'/api/invoices/{invoice.id}/', new_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    invoice.refresh_from_db()
    self.assertEqual(invoice.date, new_data['date'])
    self.assertEqual(invoice.customer_name, new_data['customer_name'])

