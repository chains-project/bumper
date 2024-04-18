Here is the proposed patch for the failing method:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringStartsWith(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
In the updated version of the library, the `StringContains` constructor no longer accepts a boolean argument. Instead, you can use the `StringStartsWith` matcher to check if a string starts with a specific substring.