```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    boolean isNegated = false;
    return new org.hamcrest.core.StringContains(isNegated, java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```