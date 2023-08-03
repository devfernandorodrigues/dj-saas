# A Django SaaS Boilerplate

### Techonologies

- Django
- Stripe
- Tailwind
- Postgres
- HTMX

## Starting

To start you need:

- A stripe account
- A product created in the Stripe account

First of all create your .env file and change the environment variables accordingly.

```bash
cp .env.example .env
```

After that you can build the containers

```bash
docker compose up -d --build
```

Get the webhook signing secret whsec\_ ...

```bash
docker compose logs -f stripe
```

```console
project-stripe-1  | Checking for new versions...
project-stripe-1  |
project-stripe-1  |
project-stripe-1  | A newer version of the Stripe CLI is available, please update to: v1.17.0
project-stripe-1  | Getting ready...
project-stripe-1  | Ready! Your webhook signing secret is whsec_...
```

Put the webhook secret in the .env file

```bash
DJSTRIPE_WEBHOOK_SECRET=wshec...
```

Down the containers

```bash
docker compose down
```

Up the containers again to have the .env file updated.

```bash
docker compose up -d
```

Now you'll need to migrate the database

```bash
docker compose exec app python manage.py migrate
```

Create your superuser

```bash
docker compose exec app python manage.py createsuperuser
```

Ok, now the last step is to create your api key in the database as suggested by the [Djstripe](https://dj-stripe.dev/api_keys/) documentation

After that you can sync your stripe account with Django.

```bash
docker compose exec app python manage.py djstripe_sync_models
```

That's it, access your [localhost](http://localhost:8000/) and try it 😄

## How it's working?

1. Create one account in the `Get started` button in [localhost](http://localhost:8000/)
2. Confirm your email, it's using the console email backend, so get the url in the console.

```bash
docker compose logs -f app
```

3. After you confirm your account, you'll be redirect to the plans page, select one plan.
4. In the checkout page, put the [testing card](https://stripe.com/docs/testing).
5. After the payment you'll be redirect to the success page and can see the dashboard page.

ℹ️ All events that occur in Striped are synced automatically through the webhook endpoint.
