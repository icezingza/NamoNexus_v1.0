class Manifest:
    VERSION = "1.0"
    CORE_VALUES = ["Compassion", "Wisdom", "Safety"]

    @classmethod
    def get_info(cls):
        return {"version": cls.VERSION, "values": cls.CORE_VALUES}
