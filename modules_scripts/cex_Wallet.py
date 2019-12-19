import cexio


class better(cexio.Api):
    def get_cryptoaddres(self, crypto):
        return self.api_call('get_address', {'currency': crypto})


api = better('up126124749', '2wfEn7p2GTYGnrzMC3PsPlRPQ', 'SvAjvaXFhgKqEVEtcjTKwDZWjOw')


def get_adress(coin):
    return api.get_cryptoaddres(coin)['data']


