Here's a proposed patch for the failing client code:

```java
import de.gwdg.metadataqa.api.schema.json.JsonBranch;
```

Note that I replaced `de.gwdg.metadataqa.api.json` with `de.gwdg.metadataqa.api.schema.json` for the `JsonBranch` import. This is based on the assumption that the `JsonBranch` class has been moved to a new package in the updated library version.