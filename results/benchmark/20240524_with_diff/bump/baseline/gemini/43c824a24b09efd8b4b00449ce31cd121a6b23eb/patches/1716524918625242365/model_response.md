```java
import de.gwdg.metadataqa.api.json.DataElement;

public void de.gwdg.metadataqa.marc.MarcFactory.evaluateJsonBranch(DataElement branch, de.gwdg.metadataqa.api.model.pathcache.PathCache pathCache, de.gwdg.metadataqa.api.counter.CompletenessCounter counter, java.lang.String path, java.lang.Object value) {
    // ...
    
    // Get the record ID from the schema.
    DataElement recordId = schema.getRecordId();
    
    // ...
}
```