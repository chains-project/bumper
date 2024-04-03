Here's a proposed patch for the failing client code:
```java
import de.gwdg.metadataqa.api.schema.json.JsonBranch;
```
Note that I changed the import statement to reference `JsonBranch` in the `de.gwdg.metadataqa.api.schema.json` package instead of `de.gwdg.metadataqa.api.json`. Based on the library changes you provided, it looks like `JsonBranch` was moved to a new location in the updated library version.