Here's the proposed patch for the failing client code:

```java
import de.gwdg.metadataqa.api.schema.json.JsonBranch;
```

Note that the package name has changed from `de.gwdg.metadataqa.api.json` to `de.gwdg.metadataqa.api.schema.json`. This is because the `JsonBranch` class has been moved to a different package in the new library version.