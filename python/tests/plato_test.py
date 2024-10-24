import asyncio
from plato.plato_client import PlatoClient, PlatoConfig

async def test_plato_client_start_session():
  config = PlatoConfig(api_key="22493513-f909-4fef-8aaf-8af2c46dcf1c")
  session = PlatoClient.start_session(config)

  try:
    session.navigate("https://www.amazon.com")
    print("navigated")
    session.act("click the search bar")
    print("clicked the search bar")
    session.type("chocolate soylent [Enter]")
    print("typed in the search bar")
    session.act("click the first result")
    print("clicked the first result")
    session.act("click add to cart")
    print("clicked add to cart")

  except Exception as e:
    print(e)
  finally:
    session.end()


if __name__ == "__main__":
  asyncio.run(test_plato_client_start_session())
