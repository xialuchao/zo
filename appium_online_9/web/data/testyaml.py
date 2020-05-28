import yaml
def testyaml():
    with open("get_driver.yaml") as f:
        k = f.read()
    a = yaml.load(k, Loader=yaml.FullLoader)
    for i in a["drivers"]:
        print(i)


testyaml()