from typing import Dict, Optional


class ROISelectorProperties:
    def __init__(self, properties: Optional[Dict[str, str]] = None) -> None:
        if properties is None:
            self.properties: Dict[str, str] = {}
        else:
            self.properties: Dict[str, str] = properties

    def set_property(self, name: str, value: str) -> None:
        self.properties[name]: Dict[str, str] = value

    def get_property(self, name: str) -> str:
        return self.properties[name]

    def remove_property(self, name: str) -> None:
        del self.properties[name]
