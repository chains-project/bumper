```java
  import de.gwdg.metadataqa.api.json.JsonBranch;
  import de.gwdg.metadataqa.api.json.JsonBranchType;

  public class MarcFactory {
    public static JsonBranch createJsonBranch(String branch, JsonBranchType type) {
      return new JsonBranch(branch, type);
    }
  }
```