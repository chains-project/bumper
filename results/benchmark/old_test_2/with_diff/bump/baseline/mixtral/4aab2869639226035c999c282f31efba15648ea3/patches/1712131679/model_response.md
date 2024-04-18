Sure, based on the information provided, it seems that the `Storages` class has been removed and replaced with `StoragesLoader`. Here's a possible patch that you can apply to the code:
```java
import com.artipie.asto.factory.StoragesLoader;

// ...

StoragesLoader storagesLoader = new StoragesLoader();