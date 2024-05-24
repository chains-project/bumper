Here's the proposed patch for the client code:
```java
import de.gwdg.metadataqa.api.json.DataElement;

// replace all occurrences of JsonBranch with DataElement
// example:
//     old: JsonBranch branch = ...
//     new: DataElement branch = ...
```
The reason for this change is that the `JsonBranch` class has been removed and replaced with the `DataElement` class in the new library version.