from miniomc import MinioadminMc

c = MinioadminMc(databasename="snadb")
value = c.getadmininfo()
print(value.info['pools'])