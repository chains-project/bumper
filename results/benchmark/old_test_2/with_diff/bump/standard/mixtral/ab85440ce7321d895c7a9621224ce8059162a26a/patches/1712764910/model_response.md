Here is the proposed patch for the failing method:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.Matchers.containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

In the new version of the library, the `StringContains` constructor has been changed to only accept a single `String` argument, instead of a `boolean` and a `String`. Therefore, we need to use the `containsString` method from `Matchers` class instead.