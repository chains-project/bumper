Here is a possible patch for the failing client code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new org.hamcrest.core.StringContains.StringStartsWith(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```
This patch uses the `StringStartsWith` matcher from Hamcrest instead of `StringContains`, as the latter does not have a constructor that takes a `String` argument. The `StringStartsWith` matcher checks if a string starts with a given substring, which should be sufficient for the purpose of this code.