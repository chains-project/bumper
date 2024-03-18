As the error message indicates that the class LengthOf cannot be found in the package org.cactoos.iterable, it means that the class LengthOf may have been moved to a different package in the new version of the library. Without the information about the new package structure, it's impossible to propose a specific patch. However, a general solution would be to import the LengthOf class from its new package. 

Here is an example:

```java
import org.cactoos.collection.LengthOf;
```

Please replace "collection" with the correct package where the LengthOf class is now located in the new version of the library.