```java
import de.gwdg.metadataqa.api.json.JsonBranch;

public class MarcFactory {

    public JsonBranch createJsonBranch(String name) {
        // Create a new JsonBranch object with the given name.
        JsonBranch branch = new JsonBranch(name);

        // Return the created JsonBranch object.
        return branch;
    }
}
```