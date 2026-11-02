# Food ordering cart (beginner example)

## Show your teacher

Run `python feature_cart.py`. It shows that a price of **100** becomes **90**
after a 10% discount. Then run `python -m pytest -q` to show the tests.
Explain it this way: multiply the price by the discount percentage, then
subtract that amount from the original price.

## Run the example and tests

```sh
python feature_cart.py
python -m pip install pytest
python -m pytest -q
```

The `total` function takes one price and a discount from 0% to 100%.

## Docker

```sh
docker build -t food-cart .
docker run --name food-cart-demo food-cart
docker ps -a
docker logs food-cart-demo
docker inspect food-cart-demo
docker rm food-cart-demo
```

This example is a command-line program, so it does not listen on a network port.
Port mapping is for web servers. To try a mapped port with the local login demo,
start it with `python login_demo.py`, then use `docker run -p 8000:8000 ...` only
after putting that web server in a container.

## Selenium login example

Install the packages in `requirements.txt`. Start `python login_demo.py` in one
terminal, then run `python selenium_login_test.py` in another. Selenium needs a
Chrome browser and a matching driver. The demo accepts `student` / `pizza123`.

## Jira stories to enter

Create a Scrum project named **Online Food Ordering** and add these stories:

| Story | Priority | Points | Suggested status |
|---|---|---:|---|
| As a customer, I want to browse the menu so I can choose food. | High | 3 | To Do |
| As a customer, I want to add food to my cart so I can order several items. | High | 5 | In Progress |
| As a customer, I want to place my order so the restaurant can prepare it. | Highest | 8 | To Do |

Create the project in Jira, choose the Scrum template, then add these as issues
and set priority, story points, and status on each issue. Jira requires your
account, so this repository only supplies the story plan.

## Git branch exercise

The repository's current branch is `main`. Make and merge the cart feature with:

```sh
git switch -c feature/cart
git add feature_cart.py test_feature_cart.py
git commit -m "Add cart total feature"
git switch main
git merge --no-ff feature/cart -m "Merge cart feature"
git log --oneline --graph --decorate -5
```

The GitHub Actions workflow in `.github/workflows/order-total.yml` runs when
changes are pushed to `main`. A real workflow result appears after pushing to
GitHub and opening the repository's Actions tab.
