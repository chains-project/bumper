```java
import de.gwdg.metadataqa.api.json.DataElement;

  import de.gwdg.metadataqa.api.json.JsonBranch;

public class MarcFactory {

    public static JsonBranch getMarcBranch(String identifier) {
        JsonBranch branch = new JsonBranch(identifier);
        branch.setIdentifier(new DataElement(identifier));
        return branch;
    }
}
```