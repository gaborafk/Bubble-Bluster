
from plantuml import PlantUML

# URL des PlantUML-Servers
plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')

# PlantUML-Code
uml_code = """
@startuml
Alice -> Bob: Test
Bob -> Alice: Response
@enduml
"""

# Generiere das Diagramm und speichere es als PNG
plantuml.processes(uml_code)