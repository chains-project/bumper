```java
  import de.gwdg.metadataqa.api.json.JsonBranch;
  import de.gwdg.metadataqa.api.json.JsonBranch.JsonBranchBuilder;

  public class MarcFactory {

    public static JsonBranch createJsonBranch(String marcString) {
      JsonBranchBuilder builder = JsonBranch.builder();
      // ... code to build the JsonBranch from the MARC string ...
      return builder.build();
    }
  }
```