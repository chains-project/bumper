```java
import de.gwdg.metadataqa.api.json.DataElement;

import java.util.List;

public class MarcFactory {

    public static List<DataElement> createMarcFactory(List<DataElement> dataElements) {
        for (DataElement dataElement : dataElements) {
            if (dataElement.getLabel().equals("leader")) {
                dataElement.setCategories(List.of("leader"));
                dataElement.setExtractable(false);
                dataElement.setMandatory(true);
            } else if (dataElement.getLabel().equals("controlfield")) {
                dataElement.setCategories(List.of("controlfield"));
                dataElement.setExtractable(false);
                dataElement.setMandatory(true);
            } else if (dataElement.getLabel().equals("datafield")) {
                dataElement.setCategories(List.of("datafield"));
                dataElement.setExtractable(true);
                dataElement.setMandatory(true);
            }
        }
        return dataElements;
    }
}
```