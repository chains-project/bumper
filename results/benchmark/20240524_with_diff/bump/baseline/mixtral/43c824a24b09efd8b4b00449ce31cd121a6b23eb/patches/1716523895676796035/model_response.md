Here's the fixed version of the client code that should work with the new library version:
```java
import de.gwdg.metadataqa.api.json.DataElement;

// replace all occurrences of JsonBranch with DataElement
// for example, replace:
// JsonBranch jsonBranch = ...;
// with:
DataElement jsonBranch = ...;
```
The reason for this change is that the `JsonBranch` class has been removed in the new library version and replaced with the `DataElement` class. Therefore, we need to replace all occurrences of `JsonBranch` with `DataElement` in the client code.

Note that this change may require further modifications in the client code, depending on how heavily it relies on the `JsonBranch` class. For example, if the client code uses any of the removed methods of `JsonBranch`, it will need to be updated accordingly.