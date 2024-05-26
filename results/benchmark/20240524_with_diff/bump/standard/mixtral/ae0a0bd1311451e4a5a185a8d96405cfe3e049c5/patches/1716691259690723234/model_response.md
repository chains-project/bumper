Here is the updated `imagePulled` method that should resolve the error:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePosed(final java.lang.String image) {
    return org.hamcrest.Matchers.stringContains(String.format("Status: Downloaded newer image for %s", image));
}
```

The `StringContains` constructor has been removed in the new version of the library, and it has been replaced with the `stringContains` method in the `Matchers` class.