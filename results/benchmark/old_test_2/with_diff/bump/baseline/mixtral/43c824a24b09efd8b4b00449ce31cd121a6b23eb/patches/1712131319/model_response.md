Here's a proposed patch for the failing client code:
```java
import de.gwdg.metadataqa.api.schema.json.JsonBranch;
```
Note that I replaced `de.gwdg.metadataqa.api.json.JsonBranch` with `de.gwdg.metadataqa.api.schema.json.JsonBranch`. It seems that the `JsonBranch` class has been moved to a different package in the new library version.