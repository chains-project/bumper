```java
import de.gwdg.metadataqa.api.json.JsonBranch;

import java.util.List;
import java.util.stream.Collectors;

public class MarcFactory {

    public static List<JsonBranch> createJsonBranches(List<String> branches) {
        return branches.stream()
                .map(JsonBranch::new)
                .collect(Collectors.toList());
    }
}
```