I cannot see the complete code, but I can still provide a possible solution for the failing method. I will replace the usage of the `StringContains` constructor with the `containsString` method from the `org.hamcrest.CoreMatchers` class, which is an added library method identified with `++`.

Here's the patched method:

```java
private static Matcher<String> imagePulled(final String image) {
    return CoreMatchers.containsString(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This solution assumes that the required Hamcrest libraries are already updated to a version that includes the `containsString` method.