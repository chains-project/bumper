Here's a proposed patch for the failing client code:

```java
import de.gwdg.metadataqa.api.schema.common.json.JsonBranch;
```

The `JsonBranch` class has been moved to a different package in the new library version, so we need to update the import statement accordingly.