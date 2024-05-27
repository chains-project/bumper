Here is the proposed patch for the failing client code:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return org.hamcrest.CoreMatchers.startsWith(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```
In the updated library version, the `StringContains` constructor no longer accepts a boolean argument, so we can use the `startsWith` matcher from `CoreMatchers` instead.