from .dir import Directory
from .lib import CmdGroupMapping

groups: CmdGroupMapping = {
    "home": Directory("~/"),
}
