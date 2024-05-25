Here is a patch that you can apply to the code:
```java
import com.artipie.asto.factory.Storages;
import com.artipie.asto.memory.InMemoryStorage;

@Override
public Storage storage() {
    return Storages.single(new InMemoryStorage());
}
```
This patch creates a new `InMemoryStorage` object and wraps it in a `SingleStorage` object using the `Storages.single` method. This object is then returned by the `storage` method.

Note: This patch assumes that the `Storage` and `InMemoryStorage` classes are still available in the updated version of the external dependency. If these classes have been removed, you will need to find a different solution.