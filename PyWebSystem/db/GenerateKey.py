from faker import Faker

fakegen = Faker()


def generate_key(**kwargs):
    prefix = kwargs.get("prefix", "")
    suffix = kwargs.get("suffix", "")
    if prefix == "":
        return fakegen.name()
    else:
        return prefix+"_"+suffix
