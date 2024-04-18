```java
import de.gwdg.metadataqa.api.json.JsonBranch;

public class MarcFactory {

    public static JsonBranch createJsonBranch(String name, String description) {
        JsonBranch jsonBranch = new JsonBranch();
        jsonBranch.setName(name);
        jsonBranch.setDescription(description);
        return jsonBranch;
    }
}
```