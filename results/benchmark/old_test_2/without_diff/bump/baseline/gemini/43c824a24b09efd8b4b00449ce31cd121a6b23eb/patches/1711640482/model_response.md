```java
import de.gwdg.metadataqa.api.json.JsonBranch;
import org.apache.commons.lang3.StringUtils;

  public static JsonBranch getBranch(String id) {
    if (StringUtils.isBlank(id)) {
      return null;
    }
    return JsonBranch.findById(id);
  }
```