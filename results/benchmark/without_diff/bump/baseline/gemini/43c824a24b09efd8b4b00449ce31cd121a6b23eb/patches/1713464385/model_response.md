```java
import de.gwdg.metadataqa.api.json.JsonBranch;

public class MarcFactory {

    public static JsonBranch createJsonBranch(String branchName) {
        return new JsonBranch(branchName);
    }
}
```