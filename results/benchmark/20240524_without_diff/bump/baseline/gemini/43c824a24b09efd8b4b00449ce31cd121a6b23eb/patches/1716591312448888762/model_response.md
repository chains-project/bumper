```java
import de.gwdg.metadataqa.api.json.JsonBranch;

import java.util.List;
import java.util.stream.Collectors;

public class MarcFactory {

    public static List<JsonBranch> createJsonBranches(List<String> marcRecords) {
        return marcRecords.stream()
                .map(MarcFactory::createJsonBranch)
                .collect(Collectors.toList());
    }

    private static JsonBranch createJsonBranch(String marcRecord) {
        // TODO: Implement logic to create a JsonBranch from a MARC record
        return null;
    }
}
```