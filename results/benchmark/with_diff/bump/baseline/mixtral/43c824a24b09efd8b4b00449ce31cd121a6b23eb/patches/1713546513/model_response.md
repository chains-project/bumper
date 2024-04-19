Here's a proposed patch for the failing client code:

```java
import de.gwdg.metadataqa.jsonld.JsonBranch;
```

The failure is caused by a breaking change in the library, where the `JsonBranch` class has been moved from the `de.gwdg.metadataqa.api.json` package to the `de.gwdg.metadataqa.jsonld` package. By changing the import statement to import `JsonBranch` from the new package, the code should compile successfully.