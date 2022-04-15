from ast import arguments
from email.headerregistry import Address
from utils import Signer, uint, str_to_felt
from nile import deployments

# TODO: ADD TO ENV ON LOAD
NETWORK = "goerli"

def run(nre):
    admin, abi = next(deployments.load("admin", NETWORK))

    arbiter, abi = next(deployments.load("arbiter", NETWORK))
    controller, abi = next(deployments.load("moduleController", NETWORK))

    admin, abi = next(deployments.load("admin", NETWORK))
    lords, abi = next(deployments.load("lords", NETWORK))
    realms, abi = next(deployments.load("realms", NETWORK))
    resources, abi = next(deployments.load("resources", NETWORK))
    s_realms, abi = next(deployments.load("s_realms", NETWORK))

    L01_Settling, abi = next(deployments.load("L01_Settling", NETWORK))
    S01_Settling, abi = next(deployments.load("S01_Settling", NETWORK))
    L02_Resources, abi = next(deployments.load("L02_Resources", NETWORK))
    S02_Resources, abi = next(deployments.load("S02_Resources", NETWORK))
    L03_Buildings, abi = next(deployments.load("L03_Buildings", NETWORK))
    S03_Buildings, abi = next(deployments.load("S03_Buildings", NETWORK))
    L04_Calculator, abi = next(deployments.load("L04_Calculator", NETWORK))
    L05_Wonders, abi = next(deployments.load("L05_Wonders", NETWORK))
    S05_Wonders, abi = next(deployments.load("S05_Wonders", NETWORK))

    # set module access within realms access
    settle = nre.invoke(
        L01_Settling,
        'settle',
        params=["1", "0"],
    )

    print(settle)