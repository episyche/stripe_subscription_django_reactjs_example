from django.shortcuts import render
from rest_framework.views import APIView
import stripe
from django.conf import settings
from django.shortcuts import redirect
import json
from django.http import JsonResponse

FRONTEND_SUBSCRIPTION_SUCCESS_URL = settings.SUBSCRIPTION_SUCCESS_URL
FRONTEND_SUBSCRIPTION_CANCEL_URL = settings.SUBSCRIPTION_FAILED_URL

webhook_secret = settings.STRIPE_WEBHOOK_SECRET
stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateSubscription(APIView):
    def post(self , request):
        """
            This API creates a subscription .

            :return: redirect to payment page .
        """
        try:
            prices = stripe.Price.list(
                lookup_keys = [request.data['lookup_key']],
                expand=['data.product']
            )
            checkout_session = stripe.checkout.Session.create(
                line_items = [
                    {
                   'price' : prices.data[0].id,
                   'quantity' : 1
                    }
                ],
                mode = 'subscription',        
                success_url = FRONTEND_SUBSCRIPTION_SUCCESS_URL +"?session_id={CHECKOUT_SESSION_ID}",
                cancel_url = FRONTEND_SUBSCRIPTION_CANCEL_URL
            )
            return redirect(checkout_session.url , code=303)
        except Exception as err:
            raise err
            

class WebHook(APIView):
    def post(self , request):
        """
            This API handling the webhook .

            :return: returns event details as json response .
        """
        request_data = json.loads(request.body)
        if webhook_secret:
            # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
            signature = request.META['HTTP_STRIPE_SIGNATURE']
            try:
                event = stripe.Webhook.construct_event(
                    payload=request.body, 
                    sig_header=signature, 
                    secret=webhook_secret
                    )
                data = event['data']
            except ValueError as err:
                raise err
            except stripe.error.SignatureVerificationError as err:
                raise err
            # Get the type of webhook event sent - used to check the status of PaymentIntents.
            event_type = event['type']
        else:
            data = request_data['data']
            event_type = request_data['type']
        data_object = data['object']

        if event_type == 'checkout.session.completed':
        # Payment is successful and the subscription is created.
        # You should provision the subscription and save the customer ID to your database.
            print("-----checkout.session.completed----->",data['object']['customer'])
        elif event_type == 'invoice.paid':
        # Continue to provision the subscription as payments continue to be made.
        # Store the status in your database and check when a user accesses your service.
        # This approach helps you avoid hitting rate limits.
            print("-----invoice.paid----->", data)
        elif event_type == 'invoice.payment_failed':
        # The payment failed or the customer does not have a valid payment method.
        # The subscription becomes past_due. Notify your customer and send them to the
        # customer portal to update their payment information.
            print("-----invoice.payment_failed----->",data)
        else:
            print('Unhandled event type {}'.format(event_type))
        
        return JsonResponse(success=True, safe=False)