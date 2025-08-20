Steps to reproduce:
1. Run `docker compose up`
2. You can use already downloaded data or run `docker compose run freqtrade_dev2 freqtrade download-data --timerange=20230101-20250707`
3. Run ` docker compose run freqtrade_dev2 freqtrade recursive-analysis --config /freqtrade/user_data/config.json --strategy MyStrategy --timerange=20250101-20250820`
