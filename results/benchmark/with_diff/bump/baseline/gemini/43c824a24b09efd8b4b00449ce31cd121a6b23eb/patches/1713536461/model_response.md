```java
import de.gwdg.metadataqa.api.json.JsonBranch;

public class MarcFactory {

    public JsonBranch createJsonBranch(String branchName) {
        return new JsonBranch(branchName);
    }
}
```