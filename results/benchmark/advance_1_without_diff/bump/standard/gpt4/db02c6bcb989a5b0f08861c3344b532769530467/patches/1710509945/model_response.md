-- org.hamcrest.core.StringContains(boolean, java.lang.String)
++ org.hamcrest.core.StringContains(java.lang.String)

Here is the fixed client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```