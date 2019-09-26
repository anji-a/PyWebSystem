from faker import Faker

fakegen = Faker()


def generate_key(**kwargs):
    prefix = fakegen.name()
    suffix = fakegen.name()
    id = fakegen.name()
    return prefix+"_"+id+"_"+suffix
