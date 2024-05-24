```java
import de.gwdg.metadataqa.api.json.DataElement;

import java.util.List;

public class MarcFactory {

    public static DataElement createMarcDataElement(String path, String label, String jsonPath, boolean isMandatory, boolean isExtractable, boolean isCollection, boolean isActive, boolean hasFormat, String indexField, String solrFieldName, List<String> categories, Schema schema) {
        DataElement dataElement = new DataElement(path, label, jsonPath, isMandatory, isExtractable, isCollection, isActive, hasFormat, indexField, solrFieldName, categories);
        dataElement.setSchema(schema);
        return dataElement;
    }
}
```