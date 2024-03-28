Here's a proposed patch to fix the failing client code:
```java
import org.yaml.snakeyaml.inspector.TrustedTagInspector;

public class TrustedTagInspectorWrapper {
    private static final TrustedTagInspector inspector = new TrustedTagInspector();

    public static boolean isGlobalTagAllowed(Tag tag) {
        return inspector.isGlobalTagAllowed(tag);
    }
}
```
Then, replace the failing line with the following:
```java
import static com.premiumminds.billy.core.test.TrustedTagInspectorWrapper.isGlobalTagAllowed;
```
Explanation:

The `TrustedTagInspector` class has been removed in the new version of the library, so we need to wrap it in a custom class and use the wrapper instead. We create a `TrustedTagInspectorWrapper` class that contains a private static final instance of `TrustedTagInspector` and exposes a static method `isGlobalTagAllowed` that forwards the call to the wrapped `TrustedTagInspector` instance.

By doing this, we avoid using the removed `TrustedTagInspector` class and instead use our own wrapper class that still provides the same functionality. The `isGlobalTagAllowed` method is now a static method, so we import it statically and use it directly in the client code.