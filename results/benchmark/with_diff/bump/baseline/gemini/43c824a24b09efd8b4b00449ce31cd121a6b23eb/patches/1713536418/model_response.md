```java
import de.gwdg.metadataqa.api.json.JsonBranch;

import java.util.List;

public class MarcFactory {

    public static JsonBranch createJsonBranch(String name, List<String> values) {
        JsonBranch branch = new JsonBranch();
        branch.setName(name);
        branch.setValues(values);
        return branch;
    }
}
```