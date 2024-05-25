Here is a possible patch for the failing method:

```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

In this patch, we replace the `StringContains` constructor with the `containsString` method from the `CoreMatchers` class, which is an added library method identified with `++`. This method accepts a single argument of type `String` and returns a `Matcher<String>` instance, which is compatible with the return type of the `imagePulled` method.

Note that this patch assumes that the `CoreMatchers` class is available in the classpath. If it is not, you may need to import it explicitly by adding the following import statement at the beginning of the file:

```java
import static org.hamcrest.CoreMatchers.containsString;
```