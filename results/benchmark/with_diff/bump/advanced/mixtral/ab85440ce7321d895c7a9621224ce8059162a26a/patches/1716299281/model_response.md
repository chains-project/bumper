Here's a fixed version of the code that should work with the new library version:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains.ContainsString(String.format("Status: Downloaded newer image for %s", image));
}
```

The change that was made is to use the new `ContainsString` constructor that takes a single `String` argument instead of the old `StringContains` constructor that takes a `boolean` and a `String`. This should fix the error message you were seeing about the argument lists differing in length.