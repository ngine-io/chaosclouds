from chaotic.cloud.cloudscale_ch import CloudscaleChChaotic
from chaotic.cloud.nomad import NomadChaotic

class ChaoticFactory:

    CLOUD_CLASSES: dict = {
        'cloudscale_ch': CloudscaleChChaotic,
        'nomad': NomadChaotic,
    }

    def get_instance(self, name: str) -> object:
        try:
            obj_class = self.CLOUD_CLASSES[name]
            return obj_class()
        except KeyError as e:
            msg = f"{e} not implemented"
            raise NotImplementedError(msg)
