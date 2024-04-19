Here's a fixed version of the code that uses a different Hamcrest matcher, `StringStartsWith`, which only takes a single `String` argument:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringStartsWith(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
This should compile and run without error.