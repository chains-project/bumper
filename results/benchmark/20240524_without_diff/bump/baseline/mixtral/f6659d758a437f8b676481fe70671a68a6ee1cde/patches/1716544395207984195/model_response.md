Here's the proposed patch:
```java
import org.yaml.snakeyaml.inspector.TrustedPrefixesTagInspector;

// Create a trusted tag inspector
TrustedPrefixesTagInspector trustedTagInspector = new TrustedPrefixesTagInspector(/* empty list */);

// Use the trusted tag inspector
// ...
```
This code creates a `TrustedPrefixesTagInspector` instance, which is a replacement for the removed `TrustedTagInspector`. You can use this instance in the same way as you used the `TrustedTagInspector` before.

Note that the `TrustedPrefixesTagInspector` constructor takes a `List` of trusted prefixes as an argument. In this example, I've passed an empty list. You can adjust the list according to your needs.

Also, the `TrustedPrefixesTagInspector` class does not have an `isGlobalTagAllowed` method. Instead, you can use the `isTagAllowed` method:
```java
// Instead of:
// isGlobalTagAllowed(tag)
boolean isTagAllowed = trustedTagInspector.isTagAllowed(tag);
```
This should fix the error and allow you to use the new version of the library.