Here's a proposed patch to fix the failure:
```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(false, () -> java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
The change is to replace `java.lang.String.format("Status: Downloaded newer image for %s", image)` with `()->java.lang.String.format("Status: Downloaded newer image for %s", image)`.


The reason for this change is that the `StringContains` constructor that takes a `boolean` and a `java.lang.String` argument has been removed in the new version of the library. Instead, there is a new constructor that takes a `Supplier<java.lang.String>` argument, which can be used to supply a string that is computed lazily.

By using a lambda expression to create a supplier that formats the string with the `image` parameter, we can work around the removal of the old constructor and still achieve the desired result.