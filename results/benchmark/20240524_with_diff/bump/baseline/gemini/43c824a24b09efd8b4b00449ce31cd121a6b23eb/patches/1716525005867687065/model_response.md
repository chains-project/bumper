```java
import de.gwdg.metadataqa.api.json.DataElement;

public class MarcFactory {

    public static DataElement createMarcElement(String label, String path) {
        return new DataElement(label, path);
    }
}
```