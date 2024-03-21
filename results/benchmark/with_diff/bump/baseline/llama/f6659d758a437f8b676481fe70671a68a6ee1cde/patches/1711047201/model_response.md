Here's a proposed patch to fix the error:
```
import org.yaml.snakeyaml.inspector.TrustedTagInspector;

public class TrustedTagInspectorWrapper {
    private static final TrustedTagInspector instance = new TrustedTagInspector();

    public static boolean isGlobalTagAllowed(Tag tag) {
        return instance.isGlobalTagAllowed(tag);
    }
}
```
Then, replace the failing line with:
```
TrustedTagInspectorWrapper.isGlobalTagAllowed(tag)
```
The patch creates a wrapper class, `TrustedTagInspectorWrapper`, that holds a static instance of `TrustedTagInspector` and provides a method, `isGlobalTagAllowed`, that delegates to the corresponding method in `TrustedTagInspector`. This allows the client code to continue using the `TrustedTagInspector` class, while the actual implementation is now in the wrapper class.

Since the `TrustedTagInspector` class has been removed in the new version of the library, the wrapper class provides a way to preserve the functionality of the removed class, without modifying the client code that uses it.