Here's the proposed patch:
```java
import org.yaml.snakeyaml.inspector.TrustedPrefixesTagInspector;

// Create a new TrustedTagInspector using the TrustedPrefixesTagInspector constructor
TrustedPrefixesTagInspector trustedTagInspector = new TrustedPrefixesTagInspector(/* pass any necessary arguments here */);
```
Note: You'll need to replace the comment `//` with the necessary arguments for the `TrustedPrefixesTagInspector` constructor.

Explanation:

The `TrustedTagInspector` class has been removed in the new library version, but a new class `TrustedPrefixesTagInspector` has been added, which provides similar functionality.

Therefore, we can create a new `TrustedPrefixesTagInspector` object using its constructor and use it instead of the removed `TrustedTagInspector` class.

The `TrustedPrefixesTagInspector` constructor takes a list of prefixes as an argument. If you don't need to specify any prefixes, you can pass an empty list `Collections.emptyList()` as an argument.

Note that the `TrustedPrefixesTagInspector` class does not have an `isGlobalTagAllowed()` method, but it has a similar method called `isTagAllowed()` that you can use instead.

Here's an example of how you can use the `TrustedPrefixesTagInspector` class:
```java
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.nodes.Tag;
import java.util.Collections;
import java.util.List;

public class Test {
    public static void main(String[] args) {
        Yaml yaml = new Yaml(new TrustedPrefixesTagInspector(Collections.emptyList()));

        // Use the yaml object to load or dump YAML documents
        // ...

        // Check if a tag is allowed
        Tag tag = new Tag("!foo");
        boolean isTagAllowed = yaml.getTagHandler().isTagAllowed(tag);
        System.out.println("Is tag allowed: " + isTagAllowed);
    }
}
```
In this example, we create a new `Yaml` object using a `TrustedPrefixesTagInspector` object with an empty list of prefixes. We can then use the `Yaml` object to load or dump YAML documents as usual.

We can also check if a tag is allowed using the `isTagAllowed()` method of the `TagHandler` object returned by the `Yaml` object. Note that the `isTagAllowed()` method takes a `Tag` object as an argument, not a string.

Therefore, you'll need to replace any occurrence of `isGlobalTagAllowed()` method with `isTagAllowed()` method and pass a `Tag` object as an argument instead of a string.

Here's an example of how you can replace the `isGlobalTagAllowed()` method with `isTagAllowed()` method:

Before:
```java
if (trustedTagInspector.isGlobalTagAllowed("!foo")) {
    // Do something
}
```
After:
```java
Tag tag = new Tag("!foo");
if (yaml.getTagHandler().isTagAllowed(tag)) {
    // Do something
}
```
Note that you'll need to replace `trustedTagInspector` with `yaml.getTagHandler()` and `"!foo"` with a `Tag` object.

You'll also need to replace any occurrence of `TrustedTagInspector` with `TrustedPrefixesTagInspector` and pass any necessary arguments to its constructor.

I hope this helps!