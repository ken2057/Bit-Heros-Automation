from const import LIST_COSTS
from ui.farm import ConfigUI, Farm
from ui.farm.utils import create_option_menu


class ExpeditionConfigUI(ConfigUI):
    def __init__(self, farm: Farm, parent, main) -> None:
        super().__init__(farm, parent, main)

    def _add_config_frames(self):
        self.zone = create_option_menu(self.root,
                                       data=self.farm.zones,
                                       value=self.farm.zone,
                                       name='zone')
        self.cost = create_option_menu(self.root,
                                       data=LIST_COSTS,
                                       value=self.farm.cost,
                                       name='cost')

    def _do_save_config(self):
        self.farm.cfg['cost'] = self.cost.get()
        self.farm.cfg['zone'] = self.zone.get()
