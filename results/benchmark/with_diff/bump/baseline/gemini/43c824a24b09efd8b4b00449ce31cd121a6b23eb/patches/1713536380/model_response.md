```java
import de.gwdg.metadataqa.api.json.JsonBranch;

import java.util.List;

public class MarcFactory {

    public static JsonBranch createJsonBranch(String branchName, List<String> values) {
        JsonBranch jsonBranch = new JsonBranch();
        jsonBranch.setName(branchName);
        jsonBranch.setValues(values);
        return jsonBranch;
    }
}
```