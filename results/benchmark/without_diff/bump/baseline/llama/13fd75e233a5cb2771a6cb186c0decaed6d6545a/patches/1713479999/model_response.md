Here's a proposed patch to fix the error:
```java
private static Matcher<String> imagePulled(final String image) {
    return new AllOf(
        new StringContains(false, "Status: Downloaded newer image for " + image),
        new StringContains(false, " pulling image ")
    );
}
```
The `StringContains` constructor taking two parameters is not available in the version of the Hamcrest library being used, so we're replacing it with `AllOf` and two `StringContains` objects.