from gdo.core.GDT_String import GDT_String
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm


class genome(MethodForm):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_String('genome'),
        )
        super().gdo_create_form(form)

    def new_genome(self) -> str:
        return self.param_val('genome')

    def form_submitted(self):
        if genome := self.new_genome():
            self.save_genome(genome)

    def save_genome(self, genome):
        pass

