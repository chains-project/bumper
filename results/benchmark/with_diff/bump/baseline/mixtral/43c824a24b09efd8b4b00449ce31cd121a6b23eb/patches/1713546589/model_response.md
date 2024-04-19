Here's a proposed patch for the failing client code:

```java
import de.gwdg.metadataqa.api.schema.json.JsonBranch;
```

This patch imports the `JsonBranch` class from the updated package `de.gwdg.metadataqa.api.schema.json` instead of `de.gwdg.metadataqa.api.json`. The `schema` package has replaced the `json` package in the new library version.