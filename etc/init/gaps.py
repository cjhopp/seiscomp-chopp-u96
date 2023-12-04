import seiscomp.kernel
import seiscomp.config
import seiscomp.system


class Module(seiscomp.kernel.Module):
    def __init__(self, env):
        seiscomp.kernel.Module.__init__(self, env, env.moduleName(__file__))

        cfg = seiscomp.config.Config()

        env = seiscomp.system.Environment.Instance()
        env.initConfig(cfg, self.name)

        try:
            self.authbind = cfg.getBool("authbind")
        except Exception:
            self.authbind = False

    def supportsAliases(self):
        # The default handler does not support aliases
        return True

    def updateConfigProxy(self):
        return "trunk"

    ## Uncomment for authbind (running service on privileged ports)
    def _run(self):
        if self.authbind:
            params = (
                "--depth 2 "
                + self.env.binaryFile(self.name)
                + " "
                + self._get_start_params()
            )
            binaryPath = "authbind"
            return self.env.start(self.name, binaryPath, params)

        return seiscomp.kernel.Module._run(self)
