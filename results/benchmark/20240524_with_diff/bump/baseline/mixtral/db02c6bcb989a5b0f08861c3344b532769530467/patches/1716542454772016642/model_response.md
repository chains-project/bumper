Here's the fixed version of the method using the new library version:

```java
private static Matcher<String> imagePulled(final String image) {
    return new StringContains(String.format("Status: Downloaded newer image for %s", image));
}
```

The `false` argument passed to the `StringContains` constructor is no longer required in the new library version, so it has been removed.