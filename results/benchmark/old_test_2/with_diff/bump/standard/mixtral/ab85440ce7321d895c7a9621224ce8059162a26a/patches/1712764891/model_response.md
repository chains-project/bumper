Here is the proposed patch for the failing method:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.stringContains(String.format("Status: Downloaded newer image for %s", image));
}
```

The `CoreMatchers` class was added in the new library version, and it provides a `stringContains` method that takes a single `String` argument. This method can be used instead of the `StringContains` constructor, which takes a `boolean` and a `String` argument.