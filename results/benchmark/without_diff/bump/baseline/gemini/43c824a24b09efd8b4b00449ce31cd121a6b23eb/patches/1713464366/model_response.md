```java
import de.gwdg.metadataqa.api.json.JsonBranch;

public class MarcFactory {

    public static JsonBranch createJsonBranch(String branchName) {
        // Create a new JsonBranch object with the given branch name.
        JsonBranch jsonBranch = new JsonBranch(branchName);

        // Return the created JsonBranch object.
        return jsonBranch;
    }
}
```